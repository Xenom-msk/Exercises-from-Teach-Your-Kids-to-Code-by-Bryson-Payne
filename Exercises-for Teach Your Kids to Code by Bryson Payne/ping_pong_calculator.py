# Ping pong ball (PPB) calculator

# Convert to ENTIRE FUCKING WORLD measures
def convert_in2cm(inches):
    return inches*2.54

def convert_lb2kg(pounds):
    return pounds/2.2

# Convert to US measures
def convert_cm2in(cm):
    return cm/2.54

def convert_kg2lb(kg):
    return kg*2.2

your_height_in=int(input("Enter your height in inches: "))
your_weight_lb=int(input("Enter your weight in pounds: "))

height_cm = convert_in2cm(your_height_in)
weight_kg = convert_lb2kg(your_weight_lb)

feet=your_height_in//12
inch=your_height_in%12

ppb_height=round(height_cm/4)
ppb_weight=round(weight_kg*1000/2.7)

print("At",feet,"feet",inch,"inches tall, and",your_weight_lb,"pounds")
print("You measure",ppb_height,"ping-pong balls tall")
print("You weight is",ppb_weight,"ping-pong balls")
