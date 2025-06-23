# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority level"

# Modify message if the task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif "Note" in message:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print("\n" + message)