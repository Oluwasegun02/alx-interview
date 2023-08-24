### (0x08. Making Change)
=========================

## Change comes from within

This project focuses on solving the "Making Change" problem using Python. The problem involves determining the fewest number of coins needed to meet a given amount total, considering a pile of coins with different values.

## Requirements
- Editors: `vi`, `vim`, `emacs`
- Execution Environment: `Ubuntu 14.04` LTS with `Python 3.4.3`
- File Endings: All files should end with a new line
- Shebang: The first line of all files should be `#!/usr/bin/python3`
- README: A `README.md` file is mandatory at the root of the project folder
- Coding Style: Code should follow the `PEP 8` style (version 1.7.x)
- Executable Files: All files must be executable
## Tasks
- 0. Change comes from within
Given a pile of coins of different values, the task is to determine the fewest number of coins needed to meet a given total amount.

Prototype: def makeChange(coins, total)
Return: Fewest number of coins needed to meet the total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of coin values
The value of a coin will always be an integer greater than 0
It can be assumed that you have an infinite number of each denomination of coin in the list
# Example
python
Copy code
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
# Usage
To test the functionality of the makeChange function, you can use the provided 0-main.py script.

