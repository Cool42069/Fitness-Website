def gather_user_info():
    print("Welcome! Please provide the following details:")
    
    # Instructions for the user
    print("\nInstructions:")
    print("1. Weight and goal weight should be provided in kilograms (kg).")
    print("2. Height should be provided in centimeters (cm).")
    print("3. Be accurate with your starting and goal weight for the best results.")
    
    # Gather input from the user
    weight = float(input("Enter your current weight (kg): "))
    height = float(input("Enter your height (cm): "))
    goal_weight = float(input("Enter your goal weight (kg): "))
    activity_level=float(input("Enter a number for how many days a week you work out."))
    gender=(input("Are you male or female?"))
    age=float(input("Enter your age in years"))


    
    
    #Calculate Calories with gender in mide
    if gender == "female":
        bmr=10 * weight + 6.25 * height - 5 * age - 161
    elif gender== "male":
        bmr=10 * weight + 6.25 * height - 5 * age + 5
    else:
        return("Missing data")

    if activity_level <= 0:
        daily_calories = bmr * 1.2  # Little or no exercise
    elif activity_level <= 3:
        daily_calories = bmr * 1.375  # Light exercise (1-3 days a week)
    elif activity_level <=5:
        daily_calories = bmr * 1.55  # Moderate exercise (3-5 days a week)
    elif activity_level <=7:
        daily_calories = bmr * 1.725  # Active exercise (6-7 days a week)
    else:
        return "Invalid activity level input"
    print("Your daily calories to stay the same weight is" , int(daily_calories))
    goal_calories=daily_calories-500
    time_frame=((weight-goal_weight)*2.2)*7

    print("Now with your daily calories I have calculated that your goal weight is attainable by eating" , int(goal_calories) , " calories a day, loses a pound of fat a week!!!")
    print("This process will take around", int(time_frame), "weeks")

    
    
    return {
        "weight": weight,
        "height": height,
        "goal_weight": goal_weight
        

    }

user_info =gather_user_info()


    