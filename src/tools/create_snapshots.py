from pathlib import Path

snapshot_file = Path("snapshots/current/rbi_snapshot.txt")

if snapshot_file.exists():

    current_text = snapshot_file.read_text(
        encoding="utf-8"
    )

    print("Snapshot Exists")
    print("Characters:", len(current_text))

else:

    print("Snapshot Not Found")