
test = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
def answer(s):
    res = ''
    for i in range(len(s)):
        if ord(s[i]) <= 96: # If number is not a lowercase alphabet
            res += s[i]     # Then just keep it
        else:
            # Get the resulting char by using its distance from 'a'
            # and subtract from the distance to 'z'
            res += chr(122 - (ord(s[i]) - 97))
    return res

print answer(test)