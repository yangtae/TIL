import threading

def sum(low,high):
    total = 0
    for i in range(low,high):
        total +=i
    print('Subthread',total)

t= threading.Thread(target=sum,args=(1,100000)) #sum함수 사용
t.start()

print('Main Thread')