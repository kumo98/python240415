strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # 전역변수 참조
        print(strName)

d = DemoString()
d.set("First Message")
d.print()
