import os
import time

start_time = time.time()
print("process start")

dir_name = "personal_info"
out_name = "practice.txt"
out_file = open(out_name, "w")

input_files = os.listdir(dir_name)

for el in input_files:
    if ".txt" not in el:
        continue

    file = open(dir_name + "/" + el)

    content = file.read()

    out_file.write(content + "\n\n")
    file.close()

out_file.close()

print("process done")
end_time = time.time()
print("process time : " + str(end_time - start_time))