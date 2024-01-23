import rsa
from rsa.decrypt import decrypt
import sha1
import sys

from rsa.helpers import read_key

def usage():
    print('Usage: python verify.py <file> [<file> ...]')
    sys.exit()

def main():
    if len(sys.argv) < 2:
        usage()

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                signature = f.read()
            with open(filename[10:], 'rb') as f:
                content = f.read()

        except:
            print ('ERROR: Input file "{0}" cannot be read.'.format(filename))

        else:
            # hash
            h = sha1.SHA1()
            h.update(content)
            hex_sha = h.hexdigest()
            # decrypt
            keys = read_key('public')
            n = int(keys['n'])
            d = int(keys['e'])
            d_h = decrypt(signature, n, d)
            verify = ''
            if d_h == hex_sha:
                verify = 'OK'
            else:
                verify = 'FAIL'
            print("{0}  {1}".format(verify, filename))

if __name__ == '__main__':
    main()            