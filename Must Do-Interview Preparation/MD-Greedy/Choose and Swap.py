'''
You are given a string s of lower case english alphabets. You can choose any two characters 
in the string and replace all the occurences of the first character with the second character 
and replace all the occurences of the second character with the first character. 
Your aim is to find the lexicographically smallest string that can be obtained 
by doing this operation at most once.

Example 1:

Input:
A = "ccad"
Output: "aacd"
Explanation:
In ccad, we choose ‘a’ and ‘c’ and after 
doing the replacement operation once we get, 
aacd and this is the lexicographically
smallest string possible. 
 

Example 2:

Input:
A = "abba"
Output: "abba"
Explanation:
In abba, we can get baab after doing the 
replacement operation once for ‘a’ and ‘b’ 
but that is not lexicographically smaller 
than abba. So, the answer is abba. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function 
chooseandswap() which takes the string A as input parameters and returns the 
lexicographically smallest string that is possible after doing the operation at most once.

Expected Time Complexity: O(|A|) length of the string A
Expected Auxiliary Space: O(1)

 

Constraints:
1<= |A| <=105
'''


class Solution:
    def chooseandswap (self, A):
        char_in_list = ''.join(set(A))
        print("Unique chars in a String: ", char_in_list)
        print("Enter first and second chars")
        chose_char = list(map(str, input().split()))
        lt = [y for y in A]
        first = chose_char[0]
        second = chose_char[1]
        print("You Choose '{}' as first char and '{}' as second char".format(first, second))
        for x in range(0, len(lt)):
            if lt[x] == first:
                lt[x] == second
            else:
                lt[x] == first
        return ''.join(lt)



if __name__ == '__main__': 
    ob = Solution()
    t = 1 #int (input ())
    for _ in range (t):
        A = "ccad" #input()
        print("String: ", A)
        ans = ob.chooseandswap(A)
        print(ans)