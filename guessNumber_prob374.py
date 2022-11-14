"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1
"""
def guessNumber(n):
    minNum = 1
    maxNum = n       
    while minNum <= maxNum:
        midNum =  (minNum + maxNum) // 2
        result = guess(midNum)
        if result == 0:
            return midNum
        elif result == 1:
            minNum = midNum + 1
        else:
            maxNum = midNum

def guess(num):
    print(num)
    number = 6
    if num == number:
        return 0
    elif num > number:
        return 1
    else:
        return -1


print(guessNumber(10))

