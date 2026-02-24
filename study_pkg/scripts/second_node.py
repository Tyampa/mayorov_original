#!/usr/bin/env python3
"""Первый узел ROS 2 — Hello World"""

import rclpy
from rclpy.node import Node
from datetime import datetime
import time
def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = Node('node2')               # создаём узел с именем hello_node
    while True:
        t=datetime.now()
        pin = t.strftime("%Y-%m-%d %H:%M:%S")
        node.get_logger().info(pin)
        time.sleep(5)
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()