import json
from collections import Counter
from pathlib import Path
from datetime import datetime, timedelta

log_file = Path.home() / "cowrie/var/log/cowrie/cowrie.json"

events = Counter()
commands = Counter()
usernames = Counter()
failed_logins = Counter()
failed_login_times = {}

with open(log_file, "r") as file:
	for line in file:
		try:
		 event = json.loads(line)
		except json.JSONDecodeError:
		 continue
		event_type = event.get("eventid","")
		events[event_type] += 1
		
		if event_type == "cowrie.command.input":
		 commands[event.get("input", "unknown")] += 1

		if event_type.startswith("cowrie.login."):
		 usernames[event.get("username", "unknown")] += 1
		if event_type == "cowrie.login.failed":
		 source_ip = event.get("src_ip", "unknown")
		 failed_logins[source_ip] += 1
		 timestamp = event.get("timestamp", None)
		 if timestamp is not None: 
		 	login_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
		 	failed_login_times.setdefault(source_ip, []).append(login_time)
print("\n===== COWRIE SECURITY REPORT =====")

print("\nSecurity Events:")
for event, count in events.most_common():
	print(f"{event}: {count}")

print("\nAttempted Usernames:")
for username, count in usernames.most_common():
	print(f"{username}: {count}")

print("\nCommands Executed:")
for command, count in commands.most_common():
	print(f"{command}: {count}")
print ("\n===== SECURITY ALERTS =====")

for ip, times in failed_login_times.items():
	times.sort()

	for i in range(len(times) - 4):
	 difference = times[i + 4] - times[i]

	 if difference <= timedelta(seconds=60):
	 	print(f"[ALERT] Possible brute force activity from {ip}")
	 	print("5 failed logins detected within 60 seconds")
	 	break
	
print("\n====================")
