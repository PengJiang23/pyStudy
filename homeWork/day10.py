import os


# 单例模式
class OneTest():
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance

    def __init__(self):
        if not OneTest.init_flag:
            print('初始化')
            OneTest.init_flag = True


# 捕获异常
def judge_num():
    try:
        num = int(input("input a num"))
        str1 = str(num)
        if str1[::-1] == str1:
            print("is a duicheng num")
        else:
            print("is not")
    except ValueError:
        print('aa')
        raise Exception("非整数")
    else:
        print('符合要求')


# 文件操作
class file_operation(object):
    file1 = open("./day 10_file.txt", mode='r+', encoding='utf8')

    @classmethod
    def file_rwa(cls):
        """
        中文占三个字节
        r+，读写方式，但是写会把文件开头进行替换
        w+，读写，写文件会覆盖整个文件
        :return:
        """
        file = open("./day 10_file.txt", mode='r+', encoding='utf8')
        # file.write('aaa')
        while True:
            text = file.readline()
            if not text:
                break
            print(text, end='')
        # 文本中的换行符也会被读取
        file.close()

    def file_copy(self):
        file = open("./day 10_file.txt", mode='r+', encoding='utf8')
        while True:
            text = file.readline()
            if not text:
                break
            file2 = open("./day_10copy.txt", mode='a+', encoding='utf8')
            file2.write(text)
        file.close()
        file2.close()

    def file_seek(self):
        file_operation.file1.seek(4)
        text = file_operation.file1.read()
        print(text)
        file_operation.file1.close()

    def rb_r_diff(self):
        """
        rb+和r+区别
        :return:
        """
        file = open("./day 10_file.txt", mode='r+', encoding='utf8')
        print(file.read())
        file1 = open("./day 10_file.txt", mode='rb+')
        file1.write(b'hello')
        file1.write('我'.encode('utf8'))
        print(file1.read())

    def file_rename(self):
        os.rename("a.txt", "a.txt")
        os.remove("a.txt")

    # 目录的深度优先遍历
    def dir_DFS(self, filepath, width):
        """
        深度，递归，先判断当前文件为目录？是递归，否打印
        :param filepath:
        :return:
        """
        for f in os.listdir(filepath):
            print(' ' * width + f)
            if  os.path.isdir(filepath + '/' + f):
                self.dir_DFS(filepath + '/' + f, width + 4)

if __name__ == '__main__':
    # a1 = OneTest()
    # print(a1)
    # a2 = OneTest()
    # print(a2)
    # judge_num()
    # file_operation.file_rwa()

    f1 = file_operation()
    # f1.file_copy()
    # f1.file_seek()
    # f1.rb_r_diff()
    # f1.file_rename()
    """
        os.listdir('./')
    os.mkdir('1')
    os.rmdir('1')
    print(os.getcwd())
    print(os.path.isdir('./day10.py'))
    # 改变工作目录
    os.chdir('../')
    print(os.getcwd())
    
    """
    # eval函数，对字符串快速转换，但存在安全隐患

    # 目录深度优先遍历
    f1.dir_DFS('../', 1)