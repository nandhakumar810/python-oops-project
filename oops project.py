

#                                                                  STUDY HABIT TRACKER SYSTEM

class StudySession:

    def __init__(self, subject, duration, date):
        self.subject = subject
        self.duration = duration
        self.date = date

    def display(self):
        print(f" Date: {self.date}, Subject: {self.subject}, Duration: {self.duration} hours")





class StudyTracker:

    def __init__(self):
        self.sessions = []

    def add_session(self, subject, duration, date):
        session = StudySession(subject, duration, date)
        self.sessions.append(session)
        print("Study session added!")

    def show_sessions(self):
        if not self.sessions:
            print("No study sessions recorded.")
        else:
            print("Study History:")
            for session in self.sessions:
                session.display()

    def total_study_time(self):
        total = 0
        for session in self.sessions:
            total += session.duration
        print(f" Total Study Time: {total} hours")




tracker = StudyTracker()

while True:

    print(" Study Habit Tracker")
    print("1. Add Study Session")
    print("2. Show Study Sessions")
    print("3. Show Total Study Time")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Enter subject: ")
        duration = float(input("Enter study duration (hours): "))
        date = input("Enter date (DD-MM-YYYY): ")
        tracker.add_session(subject, duration, date)

    elif choice == "2":
        tracker.show_sessions()

    elif choice == "3":
        tracker.total_study_time()

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice")
