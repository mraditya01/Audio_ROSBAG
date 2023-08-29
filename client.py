import struct
import pickle
import queue
import sys
import socket
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
import os
import threading
    
q = queue.Queue()
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())
    a = pickle.dumps(indata.copy())
    msg = struct.pack("Q", len(a)) + a
    c.sendall(msg)
    

def main():
    print(sd.query_devices())
    print("Starting Server")
    device = 30 # OCTA
    try:
        with sd.InputStream(samplerate = 44100, device=device, blocksize=2048*4,
                        channels=8, callback=callback, latency='low', dtype="int16"):
            print('#' * 80)
            print('press Ctrl+C to stop the recording')
            n=0
            while True:
                n += 1
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8196 #port no.
    # main()
    c.connect(('192.168.56.101', port))
    main()
    # t1 = threading.Thread(target=main, args=())
    # t1.start()