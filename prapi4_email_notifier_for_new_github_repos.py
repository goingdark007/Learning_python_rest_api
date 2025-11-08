import requests
import json
import smtplib
from email.mime.text import MIMEText
from dotenv import dotenv_values

username = 'goingdark007'

url = f'https://api.github.com/users/{username}/repos'

response = requests.get(url)

data = response.json()

repositories = []

for repo in data:

    repositories.append(repo['name'])

def save_repo_list(repos, file_name= 'repos.json'):

    with open(file_name, 'w') as f:
        json.dump(repos, f)

def load_repo_list(file_name= 'repos.json'):

    try:

        with open(file_name, 'r') as f:
            return json.load(f)

    except FileNotFoundError:

        print('File not found')

        return []

def send_email(new_repositories):

    config = dotenv_values('.env')

    sender = config['GMAIL_ADDRESS']
    receiver = 'nhasanr18@gmail.com'
    # We need to enable 2 FA to create a gmail app password (not main pass)
    # Don't hard code it in the code use .env file
    password = config['GMAIL_APP_PW']

    subject = 'New Github Repositories Found!'
    body = 'New repos:\n' + '\n'.join(new_repositories)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)

            print('Email sent!')

    except smtplib.SMTPAuthenticationError:
        print('Authentication failed! Check your app pass or gmail security settings')

    except Exception as e:
        print(f'Error: {e}')

old_repos = set(load_repo_list())

current_repos = set(repositories)

new_repos = current_repos - old_repos

if  new_repos != set():

    send_email(new_repos)

else:

    print('no new repo added')