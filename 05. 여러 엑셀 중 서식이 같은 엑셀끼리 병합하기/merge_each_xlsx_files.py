import os
import pyexcel as px
import time
import sys

print("process start")
start_time = time.time()

HEADERS = []
CONTENT = []

input_folder = sys.argv[1]
output_folder = "merged_" + input_folder
if output_folder not in os.listdir():
    os.mkdir(output_folder)

files_name = os.listdir(input_folder)

for el in files_name:
    if ".xlsx" not in el:
        continue

    file = px.get_array(file_name=input_folder + "/" + el)
    header = file[0]
    content = file[1:]

    if header not in HEADERS:
        HEADERS.append(header)
        CONTENT.append([header])

    idx = HEADERS.index(header)
    CONTENT[idx] += content

for i in range(len(CONTENT)):
    px.save_as(array=CONTENT[i], dest_file_name=output_folder + "/" + str(i) + "_merged_file.xlsx")

print("process_done")
print("process_time : " + str(time.time() - start_time) + "초")
