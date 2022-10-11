'''
@author: Nihar Shah
HW01: Testing triangle classification, 14 September 2022
HW05: Static Code Analysis, 11 October 2022
''' 

def classifyTriangle(a, b, c):
    if (a > 100 or b > 100 or c > 100):
        return 'invalid triangle'

    if a <= 0 or b <= 0 or c <= 0:
        return 'invalid triangle'
        
    if a == b and b == c:
        return 'Equilateral triangle'

    elif ((a * a) + (b * b)) == (c * c) or ((c * c) + (b * b)) == (a * a) or ((a * a) + (c * c)) == (b * b):
        return 'Right angle triangle'

    elif a == b or b == c or a ==c:
        return 'Isosceles triangle'

    else:
        return 'Scalene triangle'

