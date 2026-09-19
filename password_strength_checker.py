password = input("Enter Password: ")

has_uper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_uper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

print("\n------Password Checker------")

if len(password) < 8:
    print("❌ Password Must Contain 8 Characters")
if not has_uper:
    print("❌ Password Must Contain an Upper Case latter")
if not has_lower:
    print("❌ Password Must contain the Lower Case letter")
if not has_digit:
    print("❌ Password Must Contain the Digits")
if not has_special:
    print("❌ Password Must Contain the Special Characters")

if (len(password)>= 8 and has_special and has_digit and has_lower and has_uper):
    print("Good Password")
else:
    print("❌ Weak Password")
    
