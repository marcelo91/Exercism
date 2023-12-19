def rotate(text, key):
    alpha = list(range(27))
    rot = alpha[key:]+alpha[:key]
    dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']     
    dic_rot = [dic[num] for num in rot]
    if text == text.upper():
        return ''.join([dic_rot[dic.index(letter)] for letter in text.lower()]).upper()
    else:
        return ''.join([dic_rot[dic.index(letter)] for letter in text.lower()])

print(rotate('OMG',5))
#abcdefghijklmnopqrstuvwxyz
#fghijklmnopqrstuvwxyzabcde
