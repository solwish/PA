import os
import time

s_time = time.time()
print("process start")

# 폴더 열기 및 output 파일 만들기
dir_name = "sample_info"
out_name = "merged.txt"
out_file = open(out_name, 'w')

input_files = os.listdir(dir_name)

for el in input_files:
    if ".txt" not in el:
        continue

    # 각각의 파일 열기
    file = open(dir_name + "/" + el)

    content = file.read()

    out_file.write(content + "\n\n")

    file.close()

# merge txt 파일 저장
out_file.close()

print("process fin")
e_time = time.time()
print("작업시간 : " + str(e_time - s_time))


