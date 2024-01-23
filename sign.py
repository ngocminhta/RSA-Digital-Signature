import rsa
from rsa.encrypt import encrypt
import sha1
import sys

from rsa.helpers import read_key

def usage():
    print('Usage: python sign.py <file> [<file> ...]')
    sys.exit()

def main():
    if len(sys.argv) < 2:
        usage()

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'rb') as f:
                content = f.read()

        except:
            print ('ERROR: Input file "{0}" cannot be read.'.format(filename))

        else:
            h = sha1.SHA1()
            h.update(content)
            hex_sha = h.hexdigest()
            
            keys = read_key('private')
            n = int(keys['n'])
            e = int(keys['d'])
            signature = encrypt(hex_sha, n, e)
            
            with open(filename, 'r') as f:
                content = f.read()
            send_mes = str(content) + '*/*/*/*' + str(signature)
            
            filename = 'signature_' + filename
            with open(filename, 'w') as f:
                f.write(str(signature))
            print('Signed document')
            print("{0}  {1}".format(send_mes, filename))

if __name__ == '__main__':
    main()            