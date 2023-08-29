import rosbag
import rospy
from std_msgs.msg import String
import soundfile
import pickle
import queue
import ast
import bagpy
import pandas as pd
import numpy as np

# q = queue.Queue()

# c = np.zeros([1,8])
# df_laser = pd.read_csv("/home/ubunturos/ROS/ROS_SEND/2023-03-08-18-38-01/sound_wav.csv")

# try:
#     with soundfile.SoundFile('test.wav', mode='x', channels = 8, samplerate=22050, subtype="PCM_16") as file:
#         for data in df_laser["data"]:
#             q.put(pickle.loads(ast.literal_eval(data)))
#             file.write(q.get())

# except KeyboardInterrupt:
#     print(n/44100)
#     # pass


from bagpy import bagreader

b = bagreader('/home/ubunturos/ROS/ROS_SEND/2023-06-24-12-16-26.bag')
bmesg = b.message_by_topic('/sound_wav')
