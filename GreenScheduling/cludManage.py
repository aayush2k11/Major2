import random

#function for sorting
def compare(a,b):
    return a[2]-b[2]

def mySort(task):
    for i in range(len(task)):
        for j in range(i+1,len(task)):
            if task[i][2]>task[j][2]:
                temp=task[i]
                task[i]=task[j]
                task[j]=temp
    return task

#set of number of systems
sysSet=[10,20,30,40,50]

#set of number of tasks
for n in sysSet:
    print("Number of Systems: "+str(n))
    for numTask in range(1,501):
        systems=[]
        #for marking system as occupied or unoccupied
        occupied=[]
        for i in range(n):
            occupied.append(0)

        #property of each system
        for i in range(n):
            idle=random.randint(68,72)  	#idle temperature of system
            current=idle			#status of the system
            critical = random.randint(77,82)    #critical temperature of system
            cool = random.uniform(0.06, 0.3)    #cooling rate of system
            systems.append([idle,current,critical,cool])
        
        #property of each task
        task=[]
        for i in range(numTask):
            incRate = random.uniform(0.06,0.55) #temperature increase rate per second
            runtime = random.randint(5, 10)     #run time of each process
            arrival = random.randint(1,15)      #arrival time of each process
            task.append([incRate, runtime, arrival,0])
        task = mySort(task)
        
        #first fit starts here
        queue=[]
        for i in range(numTask):
            queue.append(task[i])
            
        #busy for keeping the count of systems which are busy
        busy=[]
        for i in range(n):
            busy.append(0)
        
        #setting load factor for first fit as 0
        load1=0.0
        time=0
        counter=0
        taskComplete=0
        countProc=0
        ffCounter=0
        while len(queue)!=0 and counter<1000:
            for j in range(n):
                if occupied[j]!=0 and busy[j]>0:
                    busy[j]=busy[j]-1
                    if busy[j]==0:
                        occupied[j]=0
                else:
		    #cooling the temperature of system if greater than idle
                    if systems[j][1]>systems[j][0]:
                        systems[j][1]-=systems[j][3]
                    if systems[j][1]<systems[j][0]:
                        systems[j][1]=systems[j][0]
                
                    
            for j in range(len(queue)):
                if queue[j][2]<=counter and queue[j][3]==0:
		    #finding the first idle system
                    for k in range(n):
                        if occupied[k]==0:
                            initial=systems[k][1]
                            final=initial+task[j][1]*task[j][0]
                            if final<=systems[k][2]:
                                queue[j][3]=1
                                occupied[k]=j+1
                                busy[k]=queue[j][1]
                                systems[k][1]=final
                                load1=load1+float(final-systems[k][0])/float(systems[k][2]-systems[k][0])
                                countProc+=1
                                if countProc==numTask:
                                    ffCounter=counter
                                    break
                                break
                
            counter=counter+1

        #best fit starts here
        for i in range(numTask):
            queue[i][3]=0

        for i in range(n):
            occupied[i]=0
            systems[i][1]=systems[i][0]
        busy=[]
        for i in range(n):
            busy.append(0)
        counter=0
        taskComplete=0
        load2=0.0
        countProc=0
        bfCounter=0
        while len(queue)!=0 and counter<1000:
            for j in range(n):
                if occupied[j]!=0 and busy[j]>0:
                    busy[j]=busy[j]-1
                    if busy[j]==0:
                        occupied[j]=0
                else:
		    #cooling down system if temperature greater than idle
                    if systems[j][1]>systems[j][0]:
                        systems[j][1]-=systems[j][3]
                    if systems[j][1]<systems[j][0]:
                        systems[j][1]=systems[j][0]
                
                    
            for j in range(len(queue)):
                if queue[j][2]<=counter and queue[j][3]==0:
                    minload=[]
                    for k in range(n):
                        minload.append(-1)
                    #evaluating load factor for each idle system
                    for k in range(n):                        
                        if occupied[k]==0:
                            initial=systems[k][1]
                            final=initial+task[j][1]*task[j][0]
                            if final<=systems[k][2]:
                                minload[k]=float(final-systems[k][0])/float(systems[k][2]-systems[k][0])
                    minl=-1
                    for k in range(n):
                        if minload[k]!=-1:
                            minl=minload[k]
                            ind=k
                            break
                    flag=0
		    #assigning task to system with minimum load factor increase
                    if minl!=-1:
                        for k in range(n):
                            if minload[k]>=0 and minload[k]<minl:
                                minl=minload[k]
                                ind=k
                        final=systems[ind][1]+(queue[j][1]*queue[j][0])
                        queue[j][3]=1
                        occupied[ind]=j+1
                        busy[ind]=queue[j][1]
                        systems[ind][1]=final
                        countProc+=1
                        load2+=minl    
                        if countProc==numTask:
                            bfCounter=counter
                            break
            counter=counter+1

        print(str(float(numTask)/float(n))+"\t"+str(load1)+"\t"+str(load2)+"\t"+str(bfCounter)+"\t"+str(ffCounter))
        
    
    




