# N11 Load Testing Project

This project contains a Locust load test script for testing the search functionality of n11.com e-commerce website.

## Overview

The load test simulates user behavior by performing search queries for "iPhone" and validates the responses based on multiple criteria:
- HTTP status code
- Response time
- Presence of expected keywords in the response

## Requirements

- Python 3.9+
- Locust

## Installation

1. Install the required packages: pip install locust

## Configuration

The test script includes the following configurations:
- Wait time between requests: 1-3 seconds
- Maximum acceptable response time: 2000ms
- Custom User-Agent header to simulate browser requests

## Running the Tests

1. Start the Locust server: locust -f locustfile.py


2. Open your browser and navigate to `http://localhost:8089`

3. Configure your test parameters:
   - Number of users
   - Spawn rate
   - Host URL (default is https://www.n11.com)

## Test Validation Criteria

The test performs the following checks:
1. Verifies that the HTTP response status code is 200
2. Confirms the presence of "iphone" keyword in the response
3. Ensures response time is within the defined threshold (2000ms)

## Logging

The script includes logging configuration to track test execution:
- Failures are logged with detailed information
- Warning messages for slow responses
- Success status for passed tests

## Note

This is a sample load testing script. Make sure to comply with the website's terms of service and testing policies before running load tests against production environments.
