password = input("enter your password: ")
if len(password) >= 8:
    print("length Length: Valid (8+ characters)")
else:
    print("password should be at least 8 characters.")
    has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "~`!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True
print("Uppercase :", has_upper)
print("Lowercase :", has_lower)
print("Number    :", has_digit)
print("Special   :", has_special)
score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1
if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
    if len(password) < 8:
     print("- Use at least 8 characters")

if not has_upper:
    print("- Add at least one uppercase letter (A-Z)")

if not has_lower:
    print("- Add at least one lowercase letter (a-z)")

if not has_digit:
    print("- Add at least one number (0-9)")

if not has_special:
    print("- Add at least one special character (!@#$%^&*)")