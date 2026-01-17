import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_date = datetime(2025, 9, 1)
end_date = datetime(2026, 1, 1)

data = []
current_date = start_date

while current_date <= end_date:
    weekday = current_date.weekday()  

    # focus hours (less on weekends)
    if weekday < 5:
        focus_hours = np.random.normal(5, 1)
    else:
        focus_hours = np.random.normal(3, 1)

    focus_hours = round(max(1, min(focus_hours, 8)), 1)

    # breaks
    break_minutes = int(np.random.normal(90, 25))
    break_minutes = max(30, min(break_minutes, 180))

    # deep work sessions depend on focus
    deep_work_sessions = max(1, min(int(focus_hours), 5))

    # screen time (more on weekends)
    if weekday < 5:
        screen_time = np.random.normal(3, 1)
    else:
        screen_time = np.random.normal(5, 1)

    screen_time = round(max(1, min(screen_time, 9)), 1)

    # sleep hours
    sleep_hours = round(max(4, min(np.random.normal(7, 1), 9)), 1)

    # mood score
    mood_score = round(max(1, min(np.random.normal(6, 1.5), 10)), 1)

    # productivity score
    productivity_score = (
        focus_hours * 1.2 +
        deep_work_sessions * 0.4 +
        sleep_hours * 0.3 -
        screen_time * 0.5
    )

    productivity_score = round(max(3, min(productivity_score, 9)), 1)

    data.append([
        current_date.strftime("%Y-%m-%d"),
        focus_hours,
        break_minutes,
        deep_work_sessions,
        screen_time,
        sleep_hours,
        mood_score,
        productivity_score
    ])

    current_date += timedelta(days=1)

columns = [
    "date",
    "focus_hours",
    "break_minutes",
    "deep_work_sessions",
    "screen_time_hours",
    "sleep_hours",
    "mood_score",
    "productivity_score"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("data/productivity_log.csv", index=False)

print("Dataset created with rows:", len(df))
