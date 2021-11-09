# 类的知识
class Restaurant:
    """"第一次创建类"""
    # 构造函数，每次实例化必会调用,self有点类似this指针,并且类内定义方法必须先在参数列表写self，在写别的形参
    # 不像c++一样，只需要在init下，就是定义类成员属性，右侧是要赋给的值
    def __init__(self, name, type, number=0):
        self.r_name = name
        self.r_type = type
        self.s_number = number

    def r_describe(self):
        print(f"our restaurant's name is {self.r_name},and food type is {self.r_type}")

    def open(self):
        print("restaurant is opening")

    def set_number(self, number):
        if number < self.s_number:
            print("failed")
        else:
            self.s_number = number

    def increment_n(self, add):
        if add < 0:
            print("failed")
        else:
            self.s_number += add


# 将大类分解为小类，并在原本的类中创建一个实例
class Flavors:
    def __init__(self, fs):
        self.fs = fs

    def show_f(self):
        print(f"we have {len(self.fs)} flavours :")
        for f in self.fs:
            print(f)


# 继承（父类），super可以调用父类的方法
class IceCreamStand(Restaurant):
    def __init__(self, name, type, fs, number=0):
        super().__init__(name, type, number)
        # 使用小类作为属性
        self.arg = Flavors(fs)
