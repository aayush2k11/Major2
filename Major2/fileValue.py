import random
fp=open("FileValue.txt","w")
for i in range(100000):
    s=""
    role=str(random.randint(1,20));
    extCrit=random.randint(1,500);
    access=random.randint(0,2000);
    s+="file"+str(i)+" "+role+" "+str(extCrit)+" "+str(access)+"\n"
    fp.write(s)
fp.close()
