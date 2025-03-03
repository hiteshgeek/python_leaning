import smtplib
import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent  # Go up one level

# Load the .env file from the parent directory
load_dotenv(BASE_DIR / ".env")

# Now you can access the environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
APP_PASSWORD = os.getenv("APP_PASSWORD")

try:
    # Connect to Gmail's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
        connection.login(user=EMAIL_ADDRESS, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs="hbvaghela83@gmail.com",
            msg="Subject:Test Mail\n\nThis is a test email sent using Python."
        )
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")