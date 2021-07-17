import numpy as np
import rclpy
from serial import Serial
from rclpy.node import Node
from geometry_msgs.msg import Twist
usb_port = '/dev/ttyUSB0'
baud_rate = 115200

try:
    ser = Serial(usb_port, baud_rate)
    print(f'{ser.name} successfully initialized')
except:
    print(f'Check whether pyserial is installed in your system, or {usb_port} not found. Please CHMOD to others.')

class EncoderPublisher(Node):
    def __init__(self):
        super().__init__('right_encoder_publisher')
        self.publisher_ = self.create_publisher(Twist, 'right_encoder', 10)
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.encoder_callback)
        self.time_multiplier = 100.0

    def encoder_callback(self):
        raw_arduino_data = ser.readline()
        ser.flush()
        # print(raw_arduino_data)
        try:
            raw_arduino_data = int(raw_arduino_data[0:len(raw_arduino_data) - 2], 10)
            revolution = raw_arduino_data / 1440.0 # kaiten pulse = 360 count = 360 * 4 = 1440 (1 pulse = 4 count)
            velocity_ms = round(revolution * 2.0 * 0.125 * np.pi, 6) * 100.0
            velocity_kmh = round(revolution * 2.0 * 0.125 * np.pi * 3.6, 6) * 100.0
        except:
            pass
        msg = Twist()
        msg.linear.x = velocity_ms
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: m/s: {msg.linear.x:.3f}, km/h: {velocity_kmh:.3f}')

def main(args=None):
    rclpy.init(args=args)
    right_encoder_publisher = EncoderPublisher()
    rclpy.spin(right_encoder_publisher)
    right_encoder_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
