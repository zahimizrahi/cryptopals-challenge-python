
import binascii
import base64

""""
command-line:
python set1.ch6.py


---------  BREAK REPEATING KEY XOR -------------
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.

"""


# code from ch3
def xor(b1, b2):
  b = bytearray(len(b1))
  k = len(b1)
  for i in range(len(b1)):
    b[i] = b1[i] ^ b2[i]
  return b

def score(s):
    freq = {}
    freq[' '] = 700000000
    freq['e'] = 390395169
    freq['t'] = 282039486
    freq['a'] = 248362256
    freq['o'] = 235661502
    freq['i'] = 214822972
    freq['n'] = 214319386
    freq['s'] = 196844692
    freq['h'] = 193607737
    freq['r'] = 184990759
    freq['d'] = 134044565
    freq['l'] = 125951672
    freq['u'] = 88219598
    freq['c'] = 79962026
    freq['m'] = 79502870
    freq['f'] = 72967175
    freq['w'] = 69069021
    freq['g'] = 61549736
    freq['y'] = 59010696
    freq['p'] = 55746578
    freq['b'] = 47673928
    freq['v'] = 30476191
    freq['k'] = 22969448
    freq['x'] = 5574077
    freq['j'] = 4507165
    freq['q'] = 3649838
    freq['z'] = 2456495
    score = 0
    for c in s.lower():
        if c in freq:
            score += freq[c]
    return score

def break_single_key_xor(b1):
    max_score = None
    english_plaintext = None
    key = None

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = xor(b1,b2)
        pscore = score(plaintext)

        if not max_score or pscore > max_score:
            max_score = pscore
            english_plaintext = plaintext
            key = chr(i)
    return key, english_plaintext


#n  ew code

#x1 and x2 are bytearray
def calcHammingDistance (x1, x2):
    return (sum(bin(x1[i]^x2[i]).count('1') for i in range(len(x1))))

# for test
# b1 = bytearray(b"this is a test")
# b2 = bytearray(b"wokka wokka!!!")

# print (calcHammingDistance(b1, b2))


cipher = bytearray( base64.b64decode("".join(list(open("ch6_file.txt", "r"))).encode('utf-8')))
normalized_distances = []
blocks = []

for KEYSIZE in range(2,40):
    blocks = [ cipher[i: i+KEYSIZE] for i in range(0, len(cipher), KEYSIZE)][0:4]
    normalized_distance = float (
        calcHammingDistance(blocks[0], blocks[1]) + calcHammingDistance(blocks[1], blocks[2]) + \
                            calcHammingDistance(blocks[2], blocks[3])) / (KEYSIZE * 3)
    normalized_distances.append ( [KEYSIZE, normalized_distance])


normalized_distances = sorted(normalized_distances, key=lambda d: d[1])

for distance in normalized_distances[:4]:
    block_bytes = [[] for i in range(distance[0]) ]
    for i, byte in enumerate(cipher):
        block_bytes [ i % distance[0]].append(byte)

    keys = ""
    for bytes in block_bytes:
        keys += break_single_key_xor(bytes)[0]

    key = bytearray (keys * len(cipher), 'utf-8')
    plaintext_ba = xor(cipher,key)
    plaintext = bytes(plaintext_ba)

    print (keys)
    print (KEYSIZE)
    print (plaintext)



