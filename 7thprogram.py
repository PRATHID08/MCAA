import math

def area_of_triangle(a, b, c):


    s = (a + b + c) / 2
    
    try:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    except ValueError:
        area = 0
    
    return area

def main():
    print("Enter the sides of the first triangle:")
    try:
        a1 = float(input("Side a: "))
        b1 = float(input("Side b: "))
        c1 = float(input("Side c: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    print("Enter the sides of the second triangle:")
    try:
        a2 = float(input("Side a: "))
        b2 = float(input("Side b: "))
        c2 = float(input("Side c: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    area1 = area_of_triangle(a1, b1, c1)
    area2 = area_of_triangle(a2, b2, c2)
    total_area = area1 + area2
    
    if total_area > 0:
        percentage1 = (area1 / total_area) * 100
        percentage2 = (area2 / total_area) * 100
    else:
        percentage1 = 0
        percentage2 = 0
    

    print(f"\nArea of the first triangle: {area1:.2f}")
    print(f"Area of the second triangle: {area2:.2f}")
    print(f"Total area of both triangles: {total_area:.2f}")
    print(f"First triangle's contribution: {percentage1:.2f}%")
    print(f"Second triangle's contribution: {percentage2:.2f}%")

if __name__ == "__main__":
    main()
