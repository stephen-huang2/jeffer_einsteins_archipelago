import csv
import os
from datetime import datetime


RUNS_FILE = "runs.csv"  # Path to the CSV file used to log all completed runs


def initialize_runs_file():
    """Create runs.csv with headers if it doesn't already exist."""
    if not os.path.exists(RUNS_FILE):
        with open(RUNS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Date",
                "Player Name",
                "Playtime (Minutes)",
                "Playtime (Seconds)",
                "Result",
            ])


def log_run(player_name, start_time, end_condition):
    """
    Log a completed run to runs.csv.

    Args:
        player_name:   Name of the player or a player object with a .name attribute.
        start_time:    Datetime object representing when the run started.
        end_condition: How the run ended
                       (e.g. "Game Completed", "Starved to Death", "Riddle Failure", "Quit").
    """
    initialize_runs_file()

    # Calculate elapsed playtime
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    total_seconds = int(elapsed_time.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # Accept either a player object or a plain string for the name
    player_name_str = player_name.name if hasattr(player_name, "name") else player_name

    # Append the run as a new row in the CSV
    with open(RUNS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            end_time.strftime("%Y-%m-%d %H:%M:%S"),
            player_name_str,
            minutes,
            seconds,
            end_condition,
        ])