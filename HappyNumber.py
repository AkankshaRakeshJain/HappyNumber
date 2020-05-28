'''Happy Number
19-->1^2 + 9^2 -->1+81=82--> 8^2 + 2^2 -->64+4 =68 -->6^2 + 8^2=100 -->1^2 + 0^2 + 0^2 = 1--> 19 is a happy number'''

# <---------------------------- Method 1 ---------------------------->
def happyNumber(num):
    sum,temp = 0,0
    while num>0:
        temp = num%10
        sum += temp **2
        num = num // 10
    return sum

num = int(input('Enter a number: '))
result = num

while(result !=1 and result!=4):
    result = happyNumber(result)

if result ==1:
    print(num, 'is a happy number')
elif result == 4:
    print(num, 'is not a happy number')


# <---------------------------- Method 2 using list ---------------------------->
def happyNumber(num):
    temp = num
    if temp != 4 and temp !=1:
        lst = []
        for i in str(temp):
            lst.append(int(i))

        lst = [number ** 2 for number in lst]
        s = sum(lst)

            happyNumber(s)
            if s == 1:
                print(num, 'is a happy number')
            elif s == 4:
                print(num, 'is not a happy number')
    

happyNumber(int(input()))


    
