def caesarCipher(ciphertext):
    listAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=''
    for letter in ciphertext.upper():
        indice= listAlphabet.index(letter)
        result+=listAlphabet[indice-3]
    return result
resu=caesarCipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(resu)



        