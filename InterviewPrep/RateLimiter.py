from datetime import datetime, timedelta
from collections import defaultdict, deque

ACCESSLOGS = [
    "2026-04-13T10:00:01Z auth-service INFO John login success",
    "2026-04-13T10:00:05Z web-service INFO John page load",
    "2026-04-13T10:00:10Z auth-service INFO Terry login success",
    "2026-04-13T10:00:20Z web-service INFO Terry page load",
    "2026-04-13T10:00:25Z web-service INFO Terry page load",
    "2026-04-13T10:01:00Z web-service INFO John page load",
    "2026-04-13T10:01:10Z web-service INFO John page load",
    "2026-04-13T10:01:20Z web-service INFO John page load",
    "2026-04-13T10:02:00Z auth-service INFO Jerry login success",
    "2026-04-13T10:02:10Z web-service INFO Jerry page load",
]

THRESHOLD = 3
WINDOW_SECONDS = 60

def log_parser(log):
    logParts = log.split(" ", 4)
    logTime = datetime.strptime(logParts[0], "%Y-%m-%dT%H:%M:%SZ")
    logService = logParts[1]
    logUser = logParts[3]
    return logTime, logUser

def rate_limiter(logs):
    userActivityDict = defaultdict(deque)
    rateLimitedUsers = set()

    for log in logs:
        curLogTime, curLogUser = log_parser(log)

        userActivityDict[curLogUser].append(curLogTime)
        currentUserActivity = userActivityDict[curLogUser]

        while currentUserActivity and (curLogTime - currentUserActivity[0]) > timedelta(seconds=WINDOW_SECONDS):
            currentUserActivity.popleft()

        if len(currentUserActivity) >= THRESHOLD:
            rateLimitedUsers.add(curLogUser)

    return rateLimitedUsers

if __name__ == "__main__":
    print("Init rate limiter")
    rateLimitedUserList = rate_limiter(ACCESSLOGS)
    print(f"Rate limited users are: {rateLimitedUserList}")