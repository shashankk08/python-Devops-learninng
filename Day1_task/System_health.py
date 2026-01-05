import psutil

def system_health():
    current_cpu=psutil.cpu_percent(interval=1)
    current_memory=psutil.virtual_memory().percent
    current_disk=psutil.disk_usage('/').percent

    
    return current_cpu,current_memory,current_disk


user_cpu=int(input("Enter the threshold Cpu "))
user_memory=int(input("Enter the threshold Memory "))
user_disk=int(input("Enter the threshold Disk "))

cpu,memory,disk=system_health()



if cpu>user_cpu:
    print(F"CPU ALERT {cpu}.....need attention")
else:
    print("CPU is under threshold, no action required")
if memory>user_memory:
    print(f"MEMORY ALERT {memory}.....need attention")
else:
    print("MEMORY is under threshold, no action required")

if disk>user_disk:
    print(f"DISK ALERT {disk}.....need attention")
else:
    print("DISK is under threshold, no action required")