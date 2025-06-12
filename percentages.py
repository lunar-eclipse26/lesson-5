print("enter marks obtained in 4 subjects")
PE = int(input("PE:"))
tech = int(input("tech:"))
maths = int(input("maths:"))
literacy = int(input("literacy:"))
sum = PE+tech+maths+literacy
print("sum of PE, tech, maths and literacy are", sum)
perc = (sum/400)*100
print(end="percentage mark =")
print(perc)