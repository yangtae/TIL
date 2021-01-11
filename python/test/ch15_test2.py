#누구의 계좌인지
#출금(withdraw)

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,money):
        self.balance += money
    
    def withdraw(self,money):
        if self.balance < money:
            raise Exception('잔액부족')
        self.balance -=money
        return money
    
    def inqurie(self):
        print(f'{self.owner}님의 남은 금액은 {self.balance}원입니다')

import traceback

try:
    account = Account('양태석',10000)
    account.deposit(1000)
    account.withdraw(5000)
    account.inqurie()
except Exception as e:
    print('예외',e)
    traceback.print_stack() #예외 위치까지 오는데 거친 함수 출력
    traceback.print_exc() # 구체적인 예외 내용을 출력
