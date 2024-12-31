name ="Thiwakorn"# index => 0
names ="   Thiwakorn   yosruengsa r  "# index นับช่องว่างด้วย
name1 = " เราจะไปไหนดี ในเมื่อไม่มีที่ไป"
x = "ไหน"in name1
print(x)#
if x:
    name1=name1.replace("ไหน","ต้องไปแล้ว")
print (name1)
'''การเข้าถึงตัวอักษรใน string
#print(name[0]) ดึงตัว index ตัวที่ 0 เอามาแสดงผล นั้นคือตัว T
#print(name[2:7]) #เอาหลังตัวที่2 ถึง ก่อนตัวที่ 7
#print(name[:7]) / print(name[0:7]) #เอาแรก ถึง ก่อนตัวที่ 7
#print(names[-2]) จะนับย้อนกลัง และตอนนี้เป็นตัว s
#print(names[-2:])  จะได้ sa 
'''

'''len funtion นับตัวอักษร นับ index 
print(len(names))
'''

'''strip funtion 
ลบช่องว่าง 
names.strip() ซ้ายสุด ขวาสุด
names.lstrip() ลบช่องว่าง ซ้าย
names.rstrip() ลบช่องว่าง ขวา

names=names.strip() เก็บค่าในname
'''

'''แปลง case ของ string
แปลงตัวอักษรให้เป็นตัวพิมใหญ๋ ทั้งหมด
print(names.upper())#
แปลงตัวอักษรให้เป็นตัวพิมเล็ก ทั้งหมด
print(names.lower())#

print(names.capitallize())# ให้เอาตัวแรกสุด เป็นตัวใหญ่

print(names.upper()[-8:])# สามารถทำได้
'''

'''การแทนที่
print(name.replace("r","333"))#  แทนที่ r เป็น 333 แปลงทั้งหมด
print(names.replace("r","333",3)) แทนที่ r เป็น333 เปลี่ยนทั้งหมด 3 จุด
'''

'''การเช็คข้อความ => true , false
name1 = " เราจะไปไหนดี ในเมื่อไม่มีที่ไป"
x = "ไหน" in name1
print(x)# ผลลัพ true
if x:
    name1=name.replace("ไหน","ต้องไปแล้ว")
print (name1)
'''
