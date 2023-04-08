import datetime

# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Define a function to check if a person is underweight, normal, overweight or obese
def check_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"

# Define a function for the balanced diet plan
def balanced_diet():
    # Include all the food items that an elderly person should consume
    diet = {
        "fruits": ["apples", "bananas", "oranges", "grapes"],
        "vegetables": ["spinach", "carrots", "broccoli", "sweet potatoes"],
        "protein": ["beans", "chicken", "fish", "eggs"],
        "dairy": ["milk", "yogurt", "cheese"],
        "whole grains": ["brown rice", "whole wheat bread", "oatmeal"],
    }
    return diet

# Define a function for exercise routine
def exercise_routine():
    # Include exercises that are beneficial for elderly persons
    exercises = ["walking", "swimming", "cycling", "yoga"]
    return exercises

# Define a function for setting medication reminders
def set_alarm():
    # Set an alarm for medication reminders
    alarm_time = input("Enter the time for medication reminder (HH:MM AM/PM): ")
    alarm_time = datetime.datetime.strptime(alarm_time, "%I:%M %p")
    return alarm_time

# Define a function for stress management
def stress_management():
    # Include stress-relieving activities
    activities = ["meditation", "deep breathing exercises", "listening to music", "reading"]
    return activities

# Define a function for avoiding smoking and alcohol
def avoid_smoking_alcohol():
    # Advise against smoking and alcohol consumption
    print("Smoking and alcohol consumption are harmful to health. Please avoid them.")

# Define a function for social activities
def social_activities():
    # Suggest social activities that elderly persons can engage in
    activities = ["playing board games with friends and family", "attending community events", "joining a hobby group"]
    return activities

# Call the functions
weight = 70 # in kilograms
height = 1.6 # in meters
bmi = calculate_bmi(weight, height)
bmi_category = check_bmi_category(bmi)
print("Your BMI is:", bmi)
print("Your BMI category is:", bmi_category)

diet_plan = balanced_diet()
print("Your balanced diet plan is:", diet_plan)

exercise_plan = exercise_routine()
print("Your exercise routine includes:", exercise_plan)

medication_reminder = set_alarm()
print("Your medication reminder is set for:", medication_reminder)

stress_relief_activities = stress_management()
print("Your stress-relief activities include:", stress_relief_activities)

avoid_smoking_alcohol()

social_activities = social_activities()
print("Your suggested social activities include:", social_activities)

