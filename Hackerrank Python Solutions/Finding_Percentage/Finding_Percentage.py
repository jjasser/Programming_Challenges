# User inputs name and three grades
# Will print name average grade

n = int(input())
marks = {}
for i in range(n):
    name, g1, g2, g3 = input().split(' ')
    p = (sum(map(float, (g1, g2, g3))))/3
    marks[name] = p
print('%.02f' % marks[input()])
