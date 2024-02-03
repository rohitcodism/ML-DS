import cmath


def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if the discriminant is non-negative
    if discriminant >= 0:
        # Calculate real roots
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    else:
        # Calculate complex roots
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def findRootsSelf(a,b,c):
    discriminant = b**2 -4*a*c

    if(discriminant >= 0):
        root1 = ( -b + discriminant) / (2*a)
        root2 = ( -b - discriminant) / (2*a)
        return root1,root2
    else:
        real_part = -b /(2*a)
        img_part = cmath.sqrt(abs(discriminant) / (2*a))
        root1 = complex(real_part, img_part)
        root2 = complex(real_part, -img_part)
        return root1,root2

# Iterate over all possible combinations of coefficients
for a in range(-10, 11):
    for b in range(-10, 11):
        for c in range(-10, 11):
            if a != 0:  # Avoid division by zero
                roots = findRootsSelf(a, b, c)
                print(f"For coefficients a={a}, b={b}, c={c}:")
                print("Roots:", roots)
