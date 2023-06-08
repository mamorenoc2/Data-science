# Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.

# Write a space.py program that helps Codey keep track of their target weight by:

# Checks which number planet is equal to.
# It should then compute their weight on the destination planet.

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")


weight = float(input('Put your weight: '))
planet = float(input('Put your planet: '))

# Write an if statement below:
if planet == 1:
  weight *= 0.91
elif planet == 2:
  weight *= 0.38
elif planet == 3:
  weight *= 2.34
elif planet == 4:
  weight *= 1.06
elif planet == 5:
  weight *= 0.92
elif planet == 6:
  weight *= 1.19

print("Your weight:", weight)

