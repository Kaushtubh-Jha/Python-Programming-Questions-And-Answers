'''
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9


Test cases:
4 - 1 - 3 - 6     : invalid move
4 - 1 - 9 - 2      : invalid move
2 - 4 - 1 - 3 - 6  : valid move
'''
# Ref: https://medium.com/@rebeccahezhang/leetcode-351-android-unlock-patterns-d9bae4a8a958

# Thanks medium.com for the answer
def validPattern():
    sample_data = [1,2,3,
                   4,5,6,
                   7,8,9]



if __name__ == '__main__':
    inp = int(input())
    print(inp)