
try:
    age = int(input("Age: "))
    income = 20000
    risk_score = income / age

    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")
