#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python Worksheet


# In[ ]:


#1.(C)  
#2.(B) 
#3.(C)  
#4.(A)  
#5.(C)  
#6.(C)
#7.(A) 
#8.(C)  
#9.(A)  
#10.(A) 


# In[ ]:


Q11 to Q15 are programming questions.


# In[ ]:


#11.Write a python program to find the factorial of a number.


# In[17]:


num=int(input('Enter the Value'))
a=1
if a<1:
    print('The entered value is a negative value')
elif a==0:
    print('The entered value is Zero')
else:
    for i in range(1,num+1):
        a=a*i
    print('The Factorial of',num,'is',a)


# In[ ]:


#12. Write a python program to find whether a number is prime or composite.


# In[18]:


num = int(input("Please enter the number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break
else:
    print(num, "is not a prime number")


# In[ ]:


#13. Write a python program to check whether a given string is palindrome or not.


# In[14]:


string = input("Please enter your own String : ")
str1 = ""
for i in string:
    str1 = i + str1
print("String in reverse Order :  ", str1)
if(string == str1):
    print("This is a Palindrome String")
else:
    print("This is Not a Palindrome String")


# In[ ]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.


# In[13]:


from math import sqrt
a= float(input('Length of the first side '))
b= float(input('Length of the second side '))
c=sqrt(a**2 + b**2)
print ("The length of the third side of right-angled triangle = ",c)


# In[ ]:


#15.Write a python program to print the frequency of each of the characters present in a given string.


# In[19]:



a=input("Enter a string ")
print("String is ",a)
count={}
for i in a:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)


# In[ ]:




