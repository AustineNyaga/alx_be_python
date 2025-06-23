# Get task with validation
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Error: Task cannot be empty.")

# Get priority with strict validation
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in {'high', 'medium', 'low'}:
        break
    print("Error: Priority must be 'high', 'medium', or 'low'.")

# Get time-bound with strict validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in {'yes', 'no'}:
        break
    print("Error: Must answer 'yes' or 'no'.")

# Build reminder (match case)
match priority:
    case "high":
        reminder = f"URGENT: '{task}' (High Priority)"
    case "medium":
        reminder = f"REMINDER: '{task}' (Medium Priority)"
    case "low":
        reminder = f"NOTE: '{task}' (Low Priority)"

# Add time sensitivity (if statement)
if time_bound == "yes":
    reminder += " - REQUIRES IMMEDIATE ACTION TODAY!"
else:
    reminder += " - Complete when convenient."

# Print final reminder
print("\n" + "="*50)
print("TASK REMINDER:")
print(reminder)
print("="*50)