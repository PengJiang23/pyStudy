#!/user/bin/python3
class HouseItem(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name} {self.area}"


if __name__ == '__main__':
    chair = HouseItem('yizi', 12)
    file = open('../f.txt', encoding='utf8')
    text = file.read()
    print(text)
