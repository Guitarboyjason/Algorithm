def star(func):
    def inner(*args, **kwargs):
        print("*"*30)
        func(*args,**kwargs)
        print("*"*30)
    return inner
@star
def printer(msg):
    print(msg)

printer("hello")