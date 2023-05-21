#!/user/bin/python3

# 3 列表交集
num1_list = [1, 2, 3, 5]
num2_list = [5, 8, 9, 10]
print(set(num1_list).intersection(num2_list))

# 4 找超过 n / 2 次的数
num3_list = [1, 4, 5, 4, 4, 2, 4, 7, 4, 4, 4]
num3_list.sort()
print(num3_list[len(num3_list) // 2])

# 6 extend追加，直接加到原list；list也支持运算符+
num_tuple = (1, 2, 3)
num_set = {4, 5, 6}
l = list(num_set)
m = list(num_tuple)
l.extend(m)
print(l)

# 7
list7 = [1, 2, 3, 4, 5, 6]
# list7.insert(len(list7), 7)
list7.append(7)
list7.insert(0, 0)
print(list7)

list7.reverse()
print(list7)

print(list7.index(5))

list8 = [True, False, 0, 1, 2]

print(list8.count(True))
print(list8.count(False))
print(list8.count(2))

list9 = [True, 1, 0, 'x', None, 'x', False, 2, True]
list9.remove('x')
list9.pop(4)
list9.clear()
print(list9)

a = [3, 0, 8, 5, 7]
a = [1 if x > 5 else 0 for x in a]
print(a)

b = ['x', 'y', 'z']
for x in b:
    print(x, b.index(x))

c = [0, 1, 2, 4, 5, 6]
l1 = c[::2]
l2 = c[1::2]

# 拼接
a1 = [1, 4, 7, 2, 5, 8]
a2 = ['x', 'y', 'z']
# i = 3
# for x in a2:
#     a1.insert(i,x)
#     i += 1
# print(a1)
# 如上可用切片操作
print(a1[:3:] + a2 + a1[3::])

a = [x for x in range(5, 50)]
aa = list(range(5, 50))

b1 = ['x', 'y', 'z']
b2 = [1, 2, 3]
aaa = list(zip(b1, b2))
print(aaa)

a_dict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# b_cit = [x for x in a_dict]
# b_cit2 = [a_dict.get(x) for x in a_dict]
print(a_dict.keys(), a_dict.values(), a_dict.items())
a_dict.setdefault('David', 19)
a_dict['Cecil'] = 17
print(a_dict)

# 32
list_c = ['a', 'b', 'c', 'd']
dict_c = {}
for x in list_c:
    dict_c.setdefault(x, 0)
print(dict_c)

# fromkeys
print({}.fromkeys('a b c d'.split(), 0))

list_33 = [['a', 1], ['b', 2]]
tuple_33 = (('c', 1), ('d', 2))
dict_33_a = {}
for x in list_33:
    dict_33_a.setdefault(x[0], x[1])
print(dict_33_a)

#
A_TUPLE = (1, 5, 3, 4, 2, 2)
print(A_TUPLE.count(2))

for x in A_TUPLE:
    if x == 4:
        print('4 in list')
        break

A_TUPLE = A_TUPLE[:2:] + (9,) + A_TUPLE[2::]
print(A_TUPLE)

s1 = set().union([1, 2, 3])
print(s1)

#
a = '2.72, 5, 7, 3.14'.split(',')
conv = lambda x: float(x) if '.' in x else int(x)
print(list(map(conv, a)))
