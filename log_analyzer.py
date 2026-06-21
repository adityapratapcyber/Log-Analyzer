logs = [
    "Login Success",
    "Login Failed",
    "Login Failed",
    "Login Success"
]

success = 0
failed = 0

for log in logs:
    if "Success" in log:
        success += 1
    elif "Failed" in log:
        failed += 1

print("Successful Logins:", success)
print("Failed Logins:", failed)
