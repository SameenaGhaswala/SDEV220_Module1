def test(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@test
def greet():
    print("Hello")
greet()