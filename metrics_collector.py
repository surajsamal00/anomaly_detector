import psutil
import GPUtil
import requests
import time
import socket

# Your DRF API endpoint
API_URL = "http://localhost:8000/api/metrics/"

def get_metrics():
    host = socket.gethostname()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    gpus = GPUtil.getGPUs()
    gpu = gpus[0].load * 100 if gpus else None  # make sure it's nullable

    return {
        "host": host,
        "cpu_usage": cpu,
        "ram_usage": memory,
        "disk_usage": disk,
        "gpu_usage": gpu
    }

def send_metrics():
    while True:
        data = get_metrics()
        try:
            response = requests.post(API_URL, json=data)
            print(f"[{response.status_code}] → {response.text}")
        except Exception as e:
            print("❌ Error sending metrics:", e)
        time.sleep(10)  # Wait 10 seconds

if __name__ == "__main__":
    send_metrics()
