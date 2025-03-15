# Locust Load Testing Project

A load testing project using Locust to simulate user behavior for a banking application.

## Test Scenarios

1. User Login
2. Money Transfer
3. User Logout

## Running Tests

To run the load tests:

```bash
locust -f banking_test.py --host=http://yourbankingapp.com --users 1000 --spawn-rate 100
```

## Test Files

- `banking_test.py` - Main load testing scenarios
- `test_singleuser.py` - Single user test implementation
