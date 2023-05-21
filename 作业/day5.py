#!/user/bin/python3
# day5
# 1 sum内置函数 列表表达式
print(sum(([x for x in range(1, 101) if x % 2])))

# 2 九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{x}*{y}={y * x}\t", end='')
    print()

# 3 打印指定图形
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

# 4 二进制
num = int(input("输入一个数"))
s = bin(num)

# 5 统计数
num_list = [1, 2, 2, 1, 4, 5, 7, 4, 7]
r_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in num_list:
    if r_list[x] == 0:
        r_list[x] = 1
    else:
        r_list[x] += 1

for x in range(0, len(r_list)):
    if r_list[x] == 1:
        print(x)

# 6 for
for x in range(1, 21):
    print(x, end='')


# 7
def say_hello():
    """
    打印函数
    :return:
    """
    print('fdas')
    print('fdassss')


if __name__ == '__main__':
    say_hello()
