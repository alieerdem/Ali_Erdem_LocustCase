from locust import HttpUser, task, between
import logging

logging.basicConfig(level=logging.INFO)

class N11User(HttpUser):
    wait_time = between(1, 3)
    host = "https://www.n11.com"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    MAX_RESPONSE_TIME_MS = 2000  # Set a maximum acceptable response time in milliseconds

    @task
    def search_iphone(self):
        with self.client.get("/arama?q=iphone", headers=self.headers, catch_response=True) as response:
            # Basic status code check
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
                return

            # Keyword check
            if "iphone" not in response.text.lower():
                logging.warning(f"FAILED: Keyword not found in {response.url}")
                return

            # Response time check
            if response.elapsed.total_seconds() * 1000 > self.MAX_RESPONSE_TIME_MS:
                logging.warning(f"FAILED: Slow response {response.elapsed.total_seconds()*1000:.2f} ms")
                return

            # All checks passed
            response.success()
