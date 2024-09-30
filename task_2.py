from collections import deque

def is_palindrome(row: str) -> bool:
    d = deque()
    for char in row:
        d.append(char.lower())

    while len(d) > 0:
        right = d.pop()
        if len(d)  == 0:
            return True

        left = d.popleft()

        if right != left:
            return False

    return True


