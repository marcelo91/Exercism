def rotate(text, key):
    dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rot = dic[key:]+dic[:key]
    rtn = [rot[dic.index(letter.lower())].upper() if letter.isalpha() and letter.isupper()
        else rot[dic.index(letter)] if letter.isalpha() else letter for letter in text]
    
    # for letter in text:
    #     if letter.isalpha() and letter.isupper():
    #         rtn.append(rot[dic.index(letter.lower())].upper())
    #     if letter.isalpha():
    #         rtn.append(rot[dic.index(letter)])
    #     else:
    #         rtn.append(letter)
    
    return ''.join(rtn)
