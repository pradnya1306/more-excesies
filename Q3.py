#strong password

password=input("enter your password : ")
if len(password)>6 and len(password)<16:
    if "$" in password:
        if ("2" in password) or ("8" in password):
            if ("A" in password) or ("Z" in password):
                print(password,"is strong password")
            else:
                print(password,"is not strong password")
        else:
                print(password,"is not strong password")
    else:
                print(password,"is not strong password")
else:
                print(password,"is not strong password")
