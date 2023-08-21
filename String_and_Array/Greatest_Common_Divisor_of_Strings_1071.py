'''
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

'''




def gcdOfStrings(str1: str, str2: str) -> str:

        def isDivisor(l):
            if len(str1) % l or len(str1) % l :
                return False
            
            f1, f2 = len(str1) // l, len(str2) // l
            s = str1[:l]

            if s*f1 == str1 and s*f2 == str2 :
                return True

            return False 

        for i in range(min(len(str1), len(str2)), 0, -1):

            if isDivisor(i):
                return str1[:i]

        return ""

print(gcdOfStrings("ababab", "abab"))
