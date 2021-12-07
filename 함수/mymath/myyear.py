def yun(year):
    return '윤년' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '윤년아님'

def get_dee(year):
    return ["원숭이", "닭", "개", "돼지","쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", ][ year%12 ]
