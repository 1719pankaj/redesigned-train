#!/usr/bin/env python3
import os
import threading
import multiprocessing
import time
import requests
import math
import psutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def format_speed(bytes_per_sec):
    return f"{(bytes_per_sec * 8) / 1_000_000:.2f} Mbps"

def log_stats(upload_speed, download_speed):
    log_path = Path.home() / 'network.log'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu_usage = psutil.cpu_percent(interval=1)
    log_entry = f"[{timestamp}] CPU: {cpu_usage}% | ↑ {format_speed(upload_speed)} | ↓ {format_speed(download_speed)}\n"
    
    with open(log_path, 'a') as f:
        f.write(log_entry)

def monitor_network():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    time_start = time.time()
    last_log = time.time()

    while True:
        time.sleep(1)
        net_io = psutil.net_io_counters()
        new_bytes_sent = net_io.bytes_sent
        new_bytes_recv = net_io.bytes_recv
        current_time = time.time()

        upload_speed = (new_bytes_sent - bytes_sent) / (current_time - time_start)
        download_speed = (new_bytes_recv - bytes_recv) / (current_time - time_start)

        # Console output
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ↑ {format_speed(upload_speed)} | ↓ {format_speed(download_speed)}")

        # Log every 15 minutes
        if current_time - last_log >= 900:  # 900 seconds = 15 minutes
            log_stats(upload_speed, download_speed)
            last_log = current_time

        bytes_sent = new_bytes_sent
        bytes_recv = new_bytes_recv
        time_start = current_time

# Rest of the code remains the same...
def network_load():
    servers = [
        'http://speedtest.ftp.otenet.gr/files/test100Mb.db',
        'http://speedtest.tele2.net/100MB.zip',
        'http://speedtest-ny.turnkeyinternet.net/100mb.bin',
        'http://speedtest.bologna.it.net/files/100mb.bin'
    ]
    
    while True:
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for url in servers:
                futures.append(executor.submit(download_file, url))

def download_file(url):
    try:
        response = requests.get(url, stream=True)
        chunk_size = 1024 * 1024  # 1MB chunks
        for _ in response.iter_content(chunk_size=chunk_size):
            pass
    except:
        time.sleep(0.1)

def cpu_intensive_task():
    while True:
        x = 0
        for i in range(10**7):
            x += math.sqrt(i)

def main():
    os.nice(19)
    
    monitor_thread = threading.Thread(target=monitor_network)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    cpu_count = multiprocessing.cpu_count()
    cpu_threads = [threading.Thread(target=cpu_intensive_task) for _ in range(cpu_count)]
    net_threads = [threading.Thread(target=network_load) for _ in range(3)]
    
    for t in cpu_threads + net_threads:
        t.daemon = True
        t.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")

if __name__ == "__main__":
    main()
