import os, random
import time

class namenode:
    
    def __init__(self, num_racks, num_nodes):
        self.node_status=[]
        self.num_nodes=num_nodes
        self.num_racks=num_racks
        self.db1={};
        self.db2={};
        self.db3={};
        self.db4={};
        self.db5={};
        for i in range(0,5):
            temp_arr=[]
            for j in range(0,num_racks):
                temp_arr2=[]
                for j in range(0,num_nodes):
                    temp_arr2.append(0)
                temp_arr.append(temp_arr2)
            self.node_status.append(temp_arr)

    def add_file(self, name, server, total_crit, num_dups, num_access):
        handle=ord(name[0])%5;
        if handle==0:
            if name not in self.db1.keys():
                assigned_node,assigned_rack=self.locate_random_empty_node(server,[]);
                if assigned_node==-1:
                    print("server full");
                    return
                self.node_status[server][assigned_rack][assigned_node]=1;
                self.save_file(name, server, assigned_rack, assigned_node, total_crit, num_access);
                self.duplicate(name, server, assigned_rack, total_crit, num_dups, num_access);
        elif handle==1:
            if name not in self.db2.keys():
                assigned_node,assigned_rack=self.locate_random_empty_node(server,[]);
                if assigned_node==-1:
                    print("server full");
                    return
                self.node_status[server][assigned_rack][assigned_node]=1;
                self.save_file(name, server, assigned_rack, assigned_node, total_crit, num_access);
                self.duplicate(name, server, assigned_rack, total_crit, num_dups, num_access);
        elif handle==2:
            if name not in self.db3.keys():
                assigned_node,assigned_rack=self.locate_random_empty_node(server,[]);
                if assigned_node==-1:
                    print("server full");
                    return
                self.node_status[server][assigned_rack][assigned_node]=1;
                self.save_file(name, server, assigned_rack, assigned_node, total_crit, num_access);
                self.duplicate(name, server, assigned_rack, total_crit, num_dups, num_access);
        elif handle==3:
            if name not in self.db4.keys():
                assigned_node,assigned_rack=self.locate_random_empty_node(server,[]);
                if assigned_node==-1:
                    print("server full");
                    return
                self.node_status[server][assigned_rack][assigned_node]=1;
                self.save_file(name, server, assigned_rack, assigned_node, total_crit, num_access);
                self.duplicate(name, server, assigned_rack, total_crit, num_dups, num_access);
        elif handle==4:
            if name not in self.db5.keys():
                assigned_node,assigned_rack=self.locate_random_empty_node(server,[]);
                if assigned_node==-1:
                    print("server full");
                    return
                self.node_status[server][assigned_rack][assigned_node]=1;
                self.save_file(name, server, assigned_rack, assigned_node, total_crit, num_access);
                self.duplicate(name, server, assigned_rack, total_crit, num_dups, num_access);
        return

    def duplicate(self, name, server, assigned_rack, total_crit, num_dups, num_access):
        temp_var=0
        not_rack=[]
        not_rack.append(assigned_rack)
        while temp_var < num_dups:
            
            assigned_dupnode,assigned_duprack=self.locate_random_empty_node(server,not_rack)
            not_rack.append(assigned_rack)
            self.node_status[server][assigned_duprack][assigned_dupnode]=1
            self.save_file(name, server, assigned_duprack, assigned_dupnode, total_crit, num_access)
            temp_var+=1
            
            
        

    def locate_random_empty_node(self,server, not_rack):
         random_rack=random.randint(1, self.num_racks)-1
         while not_rack!=[] and random_rack in not_rack:
             if random_rack<=self.num_racks/2:
                 random_rack+=random.randint(1,int(self.num_nodes/2)-1)
             else:
                 random_rack-=random.randint(1,int(self.num_nodes/2)-1)

         random_starter=random.randint(1,self.num_nodes)-1
         temp_var=random_starter
         temp_var2=random_rack
         while temp_var2<self.num_racks:
             while temp_var<self.num_nodes:
                 if self.node_status[server][temp_var2][temp_var]==0:
                     return temp_var,temp_var2
                 else:
                    temp_var+=1
             temp_var=0
             while temp_var<random_starter:
                 if self.node_status[server][temp_var2][temp_var]==0:
                     return temp_var, temp_var2
                 else:
                    temp_var+=1
         
             temp_var2+=1            
         temp_var2=0
         temp_var=random_starter
         while temp_var2<random_rack:
             while temp_var<self.num_nodes:
                 if self.node_status[server][temp_var2][temp_var]==0:
                     return temp_var,temp_var2
                 else:
                    temp_var+=1
             temp_var=0
             while temp_var<random_starter:
                 if self.node_status[server][temp_var2][temp_var]==0:
                     return temp_var, temp_var2
                 else:
                    temp_var+=1
         
             temp_var2+=1

         return -1,-1


    def del_file(self,name):
        handle=ord(name[0])%5;
        if handle==0:
            if name in self.db1.keys():
                del self.db1[name]
        elif handle==1:
            if name in self.db2.keys():
                del self.db2[name]
        elif handle==2:
            if name in self.db3.keys():
                del self.db3[name]
        elif handle==3:
            if name in self.db4.keys():
                del self.db4[name]
        elif handle==4:
            if name in self.db5.keys():
                del self.db5[name]


    def shift_file(self,name,change_to_server):
        handle=ord(name[0])%5;
        tem_num_dumps=0;
        if handle==0:
            temp_data=self.db1[name][0];
            temp_num_dumps=len(self.db1[name])-1;
            self.del_file(name);
        elif handle==1:
            temp_data=self.db2[name][0];
            temp_num_dumps=len(self.db2[name])-1;
            self.del_file(name);
        elif handle==2:
            temp_data=self.db3[name][0];
            temp_num_dumps=len(self.db3[name])-1;
            self.del_file(name);
        elif handle==3:
            temp_data=self.db4[name][0];
            temp_num_dumps=len(self.db4[name])-1;
            self.del_file(name);
        elif handle==4:
            temp_data=self.db5[name][0];
            temp_num_dumps=len(self.db5[name])-1;
            self.del_file(name);
        self.add_file(name,change_to_server,temp_data[-2],temp_num_dumps, temp_data[-1])
        
    def save_file(self,name, server, assigned_rack, assigned_node, total_crit, num_access):
        f=open("status.txt",'a')
        f.write(str(time.time())+": "+name+";"+str(server)+";"+str(assigned_rack)+";"+str(assigned_node)+";"+str(total_crit)+"\n")
        arm=ord(name[0])
        if arm%5==0:
            if name not in self.db1.keys():
                self.db1[name]=[]
                self.db1[name].append([server, assigned_rack, assigned_node, total_crit, num_access]);
            else:
                self.db1[name].append([assigned_rack, assigned_node]);
        
        elif arm%5==1:
            if name not in self.db2.keys():
                self.db2[name]=[]
                self.db2[name].append([server, assigned_rack, assigned_node, total_crit, num_access]);
            else:
                self.db2[name].append([assigned_rack, assigned_node]);
        
        elif arm%5==2:
            if name not in self.db3.keys():
                self.db3[name]=[]
                self.db3[name].append([server, assigned_rack, assigned_node, total_crit, num_access]);
            else:
                self.db3[name].append([assigned_rack, assigned_node]);
        
        elif arm%5==3:
            if name not in self.db4.keys():
                self.db4[name]=[]
                self.db4[name].append([server, assigned_rack, assigned_node, total_crit, num_access]);
            else:
                self.db4[name].append([assigned_rack, assigned_node]);
        
        elif arm%5==4:
            if name not in self.db5.keys():
                self.db5[name]=[]
                self.db5[name].append([server, assigned_rack, assigned_node, total_crit, num_access]);
            else:
                self.db5[name].append([assigned_rack, assigned_node]);
        

        f.close();
        
    def updateCriticalities(self, file_critics):
        fp3=open('update.txt','a');
        for file in file_critics.keys():
            arm=ord(file[0]);
            critic=file_critics[file];
            server=0;
            if critic >=0.0 and critic <=1.0:
                server=0;
            elif critic >1.0 and critic <=2.0:
                server=1;
            elif critic >2.0 and critic <=3.0:
                server=2;
            elif critic >3.0 and critic <=4.0:
                server=3;
            elif critic >4.0 and critic <=5.0:
                server=4;
            if arm%5==0:
                if file not in self.db1.keys():
                    self.add_file(file,server,critic,3,0);
                else:
                    if self.db1[file][0][0]==server:
                        self.db1[file][0][3]=critic;
                    else:
                        fp3.write(str(time.time())+": Shifting file "+file+" from server "+str(self.db1[file][0][0])+" to server "+str(server)+" init critic: "+str(self.db1[file][0][3])+" new_critic: "+str(critic)+"\n");
                        self.shift_file(file,server);
            elif arm%5==1:
                if file not in self.db2.keys():
                    self.add_file(file,server,critic,3,0);
                else:
                    if self.db2[file][0][0]==server:
                        self.db2[file][0][3]=critic;
                    else:
                        fp3.write(str(time.time())+": Shifting file "+file+" from server "+str(self.db2[file][0][0])+" to server "+str(server)+" init critic: "+str(self.db2[file][0][3])+" new_critic: "+str(critic)+"\n");
                        self.shift_file(file,server);
            elif arm%5==2:
                if file not in self.db3.keys():
                    self.add_file(file,server,critic,3,0);
                else:
                    if self.db3[file][0][0]==server:
                        self.db3[file][0][3]=critic;
                    else:
                        fp3.write(str(time.time())+": Shifting file "+file+" from server "+str(self.db3[file][0][0])+" to server "+str(server)+" init critic: "+str(self.db3[file][0][3])+" new_critic: "+str(critic)+"\n");
                        self.shift_file(file,server);
            elif arm%5==3:
                if file not in self.db4.keys():
                    self.add_file(file,server,critic,3,0);
                else:
                    if self.db4[file][0][0]==server:
                        self.db4[file][0][3]=critic;
                    else:
                        fp3.write(str(time.time())+": Shifting file "+file+" from server "+str(self.db4[file][0][0])+" to server "+str(server)+" init critic: "+str(self.db4[file][0][3])+" new_critic: "+str(critic)+"\n");
                        self.shift_file(file,server);
            elif arm%5==4:
                if file not in self.db5.keys():
                    self.add_file(file,server,critic,3,0);
                else:
                    if self.db5[file][0][0]==server:
                        self.db5[file][0][3]=critic;
                    else:
                        fp3.write(str(time.time())+": Shifting file "+file+" from server "+str(self.db5[file][0][0])+" to server "+str(server)+" init critic: "+str(self.db5[file][0][3])+" new_critic: "+str(critic)+"\n");
                        self.shift_file(file,server);
        fp3.close();


    def access_file(self,name):
        arm=ord(name[0])
        if arm%5==0:
            if name not in self.db1.keys():
                print("file does not exist");
            else:
                print("file accessed");
                self.db1[name][0][-1]+=1
        
        elif arm%5==1:
            if name not in self.db2.keys():
                print("file does not exist");
            else:
                print("file accessed");
                self.db2[name][0][-1]+=1
                
        elif arm%5==2:
            if name not in self.db3.keys():
                print("file does not exist");
            else:
                print("file accessed");
                self.db3[name][0][-1]+=1
        elif arm%5==3:
            if name not in self.db4.keys():
                print("file does not exist");
            else:
                print("file accessed");
                self.db4[name][0][-1]+=1
        elif arm%5==4:
            if name not in self.db5.keys():
                print("file does not exist");
            else:
                print("file accessed");
                self.db5[name][0][-1]+=1
