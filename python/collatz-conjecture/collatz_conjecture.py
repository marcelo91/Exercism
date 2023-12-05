def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        count = 0
        while number != 1:
            if number%2 == 0:
                number = number/2 ## calc is n/2
                count += 1
                #print(number)
            else:
                number = (number*3) + 1 ## calc is 3n + 1
                count += 1
                #print(number)
        return count