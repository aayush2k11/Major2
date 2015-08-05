import os
import shutil
from nameNode import *
"""
It is assumed that the role hierarchy of the organization
has been provided and weight associated to each role has
also been mentioned.

The code will take following inputs from user:
1. File to be stored in cloud
2. The external criticality of the file
3. The lowest member in hierarchy having access to file

The code will give the following output:
1. 5 directories will be made and a file will be assigned to
   its respective driectory after finding the storage criticality
   of the file by following the algorithm proposed.
"""

def intConversion(a):
    return int(a);

L1=20;
L2=40;
L3=60;
L4=80;
L5=100;

bufferCount=0;
bufferThresh=5000;

masterNode = namenode(1000,1000);
#Reading role hierarachy of the the organization
fp=open('relations2.txt','r');
fp1=open('FileValue.txt','r');
numRoles=int(input("\nEnter number of roles: "));
relations=[]
fp1_status=1;
for line in fp.readlines():
    l=list(map(intConversion, line.strip().split()));
    relations.append(l);


print("\nEnter weight of each role:\n");
roleVal=[];
for i in range(numRoles):
    val=int(input('Role '+str(i+1)+': '));
    roleVal.append(val);

files=[]

def findCriticality(roleVal, relations):
    global fp1_status;
    global fp1,files;
    if fp1_status==0:
        fp1=open('FileValue.txt','r');
        fp1_status=1;
    fileDetails=[]
    max_access_val=0;
    for file in masterNode.db1.keys():
        if masterNode.db1[file][0][-1]>max_access_val:
            max_access_val=masterNode.db1[file][0][-1];
    for file in masterNode.db2.keys():
        if masterNode.db2[file][0][-1]>max_access_val:
            max_access_val=masterNode.db2[file][0][-1];
    for file in masterNode.db3.keys():
        if masterNode.db3[file][0][-1]>max_access_val:
            max_access_val=masterNode.db3[file][0][-1];
    for file in masterNode.db4.keys():
        if masterNode.db4[file][0][-1]>max_access_val:
            max_access_val=masterNode.db4[file][0][-1];
    for file in masterNode.db5.keys():
        if masterNode.db5[file][0][-1]>max_access_val:
            max_access_val=masterNode.db5[file][0][-1];
    out=[]
    file_critics={}
    
    for line in  files:
        fileName = line[0];
        role=int(line[1]);
        externalCritic = int(line[2]);
        roleSum=0;
        access_val=int(line[3]);
        for i in range(len(relations[role-1])):
            if relations[role-1][i]==-1 or relations[role-1][i]==2:
                roleSum+=roleVal[i];
        Critic = float(externalCritic)/float(roleSum)+float(access_val)/float(max_access_val);
        file_critics[fileName]=round(Critic,4);
        out.append(round(Critic,4));
    out.sort();
    num=len(out);
    critic_count={}
    for n in out:
        if n not in critic_count.keys():
            critic_count[n]=1;
        else:
            critic_count[n]+=1;
    critic_copy=critic_count;
    
    #Array to store the keys
    key_arr=[]
    for k in critic_count.keys():
        key_arr.append(k);
    key_arr.sort();

    for k in critic_count.keys():
        critic_count[k]=critic_count[k]/float(num);
        
    critic_count[key_arr[0]]=critic_count[key_arr[0]];
    for i in range(1,len(key_arr)):
        critic_count[key_arr[i]]=critic_count[key_arr[i]]+critic_count[key_arr[i-1]];
        
    for k in critic_count.keys():
        critic_count[k]=round(critic_count[k]*5,3);

    for file in file_critics.keys():
        critic=file_critics[file];
        file_critics[file]=critic_count[critic];
    fp1.close();
    fp1_status=0;
    return file_critics;

#print("Enter file name (with absolute address), external criticality, role number");
#userInput=input();
if fp1_status==0:
    fp1=open('FileValue.txt','r');
    fp1_status=1;
for line in fp1.readlines():
    l=line.strip().split();
    files.append(l);
    fileName = l[0];
    role=int(l[1]);
    external_critic=int(l[2]);
    num_access=int(l[3]);
    temp_server= int(external_critic/100)%5;
    masterNode.add_file(fileName, temp_server,external_critic,3,num_access);
    if bufferCount <bufferThresh:
        bufferCount+=1
    else:
        bufferCount=0;
        file_critic = findCriticality(roleVal, relations);
        masterNode.updateCriticalities(file_critic);
    if len(files)%10000==0:
        print(str(len(files))+" files done!!!\n");

"""Evalluating counts"""
c1=0;
c2=0;
c3=0;
c4=0;
c5=0;
for file in masterNode.db1.keys():
    if masterNode.db1[file][0][0]==0:
        c1+=1;
    elif masterNode.db1[file][0][0]==1:
        c2+=1;
    elif masterNode.db1[file][0][0]==2:
        c3+=1;
    elif masterNode.db1[file][0][0]==3:
        c4+=1;
    elif masterNode.db1[file][0][0]==4:
        c5+=1;

for file in masterNode.db2.keys():
    if masterNode.db2[file][0][0]==0:
        c1+=1;
    elif masterNode.db2[file][0][0]==1:
        c2+=1;
    elif masterNode.db2[file][0][0]==2:
        c3+=1;
    elif masterNode.db2[file][0][0]==3:
        c4+=1;
    elif masterNode.db2[file][0][0]==4:
        c5+=1;

for file in masterNode.db3.keys():
    if masterNode.db3[file][0][0]==0:
        c1+=1;
    elif masterNode.db3[file][0][0]==1:
        c2+=1;
    elif masterNode.db3[file][0][0]==2:
        c3+=1;
    elif masterNode.db3[file][0][0]==3:
        c4+=1;
    elif masterNode.db3[file][0][0]==4:
        c5+=1;

for file in masterNode.db4.keys():
    if masterNode.db4[file][0][0]==0:
        c1+=1;
    elif masterNode.db4[file][0][0]==1:
        c2+=1;
    elif masterNode.db4[file][0][0]==2:
        c3+=1;
    elif masterNode.db4[file][0][0]==3:
        c4+=1;
    elif masterNode.db4[file][0][0]==4:
        c5+=1;

for file in masterNode.db5.keys():
    if masterNode.db5[file][0][0]==0:
        c1+=1;
    elif masterNode.db5[file][0][0]==1:
        c2+=1;
    elif masterNode.db5[file][0][0]==2:
        c3+=1;
    elif masterNode.db5[file][0][0]==3:
        c4+=1;
    elif masterNode.db5[file][0][0]==4:
        c5+=1;

print("c1: "+str(c1)+"\nc2: "+str(c2)+"\nc3: "+str(c3)+"\nc4: "+str(c4)+"\nc5: "+str(c5));
fp.close();
fp1.close();
