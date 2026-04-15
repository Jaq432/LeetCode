import time

ERROR_RESPONSES = [
    200,
    200,
    300,
    400,
    300,
    500,
    400,
    200,
]

RETRY_COUNT = 3

def request_and_limit_service(response):
    returnResponse = 0
    print(f"Request response: {response}")
    if response != 200 and response != 300:
        for i in range(1,RETRY_COUNT+1):
            print(f"Retrying request. Retry count {i}")
            time.sleep(2**i)
            if returnResponse == "200" or returnResponse == "300":
                break

def request_and_limit_service2(response):
    print(f"Requested and got response {response}")
    
    badResponse = False
    maxRetry = 3
    retryCount = 1

    if response != 200 and response != 300:
        badResponse = True

    while badResponse and retryCount <= maxRetry:
        print(f"Retrying request attempt: {retryCount} in {2**retryCount} seconds")
        time.sleep(2**retryCount)
        retryCount += 1

if __name__ == "__main__":
    for response in ERROR_RESPONSES:
        request_and_limit_service(response)