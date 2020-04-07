def hashMap(queryType, query):
    d,e,s={},[],0
    for i,j in zip(queryType,query):
        if i == 'insert':
            d[j[0]]=j[1]
            e+=[j[0]]
        elif i == 'addToValue':
            for x in e:
                d[x]+=j[0]
        elif i == 'addToKey':
            e=sorted(e)
            if j[0]>0:
                for x in range(len(e)-1,-1,-1):
                    d[e[x]+j[0]]=d[e[x]]
                    e[x]+=j[0]
            else:
                for x in range(0,len(e)):
                    d[e[x]+j[0]]=d[e[x]]
                    e[x]+=j[0]
        elif i== 'get':
            s+=d[j[0]]
    return s    
