from datetime import datetime

n = input("Patient's name: ")
vb = input("Has the patient been here before? (y/n): ")
h = int(input("What is the patient’s height (in cm)? "))
w = float(input("What is the patient’s weight (in kg)? "))
lwds = input("When was the patient last weighed in (1/1/2000 if never weighed)? ")
lwd = datetime.strptime(lwds, '%d/%m/%Y')
pw = float(input("What was the patient’s weight (in kg, -1 if never weighed)? "))
ha = int(input("Practitioner’s overall assessment of the patient’s health (-5 to +5): "))

bmi = (w / (h ** 2)) * 10000 
bmir = round(bmi, 1)

if bmir < 17:
    category = "Too thin"
    score = 0
elif 17 <= bmir < 18.5:
    category = "Underweight"
    score = 3
elif 18.5 <= bmir < 25:
    category = "Healthy"
    score = 5
elif 25 <= bmir < 30:
    category = "Overweight"
    score = 3
else:
    category = "Obese"
    score = 0

if pw == -1:
    wc = "NEW"
    lv = "First visit"
    wcs = 1
else:
    wc = w - pw
    if vb:
        days = (datetime.now() - lwd).days
        lv = f"Days since last visit: {days}"
    else:
        lv = "First visit"
    
    wc = f"Weight change: {wc:.1f} kg"

    if category == "Underweight" or category == "Too thin":
        if wc < -1:
            wcs = -3
        elif wc > 1:
            wcs = 2
        else:
            wcs = 0
    elif category == "Overweight":
        if wc > 1:
            wcs = -3
        elif wc < -1:
            wcs = 2
        else:
            wcs = 0
    elif category == "Obese":
        if wc > 1:
            wcs = -5
        elif wc < -1:
            wcs = 5
        else:
            wcs = 0
    else:
        wcs = 0

fs = score + wcs + ha

if fs > 5:
    hs = "Great condition!"
elif 3 <= fs <= 5:
    hs = "Need a little work"
elif 1 <= fs < 3:
    hs = "Need a lot of work"
else:
    hs = "At risk!"

print("\t\t Melanie Diet Clinic")
print("\t*------------------------------*\t")
print("\t\tReceipt for Patient Name: {n}")
print("\t\t Patient weight:{w}")
print("\t\t Patient weight loss:{wl}kg")
print("\t\t Days since last visit:{days}")
print("\t*------------------------------*\t")
print("\t\tBMI(conclusion):{bmir}({category})")
print("\t\tHealth(assessment):{wcs}")
print("\t*------------------------------*\t")
print("\t\tOverall:{hs}")