import binascii
import base64

""""

command-line:
python set1.ch1.py  

Convert hex to base64
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
"""

def hex_to_base64(str):
    return base64.b64encode(binascii.a2b_hex(str)).decode('ascii')


s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
res = hex_to_base64(s)
if res == expected_output:
    print("Correct")
else:
    print("Wrong!" + "\n" + expected_output + " != " + res)
