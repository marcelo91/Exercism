def is_armstrong_number(number):
    result = 0
    count = sum(x.isnumeric() for x in str(number))
    result = sum(int(x)**count for x in str(number))
    
    return result == int(number)