
#text =  'Hello World! world!'
#key = 'CoMPuTeR'
#text = 'Test   Hello World! World! World! Ok 123'
#key = 'abc'

text = 'Looking'
#text = 154654
key = 'xytIIII789999iop'
#key = 123


def vigenereEncrypt(key, text):
    if isinstance(text, str) and isinstance(key, str):
        text = text.upper()
        key = key.upper()
        move = 0    
        textOut = ''
        for i in range(len(text)):  
            if text[i].isalpha():            
                textOut += (chr( 65 + ((ord(text[i]) - 65 + (ord(key[(i-move)%len(key)]) - 65))%26)))
            else:
                textOut += (text[i])
                move += 1    
        print(textOut)      
        return textOut
    raise Exception('Data type of key and text expected to be <str>')


def vigenereDecrypt(key, text):
    if isinstance(text, str) and isinstance(key, str):
        text = text.upper()
        key = key.upper()
        move = 0    
        textOut = '' 
        for i in range(len(text)):  
            #if 'A' <= text[i] <= 'Z':
            if text[i].isalpha():
                textOut += (chr(65 + ((ord(text[i]) - 65 - (ord(key[(i-move)%len(key)]) - 65))%26)))
            else:
                textOut += (text[i])
                move += 1    
        print(textOut)      
        return textOut
    raise Exception('Data type of key and text expected to be <str>')


text1 = (vigenereEncrypt(key, text))

vigenereDecrypt(key, text1)


