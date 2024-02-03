import math


def calculate_circle_area(radius):
    return math.pi * radius ** 2


def calculate_square_area(side):
    return side ** 2


def calculate_rectangle_area(length, width):
    return length * width


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def main():
    while True:
        print("\nMenu:")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Triangle")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
            print("Area of the circle:", area)
        elif choice == '2':
            side = float(input("Enter the side length of the square: "))
            area = calculate_square_area(side)
            print("Area of the square:", area)
        elif choice == '3':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
            print("Area of the rectangle:", area)
        elif choice == '4':
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = calculate_triangle_area(base, height)
            print("Area of the triangle:", area)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
