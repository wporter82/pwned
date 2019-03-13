# Have I been Pwned?

All credit for this goes to [haveibeenpwned.com](https://haveibeenpwned.com/) and [Dr. Mike Pound's Computerphile video](https://youtu.be/hhUb5iknVJs) on the subject.

This is a simple python script that uses the haveibeenpwned API to determine if a password has been compromised. I make no claims to the validity of the data returned or accuracy of the system.

## Usage

    $ python pwned.py password
    SHA1: 5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8
    Password compromised 3645804 times.

**NOTE: You may need to surround your password with single quotes ('password') if it contains special characters that can be interpreted by the command line processor.**

## What is it doing?

The script will hash the password and send only the first 5 characters off to the API. The API returns a list of hashes that match and then locally the program will search through to find a match to your hash.

No passwords or full hashes are sent across the internet, so there is no concern for passwords becoming compromised by using this tool.
