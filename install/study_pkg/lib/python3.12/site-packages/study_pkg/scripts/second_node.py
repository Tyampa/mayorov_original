#!/usr/bin/env python3
"""Первый узел ROS 2 — Hello World"""

import rclpy
from rclpy.node import Node
import time
def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = Node('node2')               # создаём узел с именем hello_node
    t=time.ctime()
    while True:
        t=datetime.now()
        time.strftime("%Y:%m:%d:%X", [t])
        node.get_logger().info(time.strftime)
        time.sleep(5)
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()