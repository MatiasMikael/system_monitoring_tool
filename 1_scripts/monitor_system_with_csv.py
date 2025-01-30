import psutil
import time
import csv
import logging

# Configure logging
logging.basicConfig(
    filename="5_logs/system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize CSV file
def initialize_csv(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"])

# Append data to CSV file
def append_to_csv(file_name, cpu, memory, disk):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), cpu, memory, disk])

# Monitor system resources
def monitor_system(duration_in_minutes=1):
    csv_file = "5_logs/system_metrics.csv"
    initialize_csv(csv_file)

    start_time = time.time()
    duration_in_seconds = duration_in_minutes * 60

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > duration_in_seconds:
            logging.info("Monitoring finished.")
            print("Monitoring finished.")
            break

        # Get system metrics
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        # Log and save metrics
        logging.info(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory}% | Disk Usage: {disk}%")
        print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory}% | Disk Usage: {disk}%")
        append_to_csv(csv_file, cpu_usage, memory, disk)

        time.sleep(1)

if __name__ == "__main__":
    monitor_system(duration_in_minutes=1)