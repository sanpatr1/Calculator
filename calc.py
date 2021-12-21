class calc(object):
    def __init__(self, val1, val2):
        self.a = val1
        self.b = val2

    def add(self):
        return int(self.a) + int(self.b)
    def mul(self):
        return int(self.a) * int(self.b)
    def sub(self):
        return int(self.a) - int(self.b)
    def div(self):
        return int(self.a) / int(self.b)