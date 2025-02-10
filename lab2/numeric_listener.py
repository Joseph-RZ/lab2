import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class NumericListener(Node):
    def __init__(self):
        super().__init__('numeric_listener')  # Initialize the node

        # Create subscriptions
        self.string_subscription = self.create_subscription(
            String, 'chatter', self.string_callback, 10)
        self.numeric_subscription = self.create_subscription(
            Int8, 'numeric_chatter', self.numeric_callback, 10)

        # Prevent unused variable warning
        self.string_subscription
        self.numeric_subscription  

    def string_callback(self, msg):
        """Callback for /chatter topic."""
        self.get_logger().info(f'I heard: {msg.data!r}')

    def numeric_callback(self, msg):
        """Callback for /numeric_chatter topic."""
        self.get_logger().info(f'Received number: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    node = NumericListener()  # Initialize the node
    rclpy.spin(node)  # Keep node running


if __name__ == '__main__':
    main()
