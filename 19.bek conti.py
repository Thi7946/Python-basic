#break / continue
#break ออกจากลูป 

i=1
while i<=10:
    print("รอบที่ = ",i)
    if(i==5):
        break
    i+=1
else:
    print("จบโปรแกรม")


'''continue กระโดดช้าม
i=0
while i<=10:
    i+=1
    if(i==5):
        continue
    print("รอบที่ = ",i)

print("จบโปรแกรม")   


i=0
while i<=10:
    i+=1
    if(i%2 !=0):แสดงผลเฉพาะเลขคู่ เลขคี่ข้ามหมด
        continue
    print("รอบที่ = ",i)

print("จบโปรแกรม")   

#for loop ทำได้เหมือนกัน
for i in range(1,11):
     if(i%2==0):
        continue
    print(i)
print("จบโปรแกรม")  

for i in range(1,11):
     if(i==5):
        break
    print(i)
print("จบโปรแกรม")  

'''