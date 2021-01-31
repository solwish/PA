import time
import os
import random
import pyexcel as px

print("process start")
start_time = time.time()

HEADER = ["name", "age", "e-mail", "division", "telephone", "sex"]

first_name = "김오박현이신고"
middle_name = "병두진광수의명동"
last_name = "희솔환준환현동록"

email_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
email_group = ["naver.com", "kakao.com", "korea.kr"]

sex_group = ["M", "W"]


def make_name() :
    name = ""
    name += random.choice(first_name)
    name += random.choice(middle_name)
    name += random.choice(last_name)
    return name

def make_email(num) :
    email = ""
    for i in range(num):
        email += random.choice(email_alphabet)
    email += "@"
    email += random.choice(email_group)
    return email

def random_string(num) :
    temp = ""
    for i in range(num):
        temp += random.choice(email_alphabet)
    return temp

folder_name = "personal_info"
os.mkdir(folder_name)
NUM = 1000

for i in range(NUM):
    name = make_name()
    file_name = folder_name + "/" + str(i) + "_" + name + ".xlsx"

    age = str(start_time)[-2:]
    email = make_email(8)
    division = random_string(3).upper()
    telephone = "010-" + str(start_time)[-4:] + "-" + str(time.time())[-4:]
    sex = random.choice(sex_group)

    content = []
    content.append(HEADER)
    body = [name, age, email, division, telephone, sex]
    content.append(body)
    # content = [HEADER, body]

    px.save_as(array = content, dest_file_name = file_name)

print("process done")
end_time = time.time()

print("processing time : " + str(end_time - start_time))