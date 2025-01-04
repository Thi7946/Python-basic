#loop ซ้อน loop

#while true เงื่อนไขนี้เป็นจริงตลอด
# ทำลูปในจนมันเป็นเท็จก่อน ถึงจะทำลูปข้างนอกต่อ
i=1
while i<=3:
    j=1 
    while j<=5:
        print("รอบที่ =",i,"ตำแหน่งที่",j)
        j+=1
    i+=1

# ทำลูปในจนมันเป็นเท็จก่อน ถึงจะทำลูปข้างนอกต่อ
for i in range(1,4):
    print("รอบที่ = ",i)
    for j in range(1,6):
        print("ตำแหน่งที่ = ",j)

'''
s = int(input("ใส่ตัวเลช"))
r = int(input("ใส่ตัวเลช"))

for i in range(s,r):
    print("รอบที่ = ",i)
    for j in range(s,r):
        print("ตำแหน่งที่ = ",j)
'''