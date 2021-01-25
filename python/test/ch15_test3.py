# 상속 예제문
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    
    def intro(self):
        print(f'{self.age} 살 {self.name}입니다')

class Student(Human):
    def __init__(self,name,age,stunum):
        super().__init__(name,age)
        self.stunum = stunum

    def intro(self):
        super().intro()
        print(f'학번 : {self.stunum}')

    def study(self):
        print('하늘천 따지 검을현 누를황')

kim = Human('김상형',29)
kim.intro()

lee = Student('이승우',25,93011)
lee.intro()
lee.study()