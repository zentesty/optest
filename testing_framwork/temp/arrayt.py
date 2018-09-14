'''
    Class test

'''


class MyClass:
    array_temp = []

    def __init__(self):
        for x in range(0, 10):
            self.array_temp.append(self.MyInnerClass("Blue_" + str(x)))

    def call_my_array(self):
        for x in self.array_temp:
            print(x.color)

    class MyInnerClass:
        color = "ZColor"

        def __init__(self, val):
            self.color = val


myObj = MyClass()
myObj.call_my_array()
