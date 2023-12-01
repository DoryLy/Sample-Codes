border = "+" + "-"*100 + "+"

print(border)
print("\n")
# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
district_number = int(input("Enter your district number (1-9): "))

print("\n")

# Define district-color mapping
district_colors = {
    1: "Blue",
    2: "Red",
    3: "Blue",
    4: "Red",
    5: "Blue",
    6: "Red",
    7: "Green",
    8: "Green",
    9: "Green"
}

# Define curfew schedules
standard_schedule = "10:00pm - 4:00am"
special_schedule = "10:00pm - 4:00am (Mon, Thu, Fri)"

# Determine the district color
district_color = district_colors.get(district_number, "Unknown")

# Determine the curfew schedule based on age and district
if age < 18 or age > 60:
    if district_color == "Blue":
        curfew_schedule = "10:00pm - 4:00am (Mon, Thu, Fri)"
    elif district_color == "Red":
        curfew_schedule = "10:00pm - 4:00am (Wed, Sat, Mon)"
    elif district_color == "Green":
        curfew_schedule = "10:00pm - 4:00am (Tue, Fri, Sat)"
    else:
        curfew_schedule = "No curfew information available for this district"
else:
    if district_color == "Blue":
        curfew_schedule = "10:00pm - 4:00am (Mon, Thu)"
    elif district_color == "Red":
        curfew_schedule = "10:00pm - 4:00am (Wed, Sat)"
    elif district_color == "Green":
        curfew_schedule = "10:00pm - 4:00am (Tue, Fri)"
    else:
        curfew_schedule = "No curfew information available for this district"

print(border)
print("\n")

# Display user information and curfew schedule
print("\nUser Information:")
print("Name:", name)
print("District Color:", district_color)
print("Curfew Schedule:", curfew_schedule)

print("\n")
print(border)