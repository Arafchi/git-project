def SelectMenu():
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 계산")
    return int(input())

Credits = 0
## 총학점

CreditScore = 0
## ∑평점x학점

FCredit = 0
## F학점

while(SelectMenu() == 1):
    credit = int(input("\n\n학접을 입력하세요:\n"))
    Credits += credit

    match(input("평점을 입력하세요:\n")):
        case 'A+':
            CreditScore += credit * 4.5
            
        case 'A':
            CreditScore += credit * 4
            
        case 'B+':
            CreditScore += credit * 3.5
            
        case 'B':
            CreditScore += credit * 3
            
        case 'C+':
            CreditScore += credit * 2.5
            
        case 'C':
            CreditScore += credit * 2
            
        case 'D+':
            CreditScore += credit * 1.5
            
        case 'D':
            CreditScore += credit * 1
            
        case 'F':
            FCredit += credit
            
    print("입력되었습니다.\n\n\n\n")



print("제출용: " + str(Credits - FCredit) + "학점 (GPA: " + str( CreditScore / (Credits-FCredit)) + ")")
print("열람용: " + str(Credits) + "학점 (GPA: " + str( CreditScore / Credits ) + ")")
print("\n\n프로그램을 종료합니다.")
