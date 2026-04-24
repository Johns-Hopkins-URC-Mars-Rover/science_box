import rclpy
from rclpy.node import Node


import base_motor.PublisherSubscriber.subscriber as sub


def receive_data(data):
    pass

def main(args=None):
    rclpy.init(args=args)

    subscriber = sub.Subscriber('science_subscriber', "science_box", receive_data)
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()