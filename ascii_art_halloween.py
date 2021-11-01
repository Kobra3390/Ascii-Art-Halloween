import os, time, platform

if(platform.system() == "Windows"):
    clean = os.system('cls')
elif(platform.system() == "Linux"):
    clean = os.system('clear')

filenames = ["asci1.txt", "asci2.txt", "asci3.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
while True:
    for frame in frames:
        print("".join(frame))
        time.sleep(1)
        if(platform.system() == "Windows"):
            os.system('cls')
        elif(platform.system() == "Linux"):
            os.system('clear')