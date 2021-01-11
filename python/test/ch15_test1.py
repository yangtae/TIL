class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = None

    def intro(self):
        print(f'{self.age}살 {self.name}입니다')

    def change(self,gender):
        self.gender = '남'
    
    def __str__(self): #단독으로 print 할 경우 동작
        return f'<Human {self.age}, {self.name}, {self.gender}>'

    def __repr__(self): #컬렉션에 담겨있는게 print될 때 동작
        return f'<Human {self.name}>'

kim = Human('김상형',29)
print(kim.name)
kim.intro()

lee = Human('이승우',45)
lee.intro()

li = [kim,lee]
print(li)