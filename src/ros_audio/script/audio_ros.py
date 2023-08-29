import rospy
from std_msgs.msg import String, Byte, ByteMultiArray

import socket
import struct


Size = 2048*4


class IIImage(object):
    def __init__(self):
        self.ros_init()


    def ros_init(self):
        rospy.init_node('rgb2ii', anonymous=True)
        self.img_topic = rospy.get_param("~sound", "/sound_string")
        self.pub = rospy.Publisher('/sound_wav', String, queue_size=10)

    def to_wav(self):
        """Convert RGB image to illumination invariant image."""
        print("Server starting")
        # os.remove("test.wav")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.56.101', 8196))
        s.listen()
        data = b''
        print("Listening")
        payload = struct.calcsize("Q")
        while True:
            conn, adr = s.accept()
            print(f"New address {adr} is connected")
            data = b''
            n=0
            try:
                while not rospy.is_shutdown():
                    while len(data) < payload:
                        packet = conn.recv(Size)
                        data += packet
                    packed_msg_size = data[:payload]
                    data = data[payload:]
                    msg_size = struct.unpack("Q", packed_msg_size)[0]
                    while len(data) < msg_size:
                        packet = conn.recv(Size)
                        data += packet
                    data = data[:msg_size]
                    self.pub.publish(str(data))
                    data = b''
            except KeyboardInterrupt:
                s.close()
                break
                # pas


if __name__ == '__main__':
    image_convert = IIImage()
    image_convert.to_wav()
