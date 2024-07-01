nickname = input("What should I call you today? ")
print("Hello " + nickname)
total_saving = input("How much do you have in your savings account? ")
expenses = input("How much are your expenses this month? ")
print("Got it, $" + expenses)
income = input("How much did you make this paycheck? ")
print("Nice, so: $" + income)
if float(income) - float(expenses) < 1:
    print("Uh oh! you don't have much money, " + nickname)
elif float(income) - float(expenses) > 1:
    print("Doing great so far, " + nickname)
    leftover = float(income) - float(expenses)
    savings = float(leftover) * 0.50
    spending = float(leftover) - (savings)
    second_check = input("Is this your second check? Say 'Yes' or 'No': ")
    if second_check.lower() == "no":
        final_saving = float(total_saving) + float(savings)
        print("Oh, okay. Got it")
        print("It's math time!")
        print("In leftover money, you will have: " + str(leftover))
        print("I recommend saving 50% of that which would mean: " + str(savings))
        print("This will give you this amount in spending money: " + str(spending))
        print("Your total amount in savings should be: " + str(final_saving))
    elif second_check.lower() == "yes":
        saving_second = float(income) * 0.50
        final_saving = float(total_saving) + float(saving_second)
        print("Since this is your second check, this would be your amount of spending money: " + str(saving_second))
        print("Since I recommended saving 50% of that, you would save: " + str(saving_second))
print("Have a great day, " + nickname)