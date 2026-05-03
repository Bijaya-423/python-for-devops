# you have to user input to check the CPU threshold. If the CPU usage is above the threshold, print a warning message.

# threshold -> means limit

#check current cpu usage

#if the cpu usage threshold is above 80% , send the email
import psutil #import the psutil in pypi

def check_cpu_usage():
    user_cpu = int(input("Enter the current CPU Threshold:- "))

    current_cpu = psutil.cpu_percent(interval=1) #last 1 second , per cpu - interval means
    # current_cpu = psutil.cpu_percent(interval=1, percpu=True) #last 1 second , per cpu - interval means


    print(f'Per-Core: {current_cpu}')

    if current_cpu > user_cpu:
        print(f"Warning: cpu usage is above {user_cpu}%")
        print(f"CPU Alert Email sent ....")
    else:
        print(f"cpu in safe state.")

check_cpu_usage()








