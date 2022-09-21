#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to check whether a number is Disarium
# or not
import math

# Method to check whether a number is disarium or not
def check(n) :

	# Count digits in n.
	count_digits = len(str(n))
	
	# Compute sum of terms like digit multiplied by
	# power of position
	sum = 0 # Initialize sum of terms
	x = n
	while (x!=0) :

		# Get the rightmost digit
		r = x % 10
		
		# Sum the digits by powering according to
		# the positions
		sum = (int) (sum + math.pow(r, count_digits))
		count_digits = count_digits - 1
		x = x//10
		
	# If sum is same as number, then number is
	if sum == n :
		return 1
	else :
		return 0
		
# Driver method
n = 135
if (check(n) == 1) :
	print ("Disarium Number")
else :
	print ("Not a Disarium Number")

# This code is contributed by Nikita Tiwari.


# In[2]:


def Length(n):    
    length = 0;    
    while(n != 0):                    # calculating the length of the number
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumDigit()  
def sumdigit(num):    
    rem = sum = 0;    
    len = Length(num);     # checking the number is disarium or not
        
    while(num > 0):    
        rem = num;   
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     

print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):           # printing disarium numbers
    result = sumdigit(i);    
        
    if(result == i):    
        print(i),   


# In[3]:


# method return true if n is Happy Number
# numSquareSum method is given in below detailed code snippet
def isHappyNumber(n):
	st=set()
	while (1):
		n = numSquareSum(n)
		if (n == 1):
			return True
		if n not in st:
			return False
		st.insert(n)


# In[4]:


# Python3 program to check a number
# is a Happy number or not

# Utility method to return
# sum of square of digit of n
def numSquareSum(n):
	squareSum = 0;
	while(n):
		squareSum += (n % 10) * (n % 10);
		n = int(n / 10);
	return squareSum;

# method return true if
# n is Happy number
def isHappynumber(n):

	# initialize slow
	# and fast by n
	slow = n;
	fast = n;
	while(True):
		
		# move slow number
		# by one iteration
		slow = numSquareSum(slow);

		# move fast number
		# by two iteration
		fast = numSquareSum(numSquareSum(fast));
		if(slow != fast):
			continue;
		else:
			break;

	# if both number meet at 1,
	# then return true
	return (slow == 1);

# Driver Code
n = 13;
if (isHappynumber(n)):
	print(n , "is a Happy number");
else:
	print(n , "is not a Happy number");

# This code is contributed by mits


# In[5]:


def check_happy_num(my_num):
   remaining = sum_val = 0
   while(my_num > 0):
      remaining = my_num%10
      sum_val = sum_val + (remaining*remaining)
      my_num = my_num//10
   return sum_val
print("The list of happy numbers between 1 and 100 are : ")
for i in range(1, 101):
   my_result = i
   while(my_result != 1 and my_result != 4):
      my_result = check_happy_num(my_result)
   if(my_result == 1):
      print(i)


# In[7]:


# Python program to check
# if a number is Harshad
# Number or not.

def checkHarshad( n ) :
	sum = 0
	temp = n
	while temp > 0 :
		sum = sum + temp % 10
		temp = temp // 10
	# Return true if sum of
	# digits is multiple of n
	return n % sum == 0

# Driver Code
if(checkHarshad(12)) : print("Yes")
else : print ("No")

if (checkHarshad(15)) : print("Yes")
else : print ("No")
	
# This code is contributed
# by Nikita Tiwari


# In[9]:


# Python program to check
# and print Pronic Numbers
# upto 200
import math

# function to check
# Pronic Number
def checkPronic (x) :

	i = 0
	while ( i <= (int)(math.sqrt(x)) ) :
		
		# Checking Pronic Number
		# by multiplying consecutive
		# numbers
		if ( x == i * (i + 1)) :
			return True
		i = i + 1

	return False

# Driver Code

# Printing Pronic
# Numbers upto 200
i = 0
while (i <= 200 ) :
	if checkPronic(i) :
		print(i,end=" ")
	i = i + 1

# This code is contributed
# by Nikita Tiwari.

