import random

SUBJECT = 0
CREDIT = 1
SCORE = 2

def ScoreToInt(s):
    match(s):
        case "A+":
            return 4.5
        case "A":
            return 4.0
        case "B+":
            return 3.5
        case "B":
            return 3.0
        case "C+":
            return 2.5
        case "C":
            return 2.0
        case "D+":
            return 1.5
        case "D":
            return 1.0
        case "F":
            return 0

def AddSubjectInDict(subjectName):
    temp = str(random.randrange(0,10000))
    while temp in subjectDict:              # 과목코드가 겹치지 않으면
        temp = str(random.randrange(0,10000))
    subjectDict[temp] = subject

def GetSubjectID(subjectName):
    for item in subjectDict.items():
        if subjectName in item:
            return item[SUBJECT]
        
###########################################################################################
subjectDict = {}
creditList = []


while(True):
    print("\n\n작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    match(input()):
        case '1':
            subject = input("\n과목명을 입력하세요:\n")
            credit = int(input("학점을 입력하세요:\n"))
            score = input("평점을 입력하세요:\n")
            
            if subject in subjectDict.values():  # 이전에 입력받은 똑같은 과목이 있다면
                for tSubject, tCredit, tScore in creditList:      
                    if subjectDict[tSubject] == subject:  # creditList에서 똑같은 과목의 정보를 발견하면
                        if ScoreToInt(tScore) < ScoreToInt(score):
                            creditList.remove(tuple((tSubject,tCredit,tScore)))
                            creditList.append(tuple((tSubject,credit,score)))
                        break;
            else:
                AddSubjectInDict(subject)
                creditList.append(tuple((GetSubjectID(subject), credit, score)))
                
            print("입력되었습니다.\n\n\n")


        case '2':
            for item in creditList:
                print('[' + subjectDict[item[SUBJECT]] + '] ' + str(item[1]) + '학점: ' + item[2])


        case '3':
            Credits = 0
            ## 총학점
            
            CreditScore = 0
            ## ∑평점x학점
            
            FCredit = 0
            ## F 학점

            for temp in creditList:
                Credits += temp[CREDIT]
                CreditScore += temp[CREDIT] * ScoreToInt(temp[SCORE])
                if temp[SCORE] == "F":
                    FCredit += temp[CREDIT]

            print("\n제출용: " + str(Credits - FCredit) + "학점 (GPA: " + str( CreditScore / (Credits-FCredit)) + ")")
            print("열람용: " + str(Credits) + "학점 (GPA: " + str( CreditScore / Credits ) + ")")  
            break;

print("\n\n프로그램을 종료합니다.")
