'''
A thief wants to loot houses. He knows the amount of money in each house. 
He cannot loot two consecutive houses. Find the maximum amount of money he can loot.

Input format :
    The first line of input contains an integer value of 'n'. It is the total number of houses.
    The second line of input contains 'n' integer values separated by a single space denoting 
    the amount of money each house has.
Output format :
    Print the the maximum money that can be looted.
Constraints :
    0 <= n <= 10 ^ 4

Time Limit: 1 sec
Sample Input :
    6
    5 5 10 100 10 5
Sample Output :
    110
'''
# Method 1
def thief_loot(money_list):
    secondary_list = []
    largest = None
    for num in money_list:
        if largest is None or num > largest:
            largest = num
    money_list.remove(largest)
    secondary_list = money_list
    return largest, secondary_list



if __name__ == '__main__':
    houses = int(input("\nNumber of House: "))
    money_in_houses = input("Enter the money in {} houses: ".format(houses))
    money_in_houses = money_in_houses.split(' ')
    money_list = []
    for x in money_in_houses:
        if x == ' ':
            continue
        money_list.append(int(x))
    print("MyList", money_list)
    r1, r2 = thief_loot(money_list)
    r3, r4 = thief_loot(r2)
    print("\nMax Money Thief can Loot: {}\n".format(r1+r3))


# Method 2
def max_loot_money(n,inp):
    if n==0:
        return 0
    if n==1:
        return inp[0]
        
    arr = [0]*n
    arr[0]=inp[0]
    arr[1]=max(inp[1],inp[0])
    
    for i in range(2,n):
        arr[i] = max(arr[i-1],inp[i]+arr[i-2])
    
    return arr[n-1]




n = int(input())
if n==0:
    print("0")
    exit()
inp = list(map(int,input().split()))
maxLoot = max_loot_money(n,inp)
print(maxLoot)