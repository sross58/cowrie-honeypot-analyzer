from datetime import datetime, timedelta

times = [
	datetime(2026, 11, 3, 12, 0, 0),
	datetime(2026, 11, 3, 12, 0, 10),
	datetime(2026, 11, 3, 12, 0, 20),
	datetime(2026, 11, 3, 12, 0, 30),
	datetime(2026, 11, 3, 12, 0, 45)
]

times.sort()
detected = False

for i in range(len(times) - 4):
	difference = times[i + 4] - times[i]
	
	if difference <= timedelta(seconds=60):
	 detected = True
	 break
if detected: 
	print("[ALERT] Possible brute force activity")
else:
	print("[OK] No brute force activity detected")
