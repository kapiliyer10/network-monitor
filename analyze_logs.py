
error_count = 0
success_count = 0
total_devices = 0

with open("logs/ping_log.txt","r") as file:
    for line in file:
        total_devices +=1
        if "UP" in line:
            success_count +=1
        if "DOWN" in line:
            error_count +=1

with open("reports/network_report.txt","w") as report:
    report.write("Network Test Report\n")
    report.write("-------------------\n")
    report.write(f"Total Devices: {total_devices} \n")
    report.write(f"Devices UP: {success_count} \n")
    report.write(f"Devices DOWN: {error_count} \n")
print("Report Generated Successfully")
