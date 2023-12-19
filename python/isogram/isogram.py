def is_isogram(string):
    string = string.replace(' ','').replace('-','')
    string = string.lower()
    count = 0
    return len(string) == len(set(string))