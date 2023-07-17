dict1={'a':1,'b':2}
dict2={'c':2,'d':1}
dict_new=(dict1.update(dict2))
print(dict1)

lis=[1,2,3,5,8,3,2]
print(set(lis))
# o/p=[1,5,8]
out=[]
i=0
while i<len(lis):
    if lis[i] not in out:
        out.append(lis[i])
    i+=1
print(out)


def isprime(num):
        for n in range(2, num):
            if num%n == 0:
                return False
        return True

out=[]
for num in range(10,100):
    if isprime(num):
        out.append(num)
print(out)
new_out=[]
for item in out:
    for digit in str(item):
        if not isprime(int(digit)):
            break
    else:
        new_out.append(item)
print(new_out)



