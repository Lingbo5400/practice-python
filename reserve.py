input =[35,46,57,91,29]
output=[]
for i in input:
    st=str(i)
    reserst =st[::-1]
    output.append(int(reserst))
    
print("輸入:",input)
print("輸出:",output)    