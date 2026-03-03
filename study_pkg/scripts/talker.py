
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

class Talker(Node):

    def __init__(self):
        super().__init__('even_pub')
        
        # Создаем паблишер для целых чисел
        self.num_pub = self.create_publisher(Int8, '/even_numbers', 10)
        self.overflow_pub = self.create_publisher(Int8, '/overflow', 10)

        # Таймер срабатывает 10 раз в секунду (период 0.1 секунды)
        timer_period = 0.1 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Начальное значение счётчика
        self.counter = 0
        
        self.get_logger().info("Узел запущен! Каждую секунду отправляю по 10 чётных чисел.")

    def timer_callback(self):
        for _ in range(10):
            msg = Int8()
            msg.data = self.counter
            self.num_pub.publish(msg)  
            self.get_logger().info(f"Опубликовано: {msg.data}")
            self.counter += 2
            
            if self.counter >= 100:  
                ovf_msg = Int8()
                ovf_msg.data = self.counter
                self.overflow_pub.publish(ovf_msg)
                self.get_logger().warn(f"Отправлено в /overflow: {self.counter}")
                self.counter = 0 

def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
