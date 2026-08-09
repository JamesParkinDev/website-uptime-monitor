import requests
import time
import datetime

def main() -> None:

    # TODO: Store urls in external txt file

    urls = ["https://www.google.com",
            "https://www.yahoo.com",
            "https://www.microsoft.com",
            "https://www.wikipedia.org",
            "https://www.youtube.com/",
            "https://www.foo.bar"
            ]

    for url in urls:
        try:
            # measure response time in nanoseconds and convert to milliseconds
            start = time.perf_counter_ns()
            response = requests.get(url, timeout=10)
            end = time.perf_counter_ns()
            time_elapsed = (end - start)/1_000_000

            if response.status_code == 200:
                # print(f"{url} is online! ({time_elapsed}ms)")
                status = "UP"
            elif response.status_code == 403:
                # print(f"{url} is online, but you are forbidden! ({time_elapsed}ms)")
                status = "UP"
            elif response.status_code == 429:
                # print(f"{url} is online! However, too many requests are being sent ({time_elapsed}ms)")
                status = "UP"
            elif 400 <= response.status_code < 500:
                # print(f"{url} experienced a client error. ({time_elapsed}ms)")
                status = "UP"
            elif 500 <= response.status_code < 600:
                # print(f"{url} experienced a server error. ({time_elapsed}ms)")
                status = "UP"
            else:
                # print(f"{url} may be offline. ({time_elapsed}ms)")
                status = "DOWN"

            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} | {url} | {status} | {time_elapsed:.2f}ms")

        except requests.ConnectionError:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} | {url} | DOWN | CONNECTION ERROR")

        except requests.Timeout:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} | {url} | DOWN | TIMEOUT")

if __name__ == '__main__':
    main()
