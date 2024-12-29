#Type coversion
x =10
y =3.14
z =" 20"

#บวกเลข
result = x+y #10+3.14 = 13.14
result1 = x+int(z) #string => int ทำการแปลงค่า
result2 = str(x)+z #int => string ทำการแปลงค่า

print(type(x))
print(type(y))
print(type(z))
float(z)# แสดงแค่บรรทัดนี้
z=float(z) #ทำให้เปลี่ยนtype ถาวรได้ ทำให้เวลาเช็คtype z ขึ้น float ได้
#ทำให้การแสดงได้หลายบรรทัดไม่ต้องทำบ่อยๆ

print(result)
print(result1)
print(result2)
print(float(z))#str => float
print(str(y))#float =>str
print(float(x))
print(int(y))