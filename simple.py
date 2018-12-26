import re

upperCase = r"[A-Z]"
oneDigit = r"\d"
checker = None


def check_pass(str):
    countErr = 0
    if len(str) < 8:
        print("error: too short, min length is 8")
        countErr += 1
    if not re.findall(upperCase, str):
        print("error: should contain at least one uppercase letter")
        countErr += 1
    if not re.findall(oneDigit, str):
        print("error: should contain at least one digit")
        countErr += 1
    if (countErr != 0):
        checker = False
        return checker
    else:
        checker = True
        return checker




password = ""
while True:
    password = input("Enter Your Password Please: \n")
    if check_pass(password):
        break