import random
import os
import time

print("Process Start")
start_time = time.time()

num_sample = 1000
alphabet_samples = "abcdefghijklmnopqrstuvwxyz1234567890"


# 랜덤 스트링
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result


first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤현진지"
last_name_samples = "준윤우원솔후서연아은진"


# 랜덤 이름
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


email_middle_samples = ["naver", "kakao", "korea", "nate"]
email_end_samples = ["com", "co.kr", "or.kr", "go.kr"]

# 폴더 생성
os.mkdir("sample_info")

for i in range(num_sample):
    name = random_name()

    # 빈 txt 파일 생성 및 열기
    filename = "sample_info/" + str(i) + "_" + name + ".txt"
    outfile = open(filename, 'w')

    # 연 txt 작성
    outfile.write("name : " + name + "\n")
    outfile.write("age : " + str(time.time())[-2:] + "\n")
    outfile.write("e-mail : " + random_string(8) + "@" + random.choice(email_middle_samples)
                  + "." + random.choice(email_end_samples) + "\n")
    outfile.write("division : " + random_string(3) + "\n")
    outfile.write("telephone : 010-" + str(time.time())[-4:] + "-" + str(time.time())[:4] + '\n')
    outfile.write("sex : " + random.choice(["male", "female"]))

    # 저장
    outfile.close()

print("Process done.")

end_time = time.time()
print("소요시간" + str(end_time - start_time) + "초")