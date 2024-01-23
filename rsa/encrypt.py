import os
import base64
try:
    from rsa.helpers import read_key
except:
    pass
try:
    from helpers import read_key
except:
    pass

def encrypt(message, n, e):
    message_bytes = message.encode('utf-8')
    encoded_message = message_bytes.hex()
    
    encoded_message = int(encoded_message,16)
    encrypted_message = pow(encoded_message, e, n)
    
    return encrypted_message

def main():
    message = input("Enter message: ")
    message_bytes = message.encode('utf-8')
    encoded_message = message_bytes.hex()

    keys = read_key('public')
    n = int(keys['n'])
    e = int(keys['e'])
    
    print('')
    print('n:',n)
    print('e:',e)

    encrypted_message = encrypt(message, n, e)
    
    print('\n**********************************')
    print('Encrypted message:')
    print(encrypted_message)
    print('**********************************\n')


if __name__ == "__main__":
    main()