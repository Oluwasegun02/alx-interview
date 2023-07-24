validUTF8 Function

The `validUTF8` function is a Python method that determines if a given data set represents a valid UTF-8 encoding.

Function Signature
def validUTF8(data: List[int]) -> bool:
    ...
Parameters
`data` (List[int]): A list of integers representing bytes in the data set. Each integer represents 1 byte of data, containing 8 least significant bits of the byte.
Return Value
`bool`: Returns `True` if the `data` set is a valid UTF-8 encoding, otherwise returns `False`.
Function Description

A character in UTF-8 can be 1 to 4 bytes long. The function `validUTF8` checks if the `data` set follows the rules of UTF-8 encoding.

The function iterates through each byte in the `data` set and verifies if the bytes correspond to the correct number of bytes for a character and if they follow the UTF-8 format. Specifically, it checks the following:

If the first byte of a character starts with the correct number of leading 1s corresponding to the total number of bytes in the character.
If continuation bytes start with "10".
If the `data` set follows the UTF-8 format correctly, the function returns `True`. If any of the bytes do not adhere to the UTF-8 format, the function returns `False`.

Example -> `main.py`

Note: This function only checks for the validity of the UTF-8 encoding based on the given `data` set's byte representation and does not decode the characters to their actual Unicode code points.
