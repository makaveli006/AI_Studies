#Python program to print even length words in a string
#split each word, find length of each split, if its even print it
s =input("Enter a complete sentence : ")
words = s.split()
for w in words:
    if (len(w)%2 == 0):
        print(w, end=" ")
        


#Python program to interchange first and last elements in a list
# 0 - first element, -1 - last element, Using temperary variable
ls = [12, 35, 9, 56, 24]
print("Given List:",ls)
a = ls[0]
ls[0] = ls[-1]
ls[-1] = a
print("Output :",ls)


#Python program to sort dictionary by key or value

d = {'mango': 60, 'apple':70, 'Banana':65, 'Orange': 44, 'cocunut': 18}
print("Input :",d)
s = sorted(d.items())
sort = dict(s)
print("Output :",sort)

#Python program to find the power of a number using recursion

def power(n, p):
    if p == 0:
        return 1
    else:
        return n * power(n, p - 1)
n=int(input("Enter Number :"))
p=int(input("Enter power : "))

result = power(n,p)

print("Input : N=",n,", P=",p)
print("Output :",result)


#Implement a Lambda function to check if a value is in a list
ls = [1,2,3,4,5]
number = 4
f = lambda x: print("Element is Present in the list") if x in ls else print("Not Present")
f(number)


#Implement a Lambda function to find the smaller value between two elements
num = input("Input two numbers :").split()
a,b = map(int,num)
check = lambda x,y: x if x<y else y
smaller = check(a,b)
print("Output :",smaller)


#Change case of all characters in a .txt file using python
f = open("sample.txt","r+")
a= f.read()
print("before swap " ,a)
f.close()

swap = a.swapcase()

f = open("sample.txt","w+")
f.write(swap) #after write, curser will be at the end of content , seek user to move to start of the content
f.seek(0)
print("after swap " ,f.read())
f.close()


#Find the average of an unknown number of inputs in python
num = input("Enter Numbers :").split()
l1 = list(map(int,num))
avg = sum(l1) / len(l1)
print("Output :",avg)


#Python program to display half diamond pattern of numbers with star border
def display(n):
    print("Output :") 
    print("*")
    for i in range(1, n+1):
        print("*", end="")
        for j in range(1, i+1): 
            print(j, end="")
 
        for k in range(i-1, 0, -1): 
            print(k, end="")
 
        print("*", end="")
        print()

    for i in range(n-1, 0, -1):
        print("*", end="")
        for j in range(1, i+1):
            print(j, end="")
 
        for k in range(i-1, 0, -1):
            print(k, end="")
 
        print("*", end="")
        print()
 
    print("*")
n = 5
display(n)

#Pair elements with rear element in Matrix row in Python
def pair(ls):
    pairedlist=[]
    for row in ls:
        for i in range(len(ls)-1):
            plist=[row[i],row[-1]]
            pairedlist.append(plist)
    return pairedlist
     

ls=[[4,5,6],[2,4,5],[6,7,5]]
print("The original list is :")
print(ls)
p=pair(ls)
print("The list after pairing is :",p)   