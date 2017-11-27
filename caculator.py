#计算器类
class Count:

    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
#计算加法
    def add(self):
        return self.a+self.b
#计算减法
    def sub(self):
        return self.a - self.b

#计算乘法
    def mul(self):
        return self.a * self.b
#计算除法
    def div(self):
        return self.a / self.b