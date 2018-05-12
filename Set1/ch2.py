import sys
import binascii

""""

command-line:
python set1.ch2.py  in1 in2 expected output

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
"""

def sxor(s1,s2):
    i1 = int(s1, 16)
    i2 = int(s2, 16)
    return hex(i1^i2)


in1 = sys.argv[1]
in2 = sys.argv[2]
expected_output = sys.argv[3]
expected = hex(int(expected_output, 16))
res = sxor(in1,in2)
if res == expected:
    print("Correct")
else:
    print("Wrong!" + "\n" + str(expected) + " != " + str(res))
