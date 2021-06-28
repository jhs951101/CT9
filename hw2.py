cnt = 0
products = {}

while True:
    name = input('상품명  :  ')
    
    if name in products:
        print('이미 있는 상품입니다.')
    else:
        price = int(input('가   격  :  '))
        products[name] = price
        cnt += 1

        if cnt >= 5:
            print()
            break

totalprice = 0

while True:
    buyproduct = input('구매할 상품  :  ')

    if buyproduct in products:
        totalprice += products[buyproduct]
    else:
        print(buyproduct, '은 없습니다!')
        break

print('총 구매금액  : ', totalprice)
