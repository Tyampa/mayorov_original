#!/usr/bin/env python3
import rclpy                        # это главная библиотека ROS 2 для Python
from rclpy.node import Node         # от неё будем наследоваться
from std_msgs.msg import msg     # тип сообщения — просто строка

# ────────────────────────────────────────────────
# 1. Создаём класс — это и есть наш узел
# ────────────────────────────────────────────────
class Talker(Node):

    def __init__(self):
        # Даём узлу имя "talker"
        super().__init__('even_pub')

        # Создаём "почтовый ящик" — место, куда будем отправлять сообщения
        # Название топика → 'my_chat_topic'
        # Тип сообщения → строка
        # 10 — размер очереди (сколько сообщений можно временно держать)
        self.publisher = self.create_publisher(Int8, 'even_numbers', 10)

        self.overflow_publisher = self.create_publisher(String, 'overflow', 10)

        # Говорим: "каждую 1 секунду вызывай функцию timer_callback"
        timer_period = 1.0          # 1 секунда = 1 Гц
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0

        self.get_logger().info("Узел talker запущен! 10 чисел в секунду")

    # ────────────────────────────────────────────────
    # 2. Эта функция будет вызываться каждую секунду
    # ────────────────────────────────────────────────
    def timer_callback(self):
        for _ in range(10):
             msg = Int8()
             msg.data = self.counter
             self.publisher.publish(msg)
             self.get_logger().info(f"Опубликовано: {msg.data}")
             self.counter += 2
            if self.couner >=100:
                ovf_msg = String()
                ovf_msg.data = f"Счётчик был {self.counter}. Сброс на 0."
                self.overflow_publisher.publish(ovf_msg)
                self.get_logger().warn(ovf_msg.data)
                self.counter=0



# ────────────────────────────────────────────────
# 3. Главная функция — точка входа
# ────────────────────────────────────────────────
def main():
    rclpy.init()                    # начинаем работать с ROS 2

    node = Talker()                 # создаём наш узел

    try:
        rclpy.spin(node)            # "крутимся" и ждём событий (таймеров, сообщений и т.д.)
    except KeyboardInterrupt:
        pass                        # если нажали Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2


if __name__ == '__main__':
    main()
