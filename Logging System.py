from collections import defaultdict, deque
from typing import List, Dict
import re

class LogSystem:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent_logs = deque(maxlen=capacity)
        self.user_logs = defaultdict(list)
        self.level_count = defaultdict(int)

    def add_log(self, line: str) -> None:
        # Extract components using regex
        match = re.match(r'\[(.*?)\] (\w+) (\w+): (.+)', line)
        if match:
            timestamp, level, user_id, message = match.groups()
            log_entry = {
                "timestamp": timestamp,
                "level": level,
                "user_id": user_id,
                "message": message
            }
            # Store in all structures
            self.recent_logs.append(log_entry)
            self.user_logs[user_id].append(log_entry)
            self.level_count[level] += 1

    def get_user_logs(self, user_id: str) -> List[Dict]:
        return self.user_logs.get(user_id, [])

    def count_levels(self) -> Dict[str, int]:
        return dict(self.level_count)

    def filter_logs(self, keyword: str) -> List[Dict]:
        keyword = keyword.lower()
        return [log for log in self.recent_logs if keyword in log["message"].lower()]

    def get_recent_logs(self) -> List[Dict]:
        return list(self.recent_logs)
logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

log_system = LogSystem(capacity=5)

for log in logs:
    log_system.add_log(log)

while (True):
    n=int(input('''Welcome to Logging System:
            type 1 to Fetch logs by Userid
            type 2 to fetch count of levels
            type 3 to fetch filter logs by message
            type 4 to get recent logs
            type 5 to exit'''))
    if n==1:
        uid= input("Enter the user id: ")
        print("\nUser Logs (user1): ", log_system.get_user_logs("user1"))
    elif n==2:
        print("Level Count:", log_system.count_levels())
    elif n==3:
        message=input("Enter the text to be filtered with : ")
        print("Filter Logs (timeout):", log_system.filter_logs(message))
    elif n==4:
        print("Recent Logs:\n", log_system.get_recent_logs())
    elif n==5:
        print("Thank you")
        break
    else:
        print("Enter a valid input")
