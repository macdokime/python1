# ==================================================
# EXERCISE 2 — INDUSTRIAL QUALITY CONTROL
# ==================================================

# Problem:
# An industrial machine produces 20 components per hour
# for 6 hours.
#
# However, 2 components are rejected every hour.
#
# Your tasks:
# 1. Define the production per hour.
# 2. Define the number of working hours.
# 3. Define the number of rejected components per hour.
# 4. Use a for loop to iterate through the 6 hours.
# 5. Calculate the total production for each hour.
# 6. Calculate the total rejected components.
# 7. Calculate the accepted components.
# 8. Display the results for each hour.
#
# Expected final result:
# Total accepted components = 108
#
# ==================================================
# ==================================================
production_per_hour=20
rejected_per_hour=2
for hour in range(1,7):
    total_production=production_per_hour*hour
    total_rejected=rejected_per_hour*hour
    accepted=total_production-total_rejected
    print(
        "Hour :",hour,
        "|Total production :", total_production,
        "|Total_rejected :", total_rejected, 
        "|Accepted :",accepted
    )