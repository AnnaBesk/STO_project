import math
v=int(input("Введите скорость"))
c=300000000 #скорость света в м/с
b=math.pow(v,2)/math.pow(c,2) #бетта
y=1/math.sqrt(1-b)# гамма
t=1 #1 секунда в неподвижной СО
t_=t/y
print(round(t_, 5))
