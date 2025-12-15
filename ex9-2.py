class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"你好，我是 {self.name}")

p = Person("Tom")
p.greet()
