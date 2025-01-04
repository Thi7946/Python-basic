#โครงสร้างควบคุมแบบทำซ้ำ for loop
#มีจำนวนรอบที่ชัดเจน
'''for loop
for i in range(start,stop,step) #กำหนดรอบ

for i in range(3):# เริ่มต้นที่ 0
    print("รอบที่ = ",i,"Hello World")
    print("รอบที่ = ",i+1,"Hello World")

for i in range(-3,5)
for i in range(-3,5,2)
for i in range(3,0,-1)
start = กำหนด รอบที่เริ่ม
stop = หยุดก่อนเลขที่กำหนด i-1
step = เพิ่มค่ารอบ ตามจำนวนที่กำหนด
'''

sum=0
for i in range(-3,5):# sum
    sum+=i
    print("รอบที่ = ",i,)

print("ผลรวม =",sum)
print("ผลเฉลี่ย =",sum/3)



#รู้จำนวนรอบที่แน่นอน for loop 
#ไม่รู้จำนวนรอบที่แน่นอน whileloop