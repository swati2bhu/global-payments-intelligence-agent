from pathlib import Path


def detect_changes():

    current_file = Path(
        "snapshots/current/rbi_snapshot.txt"
    )

    previous_file = Path(
        "snapshots/history/rbi_snapshot.txt"
    )

    if not previous_file.exists():

        return False

    current_text = current_file.read_text(
        encoding="utf-8"
    )

    previous_text = previous_file.read_text(
        encoding="utf-8"
    )

    return current_text != previous_text
