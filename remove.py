number=int(input("輸入：n值(0-100):"))
list=[] 
count=0

#1~100依序放入陣列
for i in range(1,number+1):
    list.append(i)



while 1:
   #若陣列僅剩一個，它就是唯一結果
   if len(list)==1:
       print("最後留下的人是第",list,"順位")
       break
   else: #count不算到3就將第一個陣列值取出放到最後呈現一個cycle
       count+=1
       cycle_num=list[0]
       list.pop(0)
       if count==3:
           count=0
           continue
       else:
           list.append(cycle_num)