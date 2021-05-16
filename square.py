def decor(area):
    def wrapper(num1, num2):
        if type(num1) == int and type(num2) == int:
            return area(num1 * num2)
        else:
            raise ValueError('It must be an integer')
    return wrapper


@decor
def area(num1, num2):
    return num1*num2



