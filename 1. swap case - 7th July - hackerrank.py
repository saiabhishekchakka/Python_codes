# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# link - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

# solution: 

def swap_case(s):
    snew = s.swapcase()
    return snew
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)