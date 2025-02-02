try:
    from rich import print
except:
    pass
from math import log2
from heapq import *

text = open('transcript.txt', 'r').read()

"""
Calculate character counts and total characters
"""
total_chars = len(text)
char_counts = {}
for char in text:
    if char not in char_counts:
        char_counts[char] = 1
    else:
        char_counts[char] += 1

char_counts_lst = sorted(char_counts.items(), key=lambda x:-x[1])
print(f'{"=" * 10} Character counts {"=" * 10}')
print(f'{char_counts_lst}\n')
print(f'Total characters: {total_chars}')

"""
Calculate character frequency based on character counts and total characters
"""
char_freq = {}
for char, counts in char_counts_lst:
    char_freq[char] = counts / total_chars
char_freq_lst = sorted(char_freq.items(), key=lambda x:-x[1])
output_freq_lst = [(key, f'{value:.5f}') for key, value in char_freq_lst]
print(f'{"=" * 10} Character frequency {"=" * 10}')
print(f'{output_freq_lst}\n')

"""
Calculate entropy
"""
entropy = 0
for char, prob in char_freq_lst:
    entropy -= prob * log2(prob)
print(f'Entropy: {entropy}')

"""
Huffman Code
"""
child = [] # (left_child, right_child), leaf node if left_child == right_child
heap = [] # (prob, idx)
tbl = [] # char lookup table
for node, prob in char_freq.items():
    idx = len(child)
    child.append((idx, idx))
    heappush(heap, (prob, idx))
    tbl.append(node)

while heap is not None and len(heap) >= 2:
    left = heappop(heap)
    right = heappop(heap)
    heappush(heap, (left[0] + right[0], len(child)))
    child.append((left[1], right[1]))

## Build huffman code from tree
huff_code = {}
def build_huff_code(idx: int, code: str):
    if(child[idx] == (idx, idx)):
        # leaf node
        huff_code[tbl[idx]] = code
    else:
        build_huff_code(child[idx][0], code+'0')
        build_huff_code(child[idx][1], code+'1')
build_huff_code(len(child)-1, '')
output_huff_code = {key: value for key, value in sorted(huff_code.items(), key=lambda x:len(x[1]))}
print(f'{"=" * 10} Huffman code {"=" * 10}')
print(output_huff_code)


"""
Mean code length
"""
huff_code_lst = sorted(huff_code.items(), key=lambda x:x[0])
mean_code_length = 0
for char, code in huff_code_lst:
    mean_code_length += len(code) * char_freq[char]
print(f'Mean code length: {mean_code_length}')

"""
How it looks like if we're coding the original transcript with bunch of 8-bits 0/1?
"""
encode = {}
decode = {}
for char in char_counts:
    encode[char] = '{:08b}'.format(ord(char))
    decode['{:08b}'.format(ord(char))] = char
coded_text = ''
with open('original_binary_coded.txt', 'w+') as f:
    for char in text:
        f.write(encode[char])
        coded_text += encode[char]
"""
Sanity check: Check whether decoded is same as original code
"""
decoded = ''
with open('original_binary_coded.txt', 'r') as f:
    with open('original_decoded.txt', 'w+') as g:
        while True:
            chunk = f.read(8)
            if not chunk:
                break
            g.write(decode[chunk])
            decoded += decode[chunk]
assert decoded == text

"""
How it looks like if we apply huffman code?
"""
huff_bin_text = ''
with open('huffman_binary_coded.txt', 'w+') as f:
    for char in text:
        f.write(huff_code[char])
        huff_bin_text += huff_code[char]

"""
How it looks like if we code the binary code into characters?
"""
huff_text = ''
with open('huffman_text.txt', 'w', encoding="iso-8859-1") as f:
    with open('huffman_binary_coded.txt', 'r') as g:
        while True:
            chunk = g.read(8)
            if not chunk:
                break
            f.write(chr(int(chunk, 2)))
            huff_text += chr(int(chunk, 2))

"""
Compare file size
"""
def ratio(orig, new):
    return (orig - new) / orig * 100
import os
original_file_size = os.stat('transcript.txt').st_size
huffman_file_size = os.stat('huffman_text.txt').st_size
original_text_size = len(text)
huffman_text_size = len(huff_text)
print(f"Original text\t\tfile size {original_file_size}\t\t\tlength: {original_text_size}")
print(f"Huffman  text\t\tfile size {huffman_file_size} [green]({ratio(original_file_size, huffman_file_size):.2f}% ↓)[/green]\tlength: {huffman_text_size} [green]({ratio(original_text_size, huffman_text_size):.2f}% ↓)[/green]")

original_binary_file_size = os.stat('original_binary_coded.txt').st_size
huffman_binary_file_size = os.stat('huffman_binary_coded.txt').st_size
original_binary_size = len(coded_text)
huffman_binary_size = len(huff_bin_text)
print(f"Original binary code\tfile size {original_binary_file_size}\t\tlength: {original_binary_size}")
print(f"Huffman  binary code\tfile size {huffman_binary_file_size} [green]({ratio(original_binary_file_size, huffman_binary_file_size):.2f}% ↓)[/green]\tlength: {huffman_binary_size} [green]({(original_binary_size-huffman_binary_size)/original_binary_size*100:.2f}% ↓)[/green]")
