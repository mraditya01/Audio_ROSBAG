import soundfile
import pickle
import queue
import ast
import pandas as pd
import numpy as np

q = queue.Queue()
c = np.zeros([1,8])
names = ["/home/radit/Data/2023-06-24-13-09-04_534/sound_wav.csv", "/home/radit/Data/2023-06-24-13-08-59_533/sound_wav.csv",
        "/home/radit/Data/2023-06-24-13-09-09_535/sound_wav.csv", "/home/radit/Data/2023-06-24-13-09-14_536/sound_wav.csv",
         "/home/radit/Data/2023-06-24-13-09-19_537/sound_wav.csv", "/home/radit/Data/2023-06-24-13-09-24_538/sound_wav.csv",
         "/home/radit/Data/2023-06-24-13-09-29_539/sound_wav.csv", "/home/radit/Data/2023-06-24-13-09-34_540/sound_wav.csv",
         "/home/radit/Data/2023-06-24-13-09-39_541/sound_wav.csv"]

for n in names:
    df_laser = pd.read_csv(n)
    try:
        name = n.split("/")
        name = name[4]
        with soundfile.SoundFile(f'/home/radit/Data/Sounds/{name}.wav', mode='x', channels = 8, samplerate=44100, subtype="PCM_16") as file:
            for data in df_laser["data"]:
                q.put(pickle.loads(ast.literal_eval(data)))
                file.write(q.get())

    except KeyboardInterrupt:
        print(n/44100)
        # pass
