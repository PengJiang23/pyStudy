#!/user/bin/python3
def test(*args, **kwargs):
    print(args, kwargs)


class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(f"{self.name}今年{self.age}岁，身高{self.height}，每天早上跑")


class c():
    def run(self):
        print("dd")


class B(Person, c):
    def __eat(self):
        print('s')

    def run(self):
        print('fda')
        super().run()


if __name__ == '__main__':
    test(1, 43, 6, 8, 9, 0, 5, 0, name=1, testss=4)
    tb = B('xiaoming', 1, 1)
    tb.run()
    print(dir(Person))
    print(B.__mro__)
