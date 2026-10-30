
# PYTHON REVISION EXERCISE
# Lessons 1 and 2: Variables, Arithmetic, Comparisons, and Conditions
#
# Scenario:
# An industrial machine operates for 8 hours.
# It produces 12 parts per hour.
# At the end of the shift, 7 parts are rejected during quality control.
# The machine temperature is 85 degrees Celsius.
# The maximum allowed temperature is 80 degrees Celsius.
#
# TASK 1: VARIABLES AND CALCULATIONS
# 1. Store the production rate in a variable named production_per_hour.
# 2. Store the operating time in a variable named hours.
# 3. Calculate the total number of parts produced.
#    Store the result in total_produced.
# 4. Store the number of rejected parts in rejected.
# 5. Calculate the number of accepted parts.
#    Store the result in accepted.
# 6. Display the number of accepted parts using print().
#
# TASK 2: CONDITIONS
# 7. Store the machine temperature in temperature.
# 8. Store the maximum allowed temperature in limit.
# 9. Use an if statement to check whether the temperature
#    is greater than the maximum allowed temperature.
# 10. If the temperature is too high, display:
#     "Warning: High temperature!"
# 11. Otherwise, display:
#     "Temperature is normal."
#
# REQUIREMENTS:
# - Use meaningful variable names.
# - Use the correct arithmetic operators.
# - Use if and else correctly.
# - Remember the colon (:) and indentation.
# - Do not copy a complete solution from another source.
# - Run your program and check the output.
#
# CHALLENGE:
# Change the temperature to 75 degrees Celsius.
# Run the program again and observe the message.

#ANSWER TASK

production_per_hour = 12
hours = 8
total_produced = production_per_hour * hours
rejected = 7
accepted = total_produced - rejected
print("Number of accepted parts:", accepted)

#ANSWER TASK2
temperature = 85
limit = 80
if temperature > limit:
    print("Warning: High temperature!")
else:
    print("Temperature is normal.")