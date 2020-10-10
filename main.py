import math
PI = math.pi

# get radius
r = int(input())

# define size of the print area (matrix)
size = 2 * r + 2

# initialize the print area with spaces
db = []
for i in range(size):
    db.append([])
    for j in range(size):
        db[i].append(' ')

# define center points
a = size / 2
b = size / 2

# define symbol
s = '*'

# coordinates of the vertices of 5-point star
# rounded to 2 decimal points to avoid floating point errors
# for more info: https://math.stackexchange.com/questions/3582342/coordinates-of-the-vertices-of-a-five-pointed-star
star_x = []
star_y = []
for k in range(5):
    star_x.append(round(r*math.cos(2*PI*k/5 + PI) + a, 2))
    star_y.append(round(r*math.sin(2*PI*k/5 + PI) + b, 2))

# define error limits
L1 = 0.5
L2 = 1

# for each (x, y) coordinate, check whether it lies on the one of 5 straight lines of the star
for x in range(size):
    for y in range(size):
        for k in range(5):
            # equation of each straight line is generated using 2 points (x1, y1) and (x2, y2)
            x1, x2 = star_x[k], star_x[k+2 if k+2 < 5 else k-3]
            y1, y2 = star_y[k], star_y[k+2 if k+2 < 5 else k-3]
            try:
                if abs((y-y1)-((y2-y1)/(x2-x1))*(x-x1)) < L1 and ((x-a)**2 + (y-b)**2 - r**2 < L2):
                    db[x][y] = s
            except:
                if abs(x-x1) < L1 and ((x-a)**2 + (y-b)**2 - r**2 < L2):
                    db[x][y] = s    

# printing...
for i in range(size):
    for j in range(size):
        print(db[i][j], end=" ")
    print()
