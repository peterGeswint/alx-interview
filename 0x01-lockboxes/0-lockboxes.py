#!/usr/bin/python3

def canUnlockAll(boxes):
    # Start by marking the first box (index 0) as unlocked
    unlocked = {0}

    # Use a stack to manage the keys we have (initially, keys from box 0)
    keys = list(boxes[0])

    # Process the keys while we still have some in the stack
    while keys:
        key = keys.pop()
        # Unlock the corresponding box if it's not already unlocked
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            # Add all the keys from the newly unlocked box
            keys.extend(boxes[key])

    # If we unlocked all the boxes, return True, otherwise False
    return len(unlocked) == len(boxes)
