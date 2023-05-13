#python_version == '3.6'
x = ['python is cool',
'pythom is a large heavy-bodied snake',
'The python course is worse taking',
'The python course is worse taking',
'The python course is worse taking python python python'
]


from functools import reduce
def word_count(x, str, n):
  a = list(filter(lambda x: (len(x) > 20), x))
  b = list(map(lambda n: n.count(str), a))
  c = reduce(lambda x,y: x+y, b)
  return c

# Test
print(word_count(x,'python',20))