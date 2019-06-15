import string as st
def a1z26Cipher(ciphertext):
    listAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=''
    for frase in ciphertext.split(' '):
        for letter in frase.split('-'):
            result+=listAlphabet[int(letter)-1]
        result+=' '
    return result

#resultado=a1z26Cipher('22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1')
#print(resultado)
print(st.punctuation)