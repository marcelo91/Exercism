def is_valid(isbn):
    count = 1
    result = 0
    isbn = list(isbn.lower().replace('-',''))
    if len(isbn) == 10:
        for num in isbn:
            if num == 'x' and count == 10: 
                num = '10'
            if not num.isdigit():
                return False
            num = int(num)*count
            result = result + int(num)
            count += 1
        return result % 11 == 0
    else:
        return False