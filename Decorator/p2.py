def decor(func):
    def inner():
        print('inner before called func')
        func()
        print('inner after called func')
    return inner
@decor
def func():
    print('function inside')
func=decor(func)
func()