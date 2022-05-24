def decorator1(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
def decorator2uppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@decorator1
@decorator2uppercase
def say_hi():
    return 'python is good language'
print(say_hi())
