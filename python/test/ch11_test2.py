dates = ['월','화','수','목','금','토','일']
food = ['갈비탕','순대국','칼국수','삼겹살']

menu = zip(dates,food)

for d,f in menu:
    print(f'{d}요일 메뉴 : {f}')

menu_dic = dict(zip(dates,food))
print(menu_dic)