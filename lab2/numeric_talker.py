import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8  # Importing Int8 for numeric messages


class NumericTalker(Node):
    def __init__(self):
        super().__init__('numeric_talker')  # Fixed node name to 'numeric_talker'
        
        # Existing publisher for /chatter
        self.string_publisher = self.create_publisher(String, 'string_chatter', 10)
        
        # New publisher for /numeric_chatter
        self.numeric_publisher = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 1.0
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0  # Start from 0

    def talker_callback(self):
        # Creating messages
        string_msg = String()
        numeric_msg = Int8()

        # Set message data
        string_msg.data = f'Hello World, {self.counter}'
        numeric_msg.data = self.counter

        # Publish messages
        self.string_publisher.publish(string_msg)
        self.numeric_publisher.publish(numeric_msg)

        # Log output
        self.get_logger().info(f'Publishing: {string_msg.data}')
        self.get_logger().info(f'Sending Count: {numeric_msg.data}')

        # Increment counter and reset if it exceeds 127
        self.counter = (self.counter + 1) % 128  

def main(args=None):
    rclpy.init(args=args)

    numeric_talker = NumericTalker()
    rclpy.spin(numeric_talker)

    numeric_talker.destroy_node()  # Cleanup before shutdown
    rclpy.shutdown()


if __name__ == '__main__':
    main()
