birthday=input("생년월일을 입력하세요 (ex 1999 0723):")
               
while True:
    new = birthday.split()
    if int(new[1])>1300 or int(new[1])>1231:
        print("옳지않은 생년월일입니다.")
        birthday=input("생년월일을 입력하세요 (ex 1999 0723):")
    else:
        print("옳게 입력하셨습니다.")
        break
