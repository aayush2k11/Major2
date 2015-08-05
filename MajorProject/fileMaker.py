import random
for i in range(100):
    fp=open("file"+str(i)+".txt","w")
    s1=""
    for j in range(500000):
        s1+=str(random.randint(0,500))+" "
    fp.write(s1)
    fp.close()
            
