def hsv_Rgb():
    h = float(input("\nEnter Hue (in degrees): "))
    s = float(input("Enter Saturation (in percents): "))
    v = float(input("Enter the value (in percents): "))
    if 0 <= h < 360 and 0 <= s <= 100 and 0 <= v <= 100:
        
        H = 1.00*h
        S = 0.01*s
        V = 0.01*v
        
        C = V*S
        X = C * (1 - (abs(((H/60) % 2) - 1)))
        m = V - C
        
        if 0 <= H < 60:
            x = C; y = X; z = 0
        if 60 <= H < 120:
            x = X; y = C; z = 0
        if 120 <= H < 180:
            y = C; z = X; x = 0
        if 180 <= H < 240:
            y = X; z = C; x = 0
        if 240 <= H < 300:
            x = X; z = C; y = 0
        if 300 <= H < 360:
            x = C; z = X; y = 0
        
        R = round((x+m)*255)
        G = round((y+m)*255)
        B = round((z+m)*255)

        print("\nRGB: (", R, ", ", G, ", ", B, ")\n")
        
    else:
        print("""\n
Some values are wrong.\n
Check if your inputs are correct with conditions:\n
0° <= H < 360°\n
0% <= S <= 100%\n
0% <= V <= 100%\n
            """)
        hsv_Rgb()

def rgb_Hsv():
    x = float(input("\nEnter value of Red: "))
    y = float(input("Enter value of Green: "))
    z = float(input("Enter value of Blue: "))

    if x <= 255 and y <= 255 and z <= 255:
        R = x/255; G = y/255; B = z/255
    
        Cmax = max(R,G,B)
        Cmin = min(R,G,B)

        avg = Cmax - Cmin

        if avg == 0:
            h = 0
        else:
            if Cmax == R:
                h = 60 * (((G-B)/avg) % 6)
            if Cmax == G:
                h = 60 * (((B-R)/avg) + 2)
            if Cmax == B:
                h = 60 * (((R-G)/avg) + 4)

        if Cmax == 0:
            s = 0
        if Cmax != 0:
            s = (avg/Cmax)

        v = Cmax

        H = round(h)
        S = round(s*100)
        V = round(v*100)

        print("\nHSV: (", H, "°, ", S, ", ", V, ")\n")
    
    else:
        print("""
Some values are wrong.\n
Check if your inputs are correct with conditions:\n
0 <= R <= 255\n
0 <= G <= 255\n
0 <= B <= 255""")
        rgb_Hsv()

def select_Mode():
    print("\n1. HSV to RGB\n2. RGB to HSV\n")
    sel = int(input("Choose mode of a program: "))

    if sel == 1 or sel == 2:
        if sel == 1:
            hsv_Rgb()
        if sel == 2:
            rgb_Hsv()
        try_Again()
    else:
        print("\nWrong mode, type 1 or 2.")
        select_Mode()

def try_Again():
    print("Type Y for Yes, or N for No.\n")
    again = str(input("Wanna try again?: "))

    if again == "Y" or again == "y":
        select_Mode()
    else:
        print()

select_Mode()