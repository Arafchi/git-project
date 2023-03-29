def SelectMenu():
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 계산")
    return int(input())

validCredit = 0
numOfLecture = 0
FCredit = 0
FNumOfLecture =0

while(SelectMenu() == 1):
    credit = int(input("\n\n학접을 입력하세요:\n"))
    numOfLecture += 1
    match(input("평점을 입력하세요:\n")):
        case 'A+':
            validCredit += credit * 4.5
            
        case 'A':
            validCredit += credit * 4
            
        case 'B+':
            validCredit += credit * 3.5
            
        case 'B':
            validCredit += credit * 3
            
        case 'C+':
            validCredit += credit * 2.5
            
        case 'C':
            validCredit += credit * 2
            
        case 'D+':
            validCredit += credit * 1.5
            
        case 'D':
            validCredit += credit
            
        case 'F':
            FCredit += credit
            FNumOfLecture += 1
            
    print("입력되었습니다.\n\n\n\n")



print("제출용: " + str(validCredit) + "학점 (GPA: " + str(validCredit/numOfLecture) + ")")
print("열람용: " + str(validCredit+FCredit) + "학점 (GPA: " + str((validCredit+FCredit)/(numOfLecture+FNumOfLecture)) + ")")
print("\n\n프로그램을 종료합니다.")
