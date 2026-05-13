from time import sleep

for i in range(1, 101):
    print(f"\r Progress: {i}%", end="")
    sleep(0.1)

print("\n Task Completed!")