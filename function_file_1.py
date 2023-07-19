''''
def func1():
    print("outer function")
    def func2():
        print("inner function")
        
res = func1()
print(res)
'''

'''
def func1():
    print("Inside func1")

def func2(f):  # f = func1 address
    print(f)
    print("Inside func2")
    # None

res = func2(func1)  # func1 address
print(res)
'''
'''
def outer():
    print("inside outer - 1")
    def inner():  # local to outer function
        print("inside inner")
        return "Done"
    print("inside outer - 2")
    return inner()

res = outer()
print(res)
'''
'''
def outer():
    print("inside outer -1")
    def inner():
        print("inside inner")
        return None
    print("inside outer - 2")
    # return inner()
res = outer()
# print(res)
'''

def func1():
    print("inside func1 ")
    return None
def func2(func1):
    print("inside func2")
    return None
res = func2(func1)
print(res)
func1()
# func2()