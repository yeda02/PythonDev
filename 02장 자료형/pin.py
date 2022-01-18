# pin = input("주민번호 13자리 입력하세요: ")

pin="9834561234567"
yymmdd = pin[:6]
gender = pin[6]

year="" #초기화 숫자면 0으로

age=0

if gender in "12":
    year = '19' + yymmdd[:2]
elif gender in "34":
    year = '20' + yymmdd[:2]

age = 2022 - int(year) + 1

print("당신의 출생년도는 {}년".format(year))
print("당신의 나이는 {}세".format(age))

if int(gender) % 2 ==0:
    print("여성입니다.")
else:
    print("남성입니다.")

