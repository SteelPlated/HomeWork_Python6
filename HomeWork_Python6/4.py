from tkinter import END


flag=0
x = ('а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я')
fraz = list(map(str, input("Введите стих:\n").split()))
glas=[]
count=0
for i in fraz:
    for k in i:
        for j in k:
            if j in x:
                count+=1
    glas.append(count)
    count=0
for i in range(0,len(glas)-1):
    if glas[i+1]!=glas[i]:
        flag=1
if flag==1:
    print("Пам парам")
else:
  print("Парам пам-пам")  
   
    