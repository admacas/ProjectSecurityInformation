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
resu=caesarCipher('FDUOD, ZKB ZRQ\'W BRX FDOO PH?')
print(resu)



        