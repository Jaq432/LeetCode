from collections import defaultdict, deque

LOGS = [
    "2026-04-13T10:00:01Z auth-service INFO User login success",
    "2026-04-13T10:00:05Z payment-service ERROR Failed to process payment",
    "2026-04-13T10:00:10Z auth-service ERROR Token validation failed",
    "2026-04-13T10:00:20Z payment-service ERROR Timeout contacting bank",
    "2026-04-13T10:00:25Z payment-service ERROR Retry failed",
    "2026-04-13T10:01:00Z auth-service ERROR Token validation failed",
    "2026-04-13T10:01:10Z auth-service ERROR Token validation failed",
    "2026-04-13T10:01:20Z auth-service ERROR Token validation failed",
    "2026-04-13T10:02:00Z order-service INFO Order created",
    "2026-04-13T10:02:10Z order-service ERROR Failed to process payment",
    "2026-04-13T10:02:20Z payment-service ERROR Failed to process payment",
    "2026-04-13T10:02:10Z order-service ERROR Failed to process payment",
    "2026-04-13T10:02:10Z order-service ERROR Failed to process payment",
    "2026-04-13T10:02:10Z order-service ERROR Failed to process payment",
    "2026-04-13T10:02:10Z order-service ERROR Failed to process payment",
]

def log_translator(log):
    logParts = log.split(" ", 3)
    logService = logParts[1]
    return logService

def kMostCommon(logs, k):
    logDict = defaultdict(deque)
    kMostCommonServices = []
    for log in logs:
        curLogService = log_translator(log)

        if curLogService in logDict:
            logDict[curLogService] += 1
        else: 
            logDict[curLogService] = 1
    
    # Sort the dict
    sortedLogDict = dict(sorted(logDict.items(), key=lambda x:x[1], reverse=False))

    for i in range(k):
        kMostCommonServices.append(sortedLogDict.popitem())

    return kMostCommonServices

def log_translator2(log):
    parts = log.split(" ", 2)
    logService = parts[1]
    return logService

def kMostCommon2(logs, k):
    itemDict = {}
    for log in logs:
        logService = log_translator(log)
        #print(logService)
        if logService in itemDict.keys():
            itemDict[logService] += 1
        else:
            itemDict[logService] = 1
        
    #print(itemDict)

    sortedItemDict = dict(sorted(itemDict.items(), key=lambda x:x[1], reverse=True))

    #print(sortedItemDict)

    kMostCommonResults = []
    index = 0
    for i in sortedItemDict:
        if index >= k:
            break
        kMostCommonResults.append(i)
        index += 1

    return kMostCommonResults

if __name__ == "__main__":
    mostFrequent = kMostCommon(LOGS,2)
    print(f"Most Frequent Services: {mostFrequent}")
