import collections
def Output1(df):
    d=collections.defaultdict(int)
    for i in df[1:]:
        k=str(','.join(i.strip().split(",")[1:-2])[1:-1])
        d[k]+=1
    return dict(d)
#Output1(df)
def Output2withfilghtcancelled(df):
    max1=0
    outvalue=0
    for i in df[1:]:
        value=int(i.split(',')[-1])
        if value > max1:
            max1=value
            outvalue=str(','.join(i.strip().split(",")[1:-2])[1:-1])
    ndf = Output1(df)
    
    return {outvalue,max1,ndf[outvalue]}
    
#Output2withfilghtcancelled(df)
def OutPut2withCount(df):
    f=Output1(df)
    l=[(i,j) for i,j in f.items() if j==max(f.values())]
    return l
#OutPut2withCount(df)
def Output3withfilghtcancelled(df):
    min1=int(df[1].split(',')[-1])
    outvalue=0
    ndf = Output1(df)
    for i in df[1:]:
        value=int(i.split(',')[-1])
        if value < min1:
            min1=value
            outvalue=str(','.join(i.strip().split(",")[1:-2])[1:-1])
        
    

    return {outvalue,min1,ndf[outvalue]}
#Output3withfilghtcancelled(df)
def OutPut3withCount(df):
    f=Output1(df)
    l=[(i,j) for i,j in f.items() if j==min(f.values())]
    return l

if __name__=="__main__":  
    with open('airlines.csv') as r:
        df=r.readlines()
    print("Output1 = ",Output1(df))
    print("Output2 = ",OutPut2withCount(df))
    print("Output2 (With respect to Flight cancelled) = ",Output2withfilghtcancelled(df))
    print("Output3 = ",OutPut3withCount(df))
    print("Output3 (With respect to Flight cancelled) = ",Output3withfilghtcancelled(df))