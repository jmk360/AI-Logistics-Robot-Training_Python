dd = {}

def input_data():
    while True:
        name = input('이름: ')
        kor = int(input('국어: '))
        eng = int(input('영어: '))
        math = int(input('수학: '))
        dd[name] = (kor, eng, math)
        if input('계속 입력하시겠습니까(y/n)?') == 'n':
            break

def output_data():
    print('-'*100)
    print('\t이름\t국어\t영어\t수학')
    print('-'*100)
    for k in dd:
        print('\t{}\t{}\t{}\t{}'.format(k, *dd.get(k)))
    print('-'*100)

def search_data():
    name = input('검색할 이름을 입력하세요: ')
    print('-'*100)
    print('\t이름\t국어\t영어\t수학')
    print('\t{}\t{}\t{}\t{}'.format(name, *dd.get(name)))
    print('-'*100)

def main_menu():
    while True:
        print('메인 메뉴)')
        print('\t1. 입력')
        print('\t2. 출력')
        print('\t3. 검색')
        print('\t4. 종료')
        n = int(input('번호를 입력하세요: '))
        if n == 1:
            input_data()
        elif n == 2:
            output_data()
        elif n == 3:
            search_data()
        elif n == 4:
            break
