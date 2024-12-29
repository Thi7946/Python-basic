'''
โครงสร้างควบคุม (control struture)
1.สร้างลำดับ
2.แบบเลือก
3.แบบทำซ้ำ
'''
age = int(input("ป้อนอายุของคุณ"))
age ==15
name ="thiwakorn"
print(type(age>=15))
print(name=="thiwakorn")

if age>=15:  
    print("คำนำหน้าเป็น นาย/นางสาว")
else :
    print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")
"""elif age<=15:
    print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")
"""
if age>=30:
    print("วัยทำงาน")
elif age>=20:
    print("วัยผู้ใหญ๋")
elif age>=15:
    print("วัยรุ่น")
else :
    print("วัยเด็ก")



print("จบโปรแกรม")
 #if เงื่อนไขเป็นจริงเท่านั้น 

'''
if expression:
    statement 

'''

'''
if จริง :
    ทำอะไร
else :
    ทำอะไร

'''