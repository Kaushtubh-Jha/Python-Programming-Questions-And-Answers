'''
Given a fraction. Convert it into a decimal. 
If the fractional part is repeating, enclose the repeating part in parentheses.
 

Example 1:

Input: numerator = 1, denominator = 3
Output: "0.(3)"
Explanation: 1/3 = 0.3333... So here 3 is 
recurring.
Example 2:

Input: numerator = 5, denominator = 2
Output: "2.5"
Explanation: 5/2 = 2.5
 

Your Task:
You don't need to read or print anyhting. Your task is to complete the function fractionToDecimal() 
which takes numerator and denominator as input parameter and returns its decimal form in string format.

Note: In case, the numerator is divisible by the denominator, just print the integer value.
 

Expected Time Compelxity: O(k) where k is constant.
Expected Space Complexity: O(k)
 

Constraints:
1 ≤ numerator, denominator ≤ 2000
'''




'''class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if(numerator%denominator!=0):
            res = int(numerator/denominator)
            s = ""
            s+=str(res)
            s+="."
            rem = numerator%denominator
            mp = {}
            while(rem!=0 and rem not in mp):
                mp[rem] = len(s)
                rem = rem * 10
                res_part = rem // denominator
                s += str(res_part)
                rem = rem % denominator
                if (rem == 0):
                    return s
                else:
                    return(s[:mp[rem]]+"("+s[mp[rem]:]+")")
        else:
            return int(numerator/denominator)'''

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        return numerator/denominator


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
