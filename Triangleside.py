def right_triangle(side_1):
    side_1.sort()
    if side_1[2]**2 == side_1[0]**2 + side_1[1]**2:
        return True
    return False
side_1=[]
side_1.append(int(input("Enter side 1: ")))
side_1.append(int(input("Enter side 2: ")))
side_1.append(int(input("Enter side 3: ")))
if right_triangle(side_1):
    print("The given sides are part of right triangle")
else:
    print("The given sides are not part of right triangle")
    