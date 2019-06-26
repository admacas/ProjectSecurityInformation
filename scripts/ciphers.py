
def a1z26Cipher(ciphertext):
    listAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=''
    for frase in ciphertext.split(' '):
        for letter in frase.split('-'):
            result+=listAlphabet[int(letter)-1]
        result+=' '
    return result


def atbashCipher(ciphertext):
    listAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=''
    for frase in ciphertext.split():
        for letter in frase.upper():
            if letter not in listAlphabet:
                result+=letter
            else:
                result+=listAlphabet[25-listAlphabet.index(letter)]
        result+=' '
    return result


def caesarCipher(ciphertext):
    listAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=''
    for frase in ciphertext.split(' '):
        for letter in frase.upper():
            if letter not in listAlphabet:
                result+=letter
            else:
                result+=listAlphabet[listAlphabet.index(letter)-3]
        result+=' '
    return result


def combinendCipher(criptedtext):
    criptedtext = a1z26Cipher(criptedtext)
    criptedtext = atbashCipher(criptedtext)
    criptedtext = caesarCipher(criptedtext)
    return criptedtext

