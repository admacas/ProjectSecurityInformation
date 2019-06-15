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
resu=atbashCipher('KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"')
print(resu)