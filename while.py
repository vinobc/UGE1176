pwd = "octopus"
res = ""
user_auth = False
attempt = 0
max_attempts = 3

while res != pwd:
    attempt += 1
    if attempt > max_attempts: break
    res = input("Enter the password:")
else:
    user_auth = True

print("Successfully logged in" if user_auth else "try again in one hour..")