import os
import random
import time

print("process start")
start_time = time.time()

os.mkdir("personal_info")
num = 1000
alphabet_samples = "abcdefghijklmnopqrstuvwxyz1234567890"

def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤현진지"
last_name_samples = "준윤우원솔후서연아은진"

def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

for i in range(num):
    name = random_name()

    filename = "personal_info/" + str(i) + "_" + name + ".txt"
    outfile = open(filename, 'w')

    outfile.write("name : " + name + "\n")
    outfile.write("age : " + str(time.time())[-2:] + "\n")
    outfile.write("e-mail : " + random_string(8) + "@" + random_string(6) + ".com" + "\n")
    outfile.write("division : " + random_string(3) + "\n")
    outfile.write("telephone : 010-" + str(time.time())[-4:] + str(start_time)[-4:] + "\n")
    outfile.write("sex : " + random.choice(["M", "W"]))
    outfile.close()

print("process done")
end_time = time.time()
print(str(end_time - start_time))