from dotenv import load_dotenv, dotenv_values
import os

# Load variables from .env file
load_dotenv()

config = dotenv_values('.env')

email_config = config['GMAIL_ADDRESS']

print(email_config)

# Get values
email = os.getenv("GMAIL_ADDRESS")
password = os.getenv("GMAIL_APP_PW")

print("Email:", password)
# print("Password:", password)  # avoid printing secrets