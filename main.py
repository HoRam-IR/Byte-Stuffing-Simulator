import random

#generate kardan 1000 bit
data = ""
for _ in range(1000):
    data = data + str(random.choice([0, 1]))

print(len(data))
#framebandi be 100 ta 10 tayi
frames = []
frame = ""
for bit in data:
    frame = frame + bit
    if len(frame) == 10:
        frames.append(frame)
        frame = ""

stuffed_frames = ""     
#stuff kardan
for frame in frames:
    txt = frame
    if txt.find("101") != -1:
        txt = txt.replace("101", "100101")

    if txt.find("100") != -1:
        txt = txt.replace("100", "100100")

    if txt.find("100101") != -1:
        txt = txt.replace("100101", "100100100101")

    if txt.find("100100") != -1:
        txt = txt.replace("100100", "100100100100")

    txt = "101" + txt
    txt = txt + "101"

    stuffed_frames = stuffed_frames + txt

#joda kardan 101 haye aval va akhar har frame 10 biti
stuffed_frames = stuffed_frames + "101"
my_frames = []
while stuffed_frames.find("101101") != -1:
    find = stuffed_frames.find("101101")
    data = stuffed_frames[:find]
    data = data[3:]
    stuffed_frames = stuffed_frames[find+3:]
    my_frames.append(data) 
    
#destuffing
msg = ""
for frames in my_frames:
    txt = frames
    if txt.find("100100100100") != -1:
        txt = txt.replace("100100100100", "100100")
    
    if txt.find("100100100101") != -1:
        txt = txt.replace("100100100101", "100101")

    if txt.find("100100") != -1:
        txt = txt.replace("100100", "100")

    if txt.find("100101") != -1:
        txt = txt.replace("100101", "101")

    msg = msg + txt

print("=====================")
print(len(msg))