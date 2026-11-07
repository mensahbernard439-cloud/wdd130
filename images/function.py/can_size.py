import math
def main():
  name = "#1Picnic"
  radius = 6.83
  height = 10.16
  volume =can_vol(radius, height)
  sarea =can_sarea(radius, height)
  eff =volume/sarea
  print(f"name:{name}, volume:{volume}, sa:{sarea}, efficiency{eff:.2f}")

  name ="#1 Tall"
  radius = 7.78
  height = 11.91
  can_eff(name, radius, height)

  can_eff("#2", 8.73,11.59)







def can_eff(name, radius, height):
    volume =can_vol(radius, height)
    sarea =can_sarea(radius, height)
    eff =volume/sarea
    print(f"name:{name}, volume:{volume:.2f}, sa:{sarea:.2f}, efficiency{eff:.2f}")



def can_vol(radius, height):
  volume =math.pi * radius ** 2 * height
  return volume

def can_sarea(radius, height):
  sarea =2*math.pi*radius*(radius + height)
  return sarea


main()