
episodes_cripts = {
    1: 'WELCOME TO GRAVITY FALLS',
    2: 'NEXT WEEK: RETURN TO BUTT ISLAND',
    3: "HE'S STILL IN THE VENTS",
    4: "CARLA, WHY WONT YOU CALL ME?",
    5: "ONWARDS AOSHIMA!",
    6: "MR. CAESARIAN WILL BE OUT NEXT WEEK. MR. ATBASH WILL SUBSTITUTE",
    7: 'PAPER JAM DIPPER SAYS: "AUUGHWXQHGADSADSADUH!"',
    8: 'E. PLURIBUS TREMBLEY',
    9: 'NOT H.G. WELLS APPROVED',
    10: 'SORRY DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE',
    11: 'THE INVISIBLE WIZARD IS WATCHING',
    12: 'BROUGHT TO YOU BY HOMEWORK: THE CANDY',
    13: 'HEAVY IS THE HEAD THAT WEARS THE FEZ',
    14: 'NEXT UP: "FOOTBOT TWO: GRUNKLES GREVENGE."',
    15: 'VIVAN LOS PATOS DE LA PISCINA',
    16: 'BUT WHO STOLE THE CAPERS?',
    17: 'HAPPY NOW, ARIEL?',
    18: 'IT WORKS FOR PIIIIIIIIIIIIIIIIIGS!',
    19: 'TO BE CONTINUED...',
    20: 'SEARCH FOR THE BLINDEYE'
}


def a1z26Cipher(ciphertext):
    """
    The A1Z26 cipher is a simple substitution cipher decoded by substituting the nᵗʰ letter of the alphabet for given number n.
    @param: ciphertext: text to decode
    """

    listAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=''
    for frase in ciphertext.split(' '):
        for letter in frase.split('-'):
            result+=listAlphabet[int(letter)-1]
        result+=' '
    return result


def atbashCipher(ciphertext):
    """
    Atbash ciphers are decoded by reversing the letters. For example, an A turns into a Z.
    @param: ciphertext: text to decode
    """
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
    """
    The Caesar cipher used in Gravity Falls substitutes the original letter for the 
    third letter before it. In the case for letters X, Y, and Z, 
    one would have to cycle through to the beginning of the alphabet.
    @param: ciphertext: text to decode
    """
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
    """
    A combined cipher is a mix of two or more ciphers seen in the show. 
    The first time such cipher has been used is at the end of "Gideon Rises." 
    It's solved by converting to letters using the A1Z26 cipher, then flipping 
    the letters with the Atbash cipher, and finally by using the Caesar cipher. 
    Season 2's combined ciphers start with the Vigenère cipher.
    @param: ciphertext: text to decode
    """
    criptedtext = a1z26Cipher(criptedtext)
    criptedtext = atbashCipher(criptedtext)
    criptedtext = caesarCipher(criptedtext)
    return criptedtext


def numberCodes(criptedtext, key):
    """
    These codes are solvable by taking the number beside a parenthesis as an episode number, and the other numbers 
    beside them represents a letter in that episode's credits cryptogram.
    @param: criptedtext
    @param: keys: Dictionary with (episode_number: letter)
    """
    episode_number = ''
    char_number = ''
    words = criptedtext.split(' ')
    decrypted_message = ''
    for w in words:
        chars = w.split(',')
        for c in chars:
            if ')' in c:
                episode_number = c.split(')')[0].strip(' ').strip('[')
                char_number = c.split(')')[1]    
            else:
                char_number = c
            cryptogram = ''.join(key[int(episode_number)].split(' ')).replace(':', '').replace("\'", '')
            if ']' in char_number:
                char_number = char_number.strip(' ').strip(']')
                decrypted_message = decrypted_message + cryptogram[int(char_number) - 1] + ' '
            else:
                char_number = char_number.strip(' ').strip('[')
                decrypted_message = decrypted_message + cryptogram[int(char_number) - 1]

    return decrypted_message


def vigenere_enc(plaintext, key):
    result = ''
    i = 0
    for letter in plaintext.upper():    
        if (ord(letter) >= 65 and ord(letter) <= 90):
            k = key.upper()[i%len(key)]
            i += 1    	
            result += chr((ord(letter)-65+ord(k)-65)%26+65)
        else:
            result += letter
    return result

def vigenere_dec(ciphertext, key):
    result = ''
    i = 0
    for letter in ciphertext.upper():
        if (ord(letter) >= 65 and ord(letter) <= 90):
            k = key.upper()[i%len(key)]
            i += 1
            subs = ord(letter)%65-ord(k)%65
            result += chr(subs + (26 if subs<0 else 0) + 65)
        else:
            result += letter
    return result