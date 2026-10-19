import statistics

# Part 1: Store your scores
# Scores from recent meets 
meets = [
    "2024 US Champs D1",
    "2024 US Champs D2",
    "2025 Dev Nats D1",
    "2025 Dev Nats D2",
    "2025 US Champs D1",
    "2025 US Champs D2",
    "2026 Dev Nats D1",
    "2026 Dev Nats D2",
    "2026 Jr Pan Ams",
]
 
scores = {
    "Floor":         [12.500, 13.050, 12.450, 13.700, 12.200, 13.200, 11.750, 12.000, 11.000],
    "Pommel Horse":  [13.050, 12.750, 13.500, 13.000, 12.650, 13.250, 14.100, 13.200, 13.100],
    "Rings":         [11.800, 12.600, 12.200, 11.850, 11.350, 10.400, 12.450, 12.200, 11.866],
    "Vault":         [13.650, 13.500, 14.000, 13.850, 13.750, 13.950, 13.700, 13.750, 13.433],
    "Parallel Bars": [12.400, 13.200, 12.950, 13.300, 11.550, 12.600, 13.600, 13.950, 11.466],
    "High Bar":      [12.950, 12.750, 9.450, 12.700, 12.850, 12.750, 13.100, 12.350, 11.733],
}

# Part 2: Average for each event
print("=== Event Averages ===")
averages = {}
for event, event_scores in scores.items():
    avg = statistics.mean(event_scores)
    averages[event] = avg
    print(f"{event}: {avg:.2f}")

# Part 3: Best event
best_event = max(averages, key=averages.get)
print(f"\nBest event: {best_event} ({averages[best_event]:.2f})")

# Part 4: Most consistent event (scores vary the least)
consistency = {event: statistics.stdev(s) for event, s in scores.items()}
most_consistent = min(consistency, key=consistency.get)
print(f"Most consistent event: {most_consistent}")