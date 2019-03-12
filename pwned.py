#!/usr/bin/env python3

import argparse
import hashlib
import urllib.request
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument("password", help="Password to check if pwned")
args = parser.parse_args()

hash_object = hashlib.sha1(args.password.encode())
hex_digest = hash_object.hexdigest().upper()
print("SHA1:", hex_digest)

url = "https://api.pwnedpasswords.com/range/" + hex_digest[0:5]

request = urllib.request.Request(url, headers={'User-Agent': "pwned.py"})
result = urllib.request.urlopen(request)
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
