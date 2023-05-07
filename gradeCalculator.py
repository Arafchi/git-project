import random

COURSE = 0
CREDIT = 1
SCORE = 2

class CourseHistory:
    courseDict = {}
    def __init__(self):
        self.courseList = []


    @classmethod
    def AddCourseInDict(cls, courseName):
            if courseName in CourseHistory.courseDict.values():
                return

            tempCode = random.randrange(0,10000)
            while tempCode in CourseHistory.courseDict.keys():
                tempCode = random.randrange(0,10000)

            CourseHistory.courseDict[tempCode] = courseName
            return tempCode
        
    @classmethod
    def GetCourseID(cls, courseName):
        for item in CourseHistory.courseDict.items():
            if courseName in item:
                return item[COURSE]
        return CourseHistory.AddCourseInDict(courseName)
    

            
    def AddCourseInfo(self, nCourse, nCredit, nScore):
        for course, credit, score in self.courseList:
            if CourseHistory.courseDict[course] == nCourse:
                if ScoreToInt(score) < ScoreToInt(nScore):
                    self.courseList.remove((course, credit, score))
                    self.courseList.append((course, nCredit, nScore))
                return
            
        self.courseList.append((CourseHistory.GetCourseID(nCourse), nCredit, nScore))

    def PrintCourseInfo(self, courseName):
        for item in self.courseList:
            if item[COURSE] == CourseHistory.GetCourseID(courseName):
                print('[' + courseName + '] ' + str(item[CREDIT]) + '학점: ' + item[SCORE])
    def PrintAllCourseInfo(self):
        for course, credit, score in self.courseList:
             print('[' + CourseHistory.courseDict[course] + '] ' + str(credit) + '학점: ' + score)
    
    def Calculate(self):
        Credits = 0
            ## 총학점
            
        CreditScore = 0
            ## ∑평점x학점
                    
        FCredit = 0
        ## F 학점

        for temp in self.courseList:
            Credits += temp[CREDIT]
            CreditScore += temp[CREDIT] * ScoreToInt(temp[SCORE])
            if temp[SCORE] == "F":
                FCredit += temp[CREDIT]

        print("\n제출용: " + str(Credits - FCredit) + "학점 (GPA: " + str( CreditScore / (Credits-FCredit)) + ")")
        print("열람용: " + str(Credits) + "학점 (GPA: " + str( CreditScore / Credits ) + ")")  
                            
                
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
    return None




        
###########################################################################################

history = CourseHistory()

while(True):
    print("\n\n작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 조회")
    print("4. 계산")
    print("5. 종료")
    match(input()):
        case '1':
            course = input("\n과목명을 입력하세요:\n")
            credit = int(input("학점을 입력하세요:\n"))
            score = input("평점을 입력하세요:\n")
            
            history.AddCourseInfo(course, credit, score)
            print("입력되었습니다.\n\n\n")


        case '2':
            history.PrintAllCourseInfo()
            
        case '3':
            course = input("\n과목명을 입력하세요:\n")
            history.PrintCourseInfo(course)
            
        case '4':
            history.Calculate()
            
        case '5':
            break;

print("\n\n프로그램을 종료합니다.")
