#Your lifes in week
age=int(input("What is your current age ?\n"))
remaining_years=90-age
rem_months=remaining_years*12
rem_weeks=remaining_years*52
rem_days=remaining_years*364.25
print(f"You have {rem_days} days remaining,{rem_weeks} weeks remaining,{rem_months} months remaining,{remaining_years} years remaining")
