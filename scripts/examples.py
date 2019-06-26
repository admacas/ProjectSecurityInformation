
from ciphers import *

print('****** ATBASH EXAMPLE ******')
print('CRIPTED TEXT: KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"')
print('DECRIPTED: ', atbashCipher('KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"') + '\n\n')

print('****** A1Z26 EXAMPLE ******')
print('22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1')
print('DECRIPTED: ', a1z26Cipher('22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1') + '\n\n')
    
print('****** CAESAR EXAMPLE ******')
print('FDUOD, ZKB ZRQ\'W BRX FDOO PH?')
print('DECRIPTED: ', caesarCipher('FDUOD, ZKB ZRQ\'W BRX FDOO PH?') + '\n\n')

print('****** COMBINED CIPHER EXAMPLE ******')
print('16-19-12-12-9 1-9-6-12-20')
print('DECRIPTED: ', combinendCipher('16-19-12-12-9 1-9-6-12-20') + '\n\n')


print('****** NUMBER CODES EXAMPLES ******')
print('[1)14] [2)5,24 3)3] [5)7,9]')
print('DECRIPTED: ', numberCodes('[1)14] [2)5,24 3)3] [5)7,9]', episodes_cripts) + '\n\n')
print('[13)8,9,10] [14,17,22')
print('DECRIPTED: ', numberCodes('[13)8,9,10] [14,17,22', episodes_cripts) + '\n\n')
print('11)4,12,18] [12)8,9][17,18]')
print('DECRIPTED: ', numberCodes('11)4,12,18] [12)8,9] [17,18]', episodes_cripts) + '\n\n')

