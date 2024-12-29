'''
โครงสร้างควบคุม (control struture)
1.สร้างลำดับ
2.แบบเลือก
3.แบบทำซ้ำ
'''
age = int(input("ป้อนอายุของคุณ"))
money = int(input("ตังที่จะซื้อขนม"))
age ==15
name ="thiwakorn"
print(type(age>=15))
print(name=="thiwakorn")

'''
if age>=15:  
    print("คำนำหน้าเป็น นาย/นางสาว")
else :
    print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")
"""elif age<=15:
    print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")
"""
'''
if age>=30 and age <=39:
    print("วัยผู้ใหญ่")
elif age>=20 and age <= 30:
    print("วัยหนุ่มสาว")
elif age>=15 and age <=20:
    print("วัยรุ่น")
elif age>=40 :
    print("ลุงป้า")
else :
    print("วัยเด็ก")

#Ternary operater
"""เงื่อนไขเป็นจริง" if expresssion else "เงือ่นไขอื่นๆ"""
print("ได้กินขนม") if money>=15 else ("อดกิน")


#15-20 =>วัยรุ่น
#21-29=>วัยหนุ่มสาว
#30-39=>วัยผู้ใหญ่

# and or not



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