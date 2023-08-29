import rospy
from std_msgs.msg import String
import soundfile
import pickle
import queue
import ast
q = queue.Queue()
b = 1
def callback(data):
    rospy.loginfo(f"Received Data: {data.data}")
    try:
    with soundfile.SoundFile('test.wav', mode='x', channels = 8, samplerate=44100, subtype="PCM_16") as file:
        while True:
            print("recording")
            q.put(pickle.loads(ast.literal_eval(data.data, protocol=2)))
            file.write(q.get())
    
def listener():
    rospy.init_node('to_wav', anonymous=True)
    rospy.Subscriber('/sound_wav', String, callback)
    rospy.spin()
        
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass