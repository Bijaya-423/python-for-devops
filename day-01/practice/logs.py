logs = [ "INFO", "ERROR", "INFO", "ERROR", "WARNING" ]

count = 0
for log in logs:
    if log == "ERROR":
        count += 1
print(count)