name=input()
collegeid= input()
branch=input()
percentage=float(input())
dob=input()

# print(name+' '+collegeid+' '+branch+' '+percentage+' '+dob)

print('My Name is',name,'and collegeid is',collegeid)
print('branch in my b.tech is',branch,'with an aggregrate of',percentage,'%')
print('my date of birth is',dob)

print('My Name is %s and collegeid is %s' %(name,collegeid))
print('branch in my b.tech is %s with an aggregrate of %.2f' %(branch,percentage))
print('my date of birth is%s'%(dob))

print(f'My Name is {name} and collegeid is {collegeid}')
print(f'branch in my b.tech is {branch} with an aggregrate of {percentage}')
print(f'my date of birth is {dob}')

'''ANSWERS'''
'''kvr
15f01a0111
mechanical
64.86
18/12/1995
My Name is kvr and collegeid is 15f01a0111
branch in my b.tech is mechanical with an aggregrate of 64.86 %
my date of birth is 18/12/1995

My Name is kvr and collegeid is 15f01a0111
branch in my b.tech is mechanical with an aggregrate of 64.86
my date of birth is18/12/1995

My Name is kvr and collegeid is 15f01a0111
branch in my b.tech is mechanical with an aggregrate of 64.86
my date of birth is 18/12/1995'''