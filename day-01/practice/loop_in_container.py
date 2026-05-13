import os

containers = ["nginx", "redis", "mysql"]

for container in containers:
    os.system(f"Docker ps -f name={container}")
    