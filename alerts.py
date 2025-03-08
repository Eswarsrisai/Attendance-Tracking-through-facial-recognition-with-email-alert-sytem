import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Replace with your email and app password
SENDER_EMAIL = ""
PASSWORD = "" # Replace with your app password

# List of all student roll numbers
all_students = {"228w1a5408", "228w1a5428"}  # Add all roll numbers here
# List of present student roll numbers
present_students = {"228w1a5408"}  # Add present roll numbers here

# Find absentees by subtracting present students from all students
absentees = all_students - present_students

# Email message setup
subject = "Absentee Alert"

# Function to create the email body
def create_email_body(roll_no):
    date_today = datetime.now().strftime("%Y-%m-%d")  # Gets the current date
    return (
        f"Dear Student,\n\n"
        f"You have been marked absent today ({date_today}).\n"
        f"Roll Number: {roll_no}\n\n"
        "Please report to the concerned department if there's an error.\n\n"
        "Best regards,\n"
        "Academic Department"
    )

# Function to send email
def send_email(to_email, body):
    try:
        # Create a MIME object
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable security
            server.login(SENDER_EMAIL, PASSWORD)  # Login with sender email and password
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Send email to each absentee with a personalized message
for roll_no in absentees:
    to_email = f"{roll_no}@vrsec.ac.in"  # Generate email for absentee
    body = create_email_body(roll_no)     # Create personalized email body
    send_email(to_email, body)            # Send the email
