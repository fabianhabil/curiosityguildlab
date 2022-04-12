from datetime import date


def calculateAge(agedate):
    thisday = date.today()
    personday = agedate[0]
    personmonth = agedate[1]
    personyear = agedate[2]
    # Compare month day person and today, if true today is past from the birhday, return 1
    pastornot = (personmonth, personday) > (thisday.month, thisday.day)
    age = (thisday.year - personyear) - (pastornot)
    return age


# Input User
nama = input("Your Name? ")
dob = input("Date of Birth? (DD-MM-YYYY) ")
agedate = dob.split("-")
# Get dd mm yyyy from split and convert to integer
agedate = list(map(int, agedate))
age = calculateAge(agedate)
print(f"Welcome, Master {nama}. You are {age} years old as per today!")