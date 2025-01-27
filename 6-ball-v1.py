import random
from time import sleep

chanse = random.randint(1,6)

name = str(input("what is your name?\n"))
sleep(1)
Question = str(input("What is your question about your future?(write in full sentence form)?\n"))

sleep(3)
print(f"Hello {name}, the anwser to your question' {Question}' is.....")
sleep(3)
if chanse == 1:
    print("100%")
elif chanse == 2:
    print("Very likely")
elif chanse == 3:
    print("likely")
elif chanse == 4:
    print("Unlikely")
elif chanse == 5:
    print("Very Unlikely")
elif chanse == 6:
    print("0%")


sleep(5)

print("Cya Later!!!")