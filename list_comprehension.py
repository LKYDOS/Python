#python_version == '3.6'
a = range(1, 12)
#1
b = list(map(lambda n: n * n, a))
# print(b)
c = list(map(lambda n: n + 2, a))
# print(c)
#2
d = list(filter(lambda x: (x <= 8), a))
# print(d)
e = list(map(lambda n: n * n, list(filter(lambda x: (x % 2 ==0), a))))
# print(e)