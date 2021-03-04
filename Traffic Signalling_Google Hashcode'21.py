def intersect(*d):
    sets = iter(map(set, d))
    result = sets.next()
    for s in sets:
        result = result.intersection(s)
    return result
    
d,i,s,v,f=map(int,input().split(" "))

street_dict={}
endpoints={}

for k in range (s):
    b,e=map(int,input().split(" "))
    name=str(input())
    l=int(input())
    if name not in street_dict:
        street_dict[name]=[b,e,l]
    if e not in endpoints:
        endpoints[e]=1 
    else:
        endpoints[e]+=1
        
valid_path=[]

latency=[]
for k in range (v):
    s=0
    sent=list(map(str,input().split(" ")))
    length=int(sent[0])
    sent.pop(0)
    # Processing 
    '''ok=[]'''
    for g in sent:
        s+=street_dict[g][2]
        #ok.append(street_dict[g][1])
    latency[k]=s
    valid_path.append(sent)

intersected = list(set(valid_path[0]).intersection(*valid_path[1:]))

actual_inter =set()
for k in intersected:
    actual_inter.add(street_dict[k][0])
    actual_inter.add(street_dict[k][1])
    
actual_inter=list(actual_inter) # [0,1,2] intersection points 

# Number of incoming streets for each interesction according to the cars path clashes
first_final=[]

for k in actual_inter:
    first_final.append([k,endpoints[k]) 
    
# it will give output as 

'''intersection number :   number of incoming streets 
0  : 1  
1   :2  
2   :1 '''

second_final={}
for k in actual_inter:
    okk=set()
    for key ,val in street_dict.items():
        if val[2] == k:
            okk.add(key)
    second_final[k]=list(okk) 
    




    
    




    
    
    
        
# Input done


