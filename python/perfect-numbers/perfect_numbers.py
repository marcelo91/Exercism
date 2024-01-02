def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    ali_sum = sum([num for num in range(1,number) if number%num == 0])
    if ali_sum == number: 
        return 'perfect'
    elif ali_sum > number: 
        return 'abundant'
    else: 
        return 'deficient'

#print(classify(28))