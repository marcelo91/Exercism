def translate(text):
    vowel = ['a','e','i','o','u','x','y']
    count = 0
    text = text.lower().split()
    lst = []
    for x in text:
       
        if x[0] in vowel:
            if (x[0] == 'y' and x[1] in vowel) or (x[0] == 'x' and x[1] in vowel):
                x = x[1:]+x[0]+'ay'
                lst.append(x)
                continue
            x = x+'ay'
            lst.append(x)
            continue
        
        if x[0] not in vowel and 'y' == x[-1]:
            while x[count] not in vowel:
                count += 1
            x = x[count:]+x[0:count]+'ay'
            lst.append(x)
            continue
                
        if x[0] not in vowel and 'qu' in x:
            x = x[x.index('qu')+2:] + x[0:x.index('qu')] + 'quay'
            lst.append(x)
            continue

        if x[0] not in vowel and 'y' in x:
            while x[count] not in 'y':
                count += 1
            x = x[count:]+x[0:count]+'ay'
            lst.append(x)
            continue

        if x[0] not in vowel:
            while x[count] not in vowel:
                count += 1
            x = x[count:]+x[0:count]+'ay'
            lst.append(x)
            continue
            
    return ' '.join(lst)