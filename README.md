**RSA Digital Signature***
============
This work is a mini-project under the course IT4010E - Introduction to Cryptography and Security.
Supervisor: Assoc. Prof. NGUYEN Khanh Van

This repository contains all folders of our project about "RSA Digital Signature".
---

## RSA-digital-signature
### Usage
#### RSA
* Go to the project directory - `cd <cloned-repo>`
* Go to the application directory - `cd rsa`
* Generate keys - `python generate_keys.py`.
    * The keys are generated and stored under the application directory `rsa/`
* Encrypt message - `python encrypt.py`
* Decrypt message - `python decrypt.py`

#### SHA-1
* Make a txt file store hashing document
* Hash document - `python sha1.py filename`

#### Sign document
* Make a signature on a document - `python sign.py filename`

#### Verify a signature
* Verigy signature - `python verify.py signature_filename`
