import praw
import requests
import webbrowser
import time
import os
import unittest
from printy import printy

username = None
password = None

try:
    minimumprice = int(input("Minimum price: ")[0])
except:
    minimumprice = 200

printy('\nPlease login to your reddit account...\n', 'bB')

authenticated = False

while not authenticated:
    username = input("Username: ")
    password = input("Password: ")
    if username != '' and password != '':
        reddit = praw.Reddit(client_id='SNiG8USK-G6UtQ',
                                client_secret='FZGlEYxDjxc7vUaimCV-OYGdoco',
                                user_agent = 'acturnips bot 0.2',
                                username=username,
                                password=password)
        
        subreddit = reddit.subreddit('acturnips')
        try:
            user = reddit.user.me()
        except:
            #if user doesnt exist
            printy('\nInvalid username or password... Please try again...\n', 'rB')
            authenticated = False
        else: 
            #if user exists
            printy('\nAuthenticated! Good luck!\n', 'nB')
            authenticated = True
    else:
        printy('\nInvalid username or password... Please try again...\n', 'rB')
        authenticated = False

    
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
    price = None
    for i, char in enumerate(first):
        try:
            if int(char) >= minimumprice and int(char) != 9:
                if(split(first)[i-1].isdigit() == False):
                    price = ''
                    price = price.join(split(first)[i:i+3])
                    deal = submissions[0]
        except:
            continue
    if deal != None:
        if(all(x != firstid for x in history)):
            printy(f'\n   Found one! {price} bells per turnip\n', 'nB')
            webbrowser.open(f'https://www.reddit.com/r/acturnips/comments/{firstid}')
            history.append(firstid)

i = 0
while True:
    try:
        getDeal()
    except:
        printy('         Error occured! Reddit might be down...', 'r')
    printy(f'{i}...', 'g')
    time.sleep(.5)
    i += 1


