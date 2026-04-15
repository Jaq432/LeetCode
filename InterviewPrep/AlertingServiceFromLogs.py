from collections import defaultdict, deque
from datetime import datetime, timedelta

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
    "2026-04-13T10:02:10Z payment-service ERROR Failed to process payment",
    "2026-04-13T10:02:20Z payment-service ERROR Failed to process payment",
]

THRESHOLD = 3
WINDOW_SECONDS = 60

def logParser(log):
    logPieces = log.split(" ", 3)
    logTimestamp = datetime.strptime(logPieces[0], "%Y-%m-%dT%H:%M:%SZ")
    logService = logPieces[1]
    logStatus = logPieces[2]
    return logTimestamp, logService, logStatus

def detect_error_spikes(logs):
    logData = defaultdict(deque)
    alertingServices = set()

    for log in logs:
        curLogTimestamp, curLogService, curLogStatus = logParser(log)

        if curLogStatus != "ERROR":
            continue

        curLogWindow = logData[curLogService]

        curLogWindow.append(curLogTimestamp)

        # while there's a window and there's results outside the window
        while curLogWindow and (curLogWindow[0] - curLogTimestamp) > timedelta(WINDOW_SECONDS):
            curLogWindow.popleft()

        if len(curLogWindow) >= THRESHOLD:
            alertingServices.add(curLogService)

    return alertingServices


'''
def parse_log(line):
    logParts = line.split(" ",3)
    timestamp = datetime.strptime(logParts, "%Y-%m-%dT%H:%M:%SZ")
    service = logParts[1]
    logType = logParts[2]
    return timestamp, service, logType
'''

# Gets the time, service name, and log type
def parse_log2(line):
    logParts = line.split(" ", 3)
    logTime = datetime.strptime(logParts[0], "%Y-%m-%dT%H:%M:%SZ")
    logService = logParts[1]
    logType = logParts[2]
    return logTime, logService, logType

# Take the list of logs and find out if they are in alarm
def detect_error_spikes2(logs):
    currentLogs = defaultdict(deque)
    alertingServices = set()

    for log in logs:
        curLogTime, curLogService, curLogType = parse_log(log)

        if curLogType != "ERROR":
            continue

        currentWindow = currentLogs[curLogService]
        currentWindow.append(curLogTime)

        while (curLogTime - currentWindow[0]) > timedelta(seconds=WINDOW_SECONDS):
            currentWindow.popleft()

        if len(currentWindow) >= THRESHOLD:
            alertingServices.add(curLogService)

    return alertingServices

# Scan for erroring services
'''
def detect_error_spikes(logs):
    # Create a defaultdict object with deque for popleft functionality
    error_windows = defaultdict(deque)
    # Create an empty set of services that are in alert
    alerts = set()

    # Start parsing logs
    for line in logs:
        # Get time, service name, and log type
        curLogTimestamp, curLogService, curLogLevel = parse_log(line)

        # Skip anything that's not an alert
        if curLogLevel != "ERROR":
            continue

        logItem = error_windows[curLogService]

        # Add current error timestamp
        logItem.append(curLogTimestamp)

        # Remove timestamps older than 60 seconds
        #print(f"Checking if {curLogService} is in alarm...")
        while logItem and (curLogTimestamp - logItem[0]) > timedelta(seconds=WINDOW_SECONDS):
            #print(f"Removing log from {curLogService} for being old...")
            logItem.popleft()

        # Check threshold
        if len(logItem) >= THRESHOLD:
            alerts.add(curLogService)

    return alerts
'''

if __name__ == "__main__":
    result = detect_error_spikes(LOGS)
    print(f"Services with high error rates: {result}")