# Cryptography with Caesar (Shift) Cypher

## PR for this file: https://github.com/kimmyd70/caesar-cypher/pull/1

This is Lab 18 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 6 February 2021
____________________
### Features

1. Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
    - the phrase will then be shifted that many letters
    - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

    - shifts that exceed 26 should wrap around
    - E.g. encrypt(‘abc’,27) would return ‘bcd’

    - shifts that push a letter out or range should wrap around
    - E.g. encrypt(‘zzz’,1) would return ‘aaa’

2. Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

3. Create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

4. Devise a method for the computer to determine if code was broken with minimal human guidance.
__________

## Approach

Approach is using +/- shift keys and letter replacement.  Must have access to word library such as natural language tool kit (nltk)

_____________
## Required User Acceptance Testing

1. encrypt a string with a given shift
2. decrypt a previously encrypted string with the same shift
3. encryption should handle upper and lower case letters (return w/case match)
4. encryption should allow non-alpha characters but ignore them, including white space (return without giving away punctuation...ignore)
5. decrypt encrypted version of "It was the best of times, it was the worst of times." WITHOUT knowing the shift used.




_________________


