logs = [
"INFO request started",
"ERROR disk full",
"INFO request finished",
"ERROR disk full",
"ERROR timeout",
"INFO health check",
"ERROR timeout"
]

logCounts = {}

for log in logs:
    if "ERROR" in log:
        if log not in logCounts:
            logCounts[log] = 1
            continue
        logCounts[log] = logCounts[log] + 1

sortedLogCounts = dict(sorted(logCounts.items(), key=lambda x:x[1], reverse=True))

print(logCounts)
print(sortedLogCounts)