import math 

def is_natural_number(x):
    return x/int(x) == 1


def is_pow_of_base(number, base, precision=5):
    result = round(math.log(number, base),5)
    return is_natural_number(result)

def is_pow_of_ten(number):
    return is_pow_of_base(number, 10)
    
if __name__ == '__main__':
    print(is_pow_of_ten(100))

