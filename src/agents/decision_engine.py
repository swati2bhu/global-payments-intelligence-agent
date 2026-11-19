from detect_changes import detect_changes

change_detected = detect_changes()

print("\nDECISION ENGINE\n")

if change_detected:

    print("Changes detected.")
    print("Action Required.")
    print("Generate Summary.")
    print("Send Alert.")

else:

    print("No changes detected.")
    print("No action required.")
