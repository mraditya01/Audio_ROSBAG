import socket
import pickle
import struct
import soundfile
import queue
import time
import threading

Size = 2048
def main():
    print("Server starting")
    # os.remove("test.wav")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.56.101', 8984))
    s.listen()
    data = b''
    print("Listening")
    payload = struct.calcsize("Q")
    q = queue.Queue()
    
    while True:
        conn, adr = s.accept()
        print(f"New address {adr} is connected")
        data = b''
        n=0
        try:
            start = time.time()
            with soundfile.SoundFile('test.wav', mode='x', channels = 8, samplerate=44100, subtype="PCM_16") as file:
                while True:
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
                    q.put(pickle.loads(data))
                    data = b''
                    file.write(q.get())
                    print(time.time()- start)

        except KeyboardInterrupt:
            print(n/44100)
            s.close()
            break
            # pass
        
if __name__ == "__main__":
    t1 = threading.Thread(target=main, args=())
    t1.start()
