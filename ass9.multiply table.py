#แม่สูตรคูณ

start = int(input("ป้อนแม่สูตรคูณเริม่ตน ="))
stop = int(input("ป้อนแม่สูตรคูณสุดท้าย ="))

for x in range(start,stop+1):
    print("แม่  = " ,x)
    for y in range(1,13):
        print(x," x ",y," = ",(x*y))


'''
# แม่สูตรคูณ2-12
for x in range(2,13):
    print("แม่  = " ,x)
    for y in range(1,13):
        print(x," x ",y," = ",(x*y))
'''