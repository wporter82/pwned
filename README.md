# Have I been Pwned?

All credit for this goes to [haveibeenpwned.com](https://haveibeenpwned.com/) and [Dr. Mike Pound's Computerphile video](https://youtu.be/hhUb5iknVJs) on the subject.

This is a simple python script that uses the haveibeenpwned API to determine if a password has been compromised. I make no claims to the validity of the data returned or accuracy of the system.

## Usage

    $ python pwned.py
    Type a password to check:
    Retype the password to confirm:
    Password compromised 3645804 times.

**NOTE: The password prompt will not show what you are typing for security reasons. If you have the need to see the password and SHA1 you can use the verbose option as shown below.


    $ python pwned.py -v
    Type a password to check:
    Retype the password to confirm:
    ----- Verbose Output -----
    Password: password
    SHA1: 5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8
    Password compromised 3645804 times.

## What is it doing?

The script will hash the password and send only the first 5 characters off to the API. The API returns a list of hashes that match and then locally the program will search through to find a match to your hash.

No passwords or full hashes are sent across the internet, so there is no concern for passwords becoming compromised by using this tool.
