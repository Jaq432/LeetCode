import time

ERROR_RESPONSES = {
    200,
    200,
    300,
    400,
    300,
    500,
    400,
    200,
}

def request_and_limit_service(response):
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