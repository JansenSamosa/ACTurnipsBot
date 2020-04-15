import praw
import requests
import webbrowser
import time

f = open('credentials.txt', 'r')

username = f.readline()[9:]
password = f.readline()[9:]

try:
    reddit = praw.Reddit(client_id='SNiG8USK-G6UtQ',
                        client_secret='FZGlEYxDjxc7vUaimCV-OYGdoco',
                        user_agent = 'acturnips bot 0.1',
                        username=username,
                        password=password)
 
    subreddit = reddit.subreddit('acturnips')
except:
    print('Error occured! Reddit might be down, or maybe your credentials are incorrect!')

history = []

def split(str):
    return [char for char in str]

def getDeal():
    new_acturnips = subreddit.new()
    submissions = []
    firstid = None
    for i, submission in enumerate(new_acturnips):
        if(i == 0): 
            firstid = submission
        submissions.append(submission.title)
    first = submissions[0]
    deal = None
    for i, char in enumerate(first):
        if char == '5' or char == '6' or char == '7':
            if(split(first)[i-1].isdigit() == False):
                price = "           Price: " + "".join(split(first)[i:i+3]) + " bells"
                print(price)
                deal = submissions[0]
    if deal != None:
        if(all(x != firstid for x in history)):
            webbrowser.open(f'https://www.reddit.com/r/acturnips/comments/{firstid}')
            history.append(firstid)

i = 0
while True:
    try:
        getDeal()
    except:
        print('         Error occured! Reddit might be down, or maybe your credentials are incorrect!')
    print(f'{i}...')
    time.sleep(.5)
    i += 1

