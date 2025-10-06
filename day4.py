# this program checks on the user inputs and validate it

print("This program neeeds the credatials to verify them to grand access to users")
print()

username = input("enter your username:")
password = input("enter your password:")

if username == "Obanks" and password == "obanks123":
    print("Access granted")


elif username != "Obanks" and password == "obanks123":
     print("check your creditials and try again!")

else:
     print("Access denied")