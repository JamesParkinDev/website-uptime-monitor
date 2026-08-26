import requests
import time

# Simulated Database
userdata = {"Alice":{"urls": ["https://github.com/JamesParkinDev", "https://www.youtube.com/watch?v=rvFsGRvj9jo"]},
            "Bob":{"urls": ["https://github.com/JamesParkinDev", "https://www.youtube.com/watch?v=rvFsGRvj9jo"]},
            "Charlie":{"urls": ["https://github.com/JamesParkinDev", "https://www.youtube.com/watch?v=rvFsGRvj9jo"]}}

def monitor(user: str):
    uptime_info = {}
    for url in userdata[user]["urls"]:
        uptime_info[url] = check_url(url)
    return uptime_info

def check_url(url):
    website_info = {"url": url, "status": "DOWN", "status_code": None, "response_time_ms": None, "error": None}
    try:
        # measure response time in nanoseconds and convert to milliseconds
        start = time.perf_counter_ns()
        response = requests.get(url, timeout=10)
        end = time.perf_counter_ns()
        time_elapsed_ms = (end - start) / 1_000_000

        website_info['status_code'] = response.status_code
        website_info['response_time_ms'] = time_elapsed_ms

        website_info["status"] = "UP"

    except requests.ConnectionError:
        website_info["status"] = "DOWN"
        website_info["error"] = "CONNECTION ERROR"

    except requests.Timeout:
        website_info["status"] = "DOWN"
        website_info["error"] = "TIMEOUT"

    return website_info
