
def is_phone_number(number):
    if len(number)==10 and number[0] in "987":
        return True
    return False
phone_number=input("Enter a mobile number")
if is_phone_number(phone_number):
    print("the phone number",phone_number,"is valid")
else:
    print("The phone number ",phone_number,"is invalid")
