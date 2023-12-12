def response(hey_bob):
    if hey_bob.isupper() and hey_bob.find('?') > 0:
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    if hey_bob.isspace() or set(hey_bob) <= set('\n\r\t'):
        return "Fine. Be that way!"    
    if hey_bob.strip().endswith('?'):
        return "Sure."
    else:
        return "Whatever."

var = 'clear \t'
#print(set(var) <= set('\n\r\t'))
# print(var.strip()[len(var.strip())-1])
print(response(var))
