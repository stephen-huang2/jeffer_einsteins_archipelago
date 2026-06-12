import csv
import os
from datetime import datetime

RUNS_FILE = "runs.csv"


def initialize_runs_file():
    """Create runs.csv with headers if it doesn't exist."""
    if not os.path.exists(RUNS_FILE):
        with open(RUNS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Player Name",
                             "Playtime (Minutes)",
                             "Playtime (Seconds)",
                             "Result"])


def log_run(player_name, start_time, end_condition):
    """
    Log a completed run to runs.csv.

    Args:
        player_name: Name of the player or player object
        start_time: Start time (datetime object)
        end_condition: How the run ended
        (e.g., "Game Completed", "Starved to Death", "Riddle Failure", "Quit")
    """
    initialize_runs_file()

    end_time = datetime.now()
    elapsed_time = end_time - start_time

    total_seconds = int(elapsed_time.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    player_name_str = player_name.name if hasattr(player_name,
                                                  "name") else player_name

    with open(RUNS_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            end_time.strftime("%Y-%m-%d %H:%M:%S"),
            player_name_str,
            minutes,
            seconds,
            end_condition
        ])
