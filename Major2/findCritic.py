import math
def intConversion(a):
    return int(a)

fp=open("FileValue.txt","r")
fp2=open("output3.txt","w")
fp3=open("relations2.txt","r")
fp4=open("keys.txt","w")
fp5=open("vals.txt","w")
numRole=int(input("Enter number of roles"))
relations=[]

for line in fp3.readlines():
    l=list(map(intConversion,line.strip().split()))
    relations.append(l)
    
roleVal=[]
for i in range(numRole):
    val=int(input())
    roleVal.append(val)

out=[]
for line in fp.readlines():
    l=line.strip().split()
    r=int(l[1])
    eC=int(l[2])
    roleSum=0
    for i in range(len(relations[r-1])):
        if relations[r-1][i]==-1 or relations[r-1][i]==2:
            roleSum+=roleVal[i]
    Critic=float(eC)/float(roleSum)
    out.append(round(Critic,4))

out.sort()
num=len(out)

valI={}
for n in out:
    if n not in valI.keys():
        valI[n]=1
    else:
        valI[n]+=1
valCopy=valI.copy()

keyArr=[]
for k in valI.keys():
    keyArr.append(k)
keyArr.sort()

for k in valI.keys():
    valI[k]=valI[k]/float(num)

valI[keyArr[0]]=valI[keyArr[0]]
for i in range(1,len(keyArr)):
    valI[keyArr[i]]=valI[keyArr[i]]+valI[keyArr[i-1]]
    #print(keyArr[i],": ",valI[keyArr[i]]," :: ",keyArr[i-1],": ",valI[keyArr[i-1]])


for k in valI.keys():
    valI[k]=round(5*valI[k],3)

a=[]
for k in valI.keys():    
    for n in range(valCopy[k]):
        a.append(valI[k])
    x=str(valI[k])+", "
    y=str(valCopy[k])+", "
    fp4.write(x)
    fp5.write(y)
    
fp2.write(str(out))
fp2.close()
fp.close()
fp3.close()
fp4.close()
fp5.close()
    
    
