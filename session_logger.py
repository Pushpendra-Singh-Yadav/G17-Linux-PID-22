import datetime
import os

# File to store session logs
LOG_FILE = "session_log.txt"

def log_session(username, login_time, logout_time):
    """Log a user session to the file."""
    duration = logout_time - login_time
    duration_minutes = duration.total_seconds() / 60
    
    log_entry = (
        f"Username: {username}\n"
        f"Login Time: {login_time}\n"
        f"Logout Time: {logout_time}\n"
        f"Duration: {duration_minutes:.2f} minutes\n"
        "------------------------\n"
    )
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry)
    print("Session logged successfully!")

def view_logs():
    """Display all session logs."""
    if not os.path.exists(LOG_FILE):
        print("No logs found!")
        return
    
    with open(LOG_FILE, "r") as file:
        logs = file.read()
        if logs.strip():
            print("\n=== Session Logs ===")
            print(logs)
        else:
            print("No logs found!")

def main():
    """Main menu-driven program."""
    while True:
        print("\n=== User Session Logger ===")
        print("1. Log a new session")
        print("2. View session logs")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            # Get session details
            username = input("Enter username: ")
            try:
                login_time_str = input("Enter login time (YYYY-MM-DD HH:MM:SS): ")
                logout_time_str = input("Enter logout time (YYYY-MM-DD HH:MM:SS): ")
                
                # Convert strings to datetime objects
                login_time = datetime.datetime.strptime(login_time_str, "%Y-%m-%d %H:%M:%S")
                logout_time = datetime.datetime.strptime(logout_time_str, "%Y-%m-%d %H:%M:%S")
                
                if logout_time <= login_time:
                    print("Error: Logout time must be after login time!")
                else:
                    log_session(username, login_time, logout_time)
            except ValueError:
                print("Error: Invalid date format! Use YYYY-MM-DD HH:MM:SS")
        
        elif choice == "2":
            view_logs()
        
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
