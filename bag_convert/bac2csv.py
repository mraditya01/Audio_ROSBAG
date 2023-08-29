from bagpy import bagreader


names = ["/home/radit/Data/2023-06-24-13-09-04_534.bag", "/home/radit/Data/2023-06-24-13-08-59_533.bag",
        "/home/radit/Data/2023-06-24-13-09-09_535.bag", "/home/radit/Data/2023-06-24-13-09-14_536.bag",
         "/home/radit/Data/2023-06-24-13-09-19_537.bag", "/home/radit/Data/2023-06-24-13-09-24_538.bag",
         "/home/radit/Data/2023-06-24-13-09-29_539.bag", "/home/radit/Data/2023-06-24-13-09-34_540.bag",
         "/home/radit/Data/2023-06-24-13-09-39_541.bag"]

for n in names:
    b = bagreader(n)
    bmesg = b.message_by_topic('/sound_wav')
