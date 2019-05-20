#!/usr/bin/env python3

import argparse
from hashlib import sha1
from urllib import request
from getpass import getpass

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="store_true", help="Show more info including typed password and SHA1")
args = parser.parse_args()

password = ''

while password == '':
    password = getpass('Type a password to check: ')
    password_verify = getpass('Retype the password to confirm: ')

    if password != password_verify:
        print("Passwords do not match, please try again.")
        password = ''

    elif password == '':
        print("You must enter a password to check")

hash_object = sha1(password.encode())
hex_digest = hash_object.hexdigest().upper()

if(args.verbose):
    print("----- Verbose Output -----")
    print("Password:", password)
    print("SHA1:", hex_digest)

url = "https://api.pwnedpasswords.com/range/" + hex_digest[0:5]

requestObj = request.Request(url, headers={'User-Agent': "pwned.py"})
result = request.urlopen(requestObj)
response = result.read().decode("utf-8")

compromised = False
comp_count = 0

for line in response.splitlines():
    tmp = line.split(':')
    if tmp[0].upper() == hex_digest[5:]:
        compromised = True
        comp_count = tmp[1]
        break

if compromised:
    print("Password compromised " + comp_count + " times.")
else:
    print("Password is not compromised.")
