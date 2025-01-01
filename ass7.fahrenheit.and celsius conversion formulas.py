#แปลงอุณหภูมิ
temp = input("ป้อนอุณภูมิ (องศา) :")

degree = temp[:-1]
unit =temp[-1].upper() #C F

degree = float(degree)
if unit == "C":
    result =((degree*9/5)+32)
    unit_result ="ฟาเรนไฮน์"
if unit == "F":
    print((degree-32)*5/9,"C")
    unit_result ="เซลเซียส"

print("แปลงค่าตัวเลข = ",degree," เป็น ",unit_result," = ",result)

'''
#แปลงอุณหภูมิ
temp = input("ป้อนอุณภูมิ (องศา) :")


if temp.endswith("C"):
    temp = temp[:-1]
    print((float(temp)*9/5)+32,"F")
    #แปลงเป็นฟาเรนไฮน์
if temp.endswith("F"):
    temp = temp[:-1]
    print((float(temp)-32)*5/9,"C")
    #แปลงเป็นเซลเซียส


temp = input("ป้อนอุณภูมิ (องศา) :")

degree = temp[:-1]
unit =temp[-1].upper() #C F

degree = float(degree)
if unit == "C":
    print((degree*9/5)+32,"F")
if unit == "F":
    print((degree-32)*5/9,"C")
'''