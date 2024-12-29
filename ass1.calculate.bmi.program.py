#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg)/ส่วนสูง =ส่วนสูง(cm)

#input
#kg,cm =map(float,[input("ป้อนน้ำหนักของคุณ (kg) : "),input("ป้อนส่วนสูงของคุณ (cm) : ")])
kg,cm =map(float,[input("ป้อนน้ำหนักของคุณ (kg) : "),(int(input("ป้อนส่วนสูงของคุณ (cm) : "))/100)])
#process
#cm = (cm/100)**2 #cm=>m
#BMI = kg/cm
#BMI=kg/(m**2)

#input
#weight=float(input("ป้อนน้ำหนักของคุณ (kg) : "))
#high=float(input("ป้อนส่วนสูงของคุณ (cm) : "))
#high=float(input("ป้อนส่วนสูงของคุณ (cm) : "))/100

#process
#high/=100   #high=high/100   #cm=>m


#calculate bmi
#BMI=weight/(high*high)
#BMI=weight/high**2

#output
#print("BMI =",BMI)
#print("BMI =",weight/(high*high))
print("BMI =",kg/(cm*cm))
