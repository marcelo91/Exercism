def is_pangram(sentence):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if alpha in sentence:
        return True
    else:
        return False
    
print(is_pangram('ola meu chacho'))
