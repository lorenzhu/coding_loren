
'''
# loop
loop_conditon = True

while loop_conditon:
    print("I am a loop")
    loop_conditon = False




#
num = 1
while num <=10:
    print(num**2)
    num += 1


#

choice = input('Enjoy the course?(y/n): ')

while choice !='y' or choice != 'no':
#while choice not in ['y', 'n']:
    choice = input("Sorry, I didn't catch that. Enter again: ")


# while...else
import random
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you win!")
count = 0
while count < 3:
    num = random.randint(1,6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")


from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")
'''

#
hobbies = []
for i in range(3):
    hobbies.append(input("input your hobbies:"))
    print(hobbies)
print("Your hobbies: {}".format(hobbies))