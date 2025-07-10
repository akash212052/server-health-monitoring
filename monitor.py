import psutil
import logging

logging.basicConfig(
    filename='system_health.log' ,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

CPU_THRESHOLD = 80
MEM_THRESHOLD = 81
DISK_THRESHOLD = 82

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        logging.warning(f"High CPU usage: {cpu}%")
    else:
        logging.info(f"cpu usage: {cpu}%")

def check_memory():
    memory = psutil.virtual_memory().percent
    if memory > MEM_THRESHOLD:
        logging.warning(f"High Memory usage: {memory}%")
    else:
        logging.info(f"Memory usage: {memory}%")

def check_disk():
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        logging.warning(f"High Disk usage: {disk}%")
    else:
        logging.info(f"Disk usage: {disk}%")

def main():
    logging.info("Running system health check...")
    check_cpu()
    check_memory()
    check_disk()
    logging.info("System health check complete.\n")

if __name__ == "_main_":
    main()      