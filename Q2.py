
#student expenses
student=int(input("enter the student : "))
exp=int(input("enter the exp per student : "))
total_exp=(student*exp)
if total_exp<50000:
    print("we are under the budget")
else:
    print("we are out of budget")