def dividestring(s,k,fill):
    res=[]
    for i in range(0,len(s),k):
        grp=s[i:i+k]
        if len(grp)<k:
            grp += fill*(k-len(grp))
        res.append(grp)
    return res