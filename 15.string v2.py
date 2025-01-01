
name ="1150"
if name.endswith("0"):
    print("ถูกหวย")
else :
    print("ถูกกิน")


'''
#การต่อ string (concatinate) +
fname ="thiwakorn"
lname = "yosruengsa"
age="80"
fullname=fname+lname+age
print(fullname)
print("ชื่อต้น :" +fname+"\tนามสกุล : "+lname+"\tอายุ : "+age )
'''

'''
#การจัดรูปแบบการแสดงผล {} funtion format
fname ="thiwakorn"
lname = "yosruengsa"
age="80"
text="ชื่อต้น :{} \tนามสกุล :{}\tอายุ :{}"
text="ชื่อต้น :{0} \tนามสกุล :{1}\tอายุ :{2}" ระบุตำแหน่งได้ เหมือนกัน เปลี่ยนได้
print(text.format(fname,lname,age))

text="ชื่อต้น :{0} \tนามสกุล :{1}\tอายุ :{2}\tอาชีพ; {3}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์")) ใส้ได้เลยก็ได้

text="ชื่อต้น :{0} \tนามสกุล :{1}\tอายุ :{2}\tอาชีพ; {3}\tเงินเดือน: {4:.2f}" สามารถทำเป็นทศนิยม2 ตำแหน่งได้
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary))
'''

'''นับจำนวนคำในประโยค
fruit="ไปซื้อผลไม้ มีทุเรียน มังคุด มะม่วง ข้าวเหนียวทุเรียน ที่ตลาด"

print(fruit.count("ทุเรียน")) หาทุเรียนว่ามีกี่จุด หาคำว่ามีจุด
'''

'''เช็คคำขึ้นต้น
name ="นายกอไก้ ใจดี"
print(name.startswith("นาย")) คำตอบ true false

name ="นายกอไก้ ใจดี"
if name.startswith("นาย"): เช็คขึเนต้น
    print("เป็นเพศชาย")
else :
    print("เป็นไม่ระบุ")


name ="1150"
if name.endswith("0"): เช็คท้ายสุด
    print("ถูกหวย")
else :
    print("ถูกกิน")
'''