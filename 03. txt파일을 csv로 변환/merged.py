import os
import time

start_time = time.time()
print("process start")

directory = "personal_info"

out_file = open("merged.csv", 'w')
files = os.listdir(directory)

headers = []
header_flag = False

for file in files:

    if ".txt" not in file:
        continue

    el = open(directory + "/" + file)

    contents = []

    for line in el:
        if ":" in line:
            temp = line.split(":")
            contents.append(temp[-1].strip())

            if len(contents) > len(headers):
                headers.append(temp[0].strip())

    if not header_flag:
        head = ", ".join(headers)
        out_file.write(head)
        header_flag = True

    content = ", ".join(contents)
    out_file.write("\n" + content)

    el.close()

out_file.close()
print("process done")
end_time = time.time()
print(str(end_time-start_time) + "초 소요됨")
