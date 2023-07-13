#!/bin/python3

def caesarCipher(s, k):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    capital_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotated = ''
    if k >= 26:
        k = k % 26

    for i in range(len(s)):
        char = s[i]
        if char.isalpha():
            if char.isupper():
                char_index = capital_alpha.index(char)
                if char_index + k >= len(capital_alpha):
                    new_index = (char_index + k) - len(capital_alpha)
                    new_char = capital_alpha[0 + new_index]
                else:
                    new_char = capital_alpha[char_index + k]

            else:
                char_index = alphabet.index(char)
                if char_index + k >= len(alphabet):
                    new_index = (char_index + k) - len(alphabet)
                    new_char = alphabet[0 + new_index]
                else:
                    new_char = alphabet[char_index + k]

            rotated += new_char

        else:
            rotated += char

    return rotated


if __name__ == '__main__':

    n = int(input('Enter string length: ').strip())

    s = input('Enter the string: ')

    k = int(input('Enter the rotate size: ').strip())

    result = caesarCipher(s, k)

    print(result)
