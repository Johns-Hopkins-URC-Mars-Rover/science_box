import rclpy

from gpiozero import AngularServo
from DRV8825 import DRV8825

import base_motor.PublisherSubscriber.subscriber as sub

nema = DRV8825(13, 18, 24, 10, 9, 11) #probably need to replace all these

servo1 = AngularServo(5) #gpio pin numebrs 
servo2 = AngularServo(6)

def receive_data(data):
    
    

def main(args=None):
    rclpy.init(args=args)

    subscriber = sub.Subscriber('science_subscriber', "science_box", receive_data)
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()