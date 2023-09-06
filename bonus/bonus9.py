password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["upper-case"] = uppercase

print(result)
print(result.values())

if all (result.values()):
    print("Strong Password")
else:
    print("Weak Password - Your password needs to be at least "
          "8 characters with at least one uppercase and one number.")
