
def same_by(characteristic, objects):
    fl=0
    res=[]
    for x in objects:
        res.append(characteristic(x))
    for i in range(0,len(res)-1):
        if res[i+1]!=res[i]:
            fl=1    
    if fl==1:
        return False
    else:
        return True
    
    
values=[0,2,10,6]
if same_by(lambda x:x%2, values):
    print('same')
else:
    print('different')
    
values2=[1,2,3,4]
if same_by(lambda x:x%2, values2):
    print('same')
else:
    print('different') 
     