#!/usr/bin/env python3
import hashlib

number = 1
while True:
    hash = hashlib.md5()
    hash.update(b"bgvyzdsv")
    temp = (bytes(str(number), 'ascii'))
    hash.update(temp)
    digest = hash.hexdigest()
    if digest.startswith('000000'):
        print('FOUND: moroz{}: {}'.format(number, digest))
    number += 1
