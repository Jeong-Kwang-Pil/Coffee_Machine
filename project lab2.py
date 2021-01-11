menu = '''Coffee menu!
1. 아메리카노     2000
2. 카페라떼     2500
3. 카푸치노     3000
4. 케러멜마키아또       4000
0. 주문 종료
종류 ? '''
print("환영합니다. 음료를 선택하세요")
total = 0
while True:
    me= int(input(menu))
    if me == 0:
        print()
        print(" 주문 종료 ".center(18,"*"))
        break
    else :
        cnt=int(input('수량 ? '))
        if me == 1:
            total += cnt*2000
            print("\n%s %d개 주문"%('아메리카노', cnt))
        elif me == 2:
            total += cnt*2500
            print("\n%s %d개 주문"%('카페라떼', cnt))
        elif me == 3:
            total += cnt*3000
            print("\n%s %d개 주문"%('카푸치노', cnt))
        elif me == 4:
            total += cnt*4000
            print("\n%s %d개 주문"%('캐러멜마키아또', cnt))
        else:
            print('모르겠어요.')
        print("현재 주문 가격: %d"%total)
        print()
print('총 주문 가격: %s'%total)
print(' 안녕 '.center(30,"="))