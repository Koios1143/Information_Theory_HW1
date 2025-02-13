# Information Theory Homework 1 - Huffman Code

This is the implementation of the first homework of 2024 Fall Semester Lecture, aiming to implement Huffman Code and try to check the Shanon's First Theorem (a.k.a Source Coding Theorem).

## Installation (Optional)

This step is optional. The only package required is for improved output formatting and color. If you'd like to install it, run:

```bash
pip install -r requirements.txt
```

## Project structure

- `main.py`
    Contains the whole code of this homework
- `transcript.txt`
    The example article to be test.

## Run the code

Simply run the following command, you can see the results, including `entropy`, `mean code length` and `file size improvement`

```bash
python main.py
```

After running the Python script, the code will generate four text files.

- `original_binary_coded.txt`
    The binary representation of original `transcript.txt`. (Note: We coded a single char with 8-bits)
- `original_decoded.txt`
    The decoded transcript based on `original_binary_coded.txt`, and it should be same as `transcript.txt`.
    You may check it manually with `diff` command (But actually we'll also check this in our code).
    ```bash
    diff original_decoded.txt transcript.txt
    ```
- `huffman_binary_coded.txt`
    The binary string version of huffman code
- `huffman_text.txt`
    Take every 8-bits of binary huffman with a character, to compare with original file intuitively.

## Results

For the given example transcript, we have the following results.

```
========== Character counts ==========
[(' ', 3035), ('e', 1714), ('a', 1103), ('t', 1097), ('o', 1028), ('n', 1018), ('i', 989), ('r', 916), ('s', 750), ('l', 701), 
('h', 519), ('d', 491), ('u', 432), ('c', 377), ('m', 338), ('p', 334), ('w', 309), ('y', 297), ('g', 283), ('f', 281), ('.', 
234), (',', 222), ('b', 193), ('\n', 180), ('v', 174), ('A', 126), ('k', 85), ('(', 57), (')', 57), ('T', 54), ('I', 49), ('W',
37), ('-', 27), ("'", 25), ('x', 23), ('S', 17), ('P', 16), ('C', 14), ('z', 14), ('M', 13), ('U', 11), ('j', 10), ('O', 10), 
('B', 9), ('F', 8), ('D', 8), ('N', 8), ('G', 8), ('0', 7), ('L', 6), ('E', 6), ('J', 5), ('q', 5), ('2', 5), ('V', 4), ('R', 
4), ('H', 4), (':', 4), ('K', 4), ('5', 2), ('1', 2), ('7', 2), ('8', 2), ('9', 1), ('3', 1), ('Y', 1)]

Total characters: 17766
========== Character frequency ==========
[(' ', '0.17083'), ('e', '0.09648'), ('a', '0.06208'), ('t', '0.06175'), ('o', '0.05786'), ('n', '0.05730'), ('i', '0.05567'), 
('r', '0.05156'), ('s', '0.04222'), ('l', '0.03946'), ('h', '0.02921'), ('d', '0.02764'), ('u', '0.02432'), ('c', '0.02122'), 
('m', '0.01903'), ('p', '0.01880'), ('w', '0.01739'), ('y', '0.01672'), ('g', '0.01593'), ('f', '0.01582'), ('.', '0.01317'), 
(',', '0.01250'), ('b', '0.01086'), ('\n', '0.01013'), ('v', '0.00979'), ('A', '0.00709'), ('k', '0.00478'), ('(', '0.00321'), 
(')', '0.00321'), ('T', '0.00304'), ('I', '0.00276'), ('W', '0.00208'), ('-', '0.00152'), ("'", '0.00141'), ('x', '0.00129'), 
('S', '0.00096'), ('P', '0.00090'), ('C', '0.00079'), ('z', '0.00079'), ('M', '0.00073'), ('U', '0.00062'), ('j', '0.00056'), 
('O', '0.00056'), ('B', '0.00051'), ('F', '0.00045'), ('D', '0.00045'), ('N', '0.00045'), ('G', '0.00045'), ('0', '0.00039'), 
('L', '0.00034'), ('E', '0.00034'), ('J', '0.00028'), ('q', '0.00028'), ('2', '0.00028'), ('V', '0.00023'), ('R', '0.00023'), 
('H', '0.00023'), (':', '0.00023'), ('K', '0.00023'), ('5', '0.00011'), ('1', '0.00011'), ('7', '0.00011'), ('8', '0.00011'), 
('9', '0.00006'), ('3', '0.00006'), ('Y', '0.00006')]

Entropy: 4.452240038286298
========== Huffman code ==========
{
    'e': '000',
    ' ': '111',
    'r': '0011',
    'i': '0101',
    'n': '0110',
    'o': '0111',
    't': '1001',
    'a': '1010',
    'u': '00101',
    'd': '01001',
    'h': '10000',
    'l': '11001',
    's': '11011',
    'b': '001000',
    ',': '010000',
    '.': '010001',
    'f': '100011',
    'g': '101100',
    'y': '101101',
    'w': '101111',
    'p': '110000',
    'm': '110001',
    'c': '110101',
    'A': '1000101',
    'v': '1101000',
    '\n': '1101001',
    'I': '00100100',
    'T': '00100110',
    '(': '10001000',
    ')': '10001001',
    'k': '10111011',
    "'": '001001010',
    '-': '001001110',
    'W': '101110011',
    'M': '0010010111',
    'C': '0010011110',
    'z': '0010011111',
    'P': '1011100001',
    'S': '1011100101',
    'x': '1011101011',
    'E': '00100101100',
    '0': '10111000000',
    'F': '10111000001',
    'D': '10111000100',
    'N': '10111000101',
    'G': '10111000110',
    'B': '10111010000',
    'j': '10111010001',
    'O': '10111010010',
    'U': '10111010100',
    'V': '001001011011',
    'R': '101110001110',
    'H': '101110001111',
    ':': '101110010000',
    'K': '101110010001',
    'J': '101110100110',
    'q': '101110100111',
    '2': '101110101010',
    'L': '101110101011',
    'Y': '0010010110100',
    '5': '0010010110101',
    '1': '1011100100100',
    '7': '1011100100101',
    '8': '1011100100110',
    '9': '10111001001110',
    '3': '10111001001111'
}
Mean code length: 4.482888663739727
Original text           file size 17766                 length: 17766
Huffman  text           file size 9956 (43.96% ↓)       length: 9956 (43.96% ↓)
Original binary code    file size 142128                length: 142128
Huffman  binary code    file size 79643 (43.96% ↓)      length: 79643 (43.96% ↓)
```

According to the Shannon's First Theorem, the following equation should be establish.

$$
H(X) \leq \frac{\bar{L}}{n} < H(X) + \epsilon
$$

Where

- $H(X) = 4.452240038286298$
- $\bar{L} = 4.482888663739727$
- $n = 1$
- $\epsilon = 1$

$$
4.45224 \leq 4.48288 < 5.45224 \quad \blacksquare
$$

Also by the result we can see a $43.96\%$ compress rate.

# Problem 2

Ploblem 2 is about Shannon's Second Theorem (Noisy-channel coding theorem).

To see the result, simply run the following command

```bash
python problem2.py
```
