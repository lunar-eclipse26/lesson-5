amount = int(input("please enter the amount of sheckles you want to withdraw:"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print("gives coin of 1000 sheckles", note_1)
print("gives coin of 500 sheckles", note_2)
print("gives coin of 100 sheckles", note_3)