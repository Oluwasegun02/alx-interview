#!/usr/bin/python3
''' function that determines if all boxes can be opened
from a list of lists
'''

def canUnlockAll(boxes):
    ''' function that determines if all boxes can be unlocked
    And returns True or False
    '''
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Use a stack to perform DFS

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

# Example usage
# boxes = [[1], [2], [3], []]
# print(canUnlockAll(boxes))  # Output: True

# boxes = [[1, 2], [3], [4], []]
# print(canUnlockAll(boxes))  # Output: False
