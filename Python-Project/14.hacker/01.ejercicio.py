import sqlite3
from datetime import timedelta, datetime
from pathlib import Path
from random import randrange
from time import sleep


FILE_NAME = "for_you.txt"

def delay_action():
    n_hour = randrange(1, 3)
    n_minutes = randrange(0, 60)
    total_seconds = (n_hour * 60 + n_minutes) * 60
    print(f"Sleeping for {n_hour}h {n_minutes}m ({total_seconds}s...)")
    sleep(1)

def get_user_desktop():
    user_path = Path.home()
    desktop_path = user_path / "Desktop"

    if not desktop_path.exists():
        print(f"Desk not found in: {desktop_path}")
        return None, None
    else:
        print(f"Desk detected in: {desktop_path}")

    return user_path, desktop_path

def convert_edge_time(edge_time):
    if edge_time:
        return datetime(1601, 1, 1) + timedelta(microseconds=edge_time)
    return  "Unknown"

def get_edge_history(user_path):
    history_path = user_path / ".var/app/com.microsoft.Edge/config/microsoft-edge/Default/History"
    print(f"Looking for history at: {history_path}")

    while True:
        try:
            with sqlite3.connect(history_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT title, last_visit_time, url
                    FROM urls 
                    ORDER BY last_visit_time DESC
                    LIMIT 5
                    """)
                urls = cursor.fetchall()

            return urls
        except sqlite3.Error as e:
            print(f"Error accessing Edge: {e}")
            print("Re-accessing in 30 seconds...\n")
            sleep(5)

def hacker_desktop(desktop_path, urls):
    with open(desktop_path / FILE_NAME, "w") as hacker_file:
        hacker_file.write("hi, I am hacker and I have infiltrated your system")
        print("\nLast sites visited in Edge: ")
        for title, visit_time, url in urls:
            readable_time = convert_edge_time(visit_time)
            hacker_file.write(f"- {title or 'No title'}\n {readable_time}\n {url}\n")

def main():
    delay_action()
    user_path, desktop_path = get_user_desktop()
    if desktop_path is None:
        exit("The desktop is not found. Finishing the program")
    urls = get_edge_history(user_path)
    hacker_desktop(desktop_path, urls)


if __name__ == "__main__":
    main()