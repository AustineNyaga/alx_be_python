# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Adjust reminder if time-bound
if time_bound == "yes":
    if priority == "high":
        reminder += " that requires immediate attention today!"
    else:
        reminder += " that should be completed soon."
elif time_bound == "no":
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Plan to complete it at your convenience."
else:
    reminder += " (time sensitivity unclear)."

# Print the final reminder
print("\nReminder:", reminder)