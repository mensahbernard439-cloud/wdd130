def getinaction(prompt):
# Get the value out
  value =float(input(prompt))
#Value must be positive
  while value <= 0:
    print("Sorry value must be positive")

    value =float(input(prompt))
  return value
  





length =getinaction("What is the length of the rectangle? ")
width =getinaction("What is the width of the rectangle? ")

area = length * width

print(f"The area of the rectangle is {area}")