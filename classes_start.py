"""
Example file for working with Classes - LinkedIn Learning
"""


class MyClass:
    def method1(self):
        print("MyClass: ", MyClass.method1.__name__)

    def method2(self, some_string):
        print("MyClass: ", MyClass.method2.__name__, " ", some_string)


class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print(AnotherClass.__name__, " ", AnotherClass.method1.__name__)

    def method2(self, some_string):
        print(AnotherClass.__name__, " ", AnotherClass.method2.__name__)


def main():
    c = MyClass()
    c.method1()
    c.method2("This is a String")

    c2 = AnotherClass()
    c2.method1()
    c2.method2("This is a String")


main()
