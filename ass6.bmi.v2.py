kg,cm =map(float,[input("ป้อนน้ำหนักของคุณ (kg) : "),(int(input("ป้อนส่วนสูงของคุณ (cm) : "))/100)])
BMI = kg/(cm*cm)
print("BMI =",kg/(cm*cm))

if BMI <18.4 :
    result="น้ำหนักต่ำกว่าเกณฑ์"
elif BMI >= 18.5 and BMI < 23.0:
    result="สมส่วน"
elif BMI >= 23 and BMI < 25.0:
    result="น้ำหนักเกิน"
elif BMI >= 25 and BMI < 30.0:
    result="โรคอ้วนระดับ ที่ 1"
elif BMI >30 :
    result="อ้วนมาก ควรลดน้ำหนัก"
else :
    result ="ไม่ทราบค่าที่ชัดเจน"

print(result)
'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 สมส่วน
23.0 - 24.9 น้ำหนักเกิน
25.0-29.9 โรคอ้วน ระดับที่
>30 อ้วนมาก ควรลดน้ำหนัก
'''