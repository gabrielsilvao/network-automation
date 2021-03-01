import signal

print("press ctrl+c to interrupt the script")

def xyz():
    print("im xyz")

def keyboardInterruptHandler(signal, frame):
    xyz()
    # print("Call your function here")
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

while True:
    pass