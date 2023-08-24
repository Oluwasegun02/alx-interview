#!/usr/bin/python3
''' function that determines if all boxes can be opened
from a list of lists
'''

def canUnlockAll(boxes):
    ''' function that determines if all boxes can be unlocked
    And returns True or False
    '''
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True 
    stack = [0]  

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
