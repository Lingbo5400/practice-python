a ="Hello welcome to Cathay 60th year anniversary"
b =list(a.lower()) #將文字統一大小寫
#print(b)
d ={} #建立一個dic
for i in b:
    d[i]=b.count(i)
print(d)
