import sys
import praw 
import time
import urllib
import random


'''-------------------------------------------------------- Reddit API setup -----------------------------------------------------------------------------'''

reddit_p = praw.Reddit(client_id='Enter Here',
						client_secret='Enter Here',
						user_agent='Enter Here')

sr_memes = reddit_p.subreddit('memes')
sr_dankmemes = reddit_p.subreddit('dankmemes')
sr_bpt = reddit_p.subreddit('blackpeopletwitter')
sr_funny = reddit_p.subreddit('funny')

'''------------------------------------------------------- Variables used for checking or lists -----------------------------------------------------------------------------'''

bpt_urls = []
dankmemes_urls = []
meme_urls = []
funny_urls = []

'''------------------------------------------------------ Loop that indexes urls to lists -------------------------------------------------------------------------------'''

for submission_bpt in sr_bpt.hot(limit=15):
	if('.jpg' in submission_bpt.url and 'redd' in submission_bpt.url):
		temp = [submission_bpt.title , submission_bpt.url]
		bpt_urls.append(temp)
	else:
		continue

for submission_meme in sr_memes.hot(limit=15):
	if('.jpg' in submission_meme.url and 'redd' in submission_meme.url):
		temp = [submission_meme.title , submission_meme.url]
		meme_urls.append( temp)

	else:
		continue

for submission_dankmeme in sr_dankmemes.hot(limit=10):
	if('.jpg' in submission_dankmeme.url and 'redd' in submission_dankmeme.url):
		temp = [submission_dankmeme.title , submission_dankmeme.url]
		dankmemes_urls.append(temp)
	else:
		continue

for submission_funny in sr_funny.hot(limit=10):
	if('.jpg' in submission_funny.url and 'redd' in submission_funny.url):
		temp = [submission_funny.title,submission_funny.url]
		funny_urls.append(temp)
	else:
		continue		

'''----------------------------------------------------------- Loop that iterates through each url and saves them --------------------------------------------------------------------------'''
print("Starting Download from r/meme.........")
for i_meme, image_meme in enumerate(meme_urls, start=1):
	print("Downloading meme "+str(i_meme))
	urllib.request.urlretrieve(image_meme[1],str(image_meme[0])+".jpg")
	time.sleep(2.5)
print("Completed Download from r/meme...")
time.sleep(5)


print("Starting Download from r/blackpeopletwitter.........")
for i_bpt, image_bpt in enumerate(bpt_urls, start=1):
	print("Downloading meme "+str(i_bpt))
	urllib.request.urlretrieve(image_bpt[1], str(image_bpt[0])+".jpg")
	time.sleep(2.5)
print("Completed Download from r/blackpeopletwitter...")
time.sleep(5)


print("Starting Download from r/dankmemes.........")
for i_dankmeme, image_dankmeme in enumerate(dankmemes_urls, start=1):
	print("Downloading meme "+str(i_dankmeme))
	urllib.request.urlretrieve(image_dankmeme[1], str(image_dankmeme[0])+".jpg")
	time.sleep(3)
print("Completed Download from r/dankmemes...")


print("Starting Download from r/funny.........")
for i_funny, image_funny in enumerate(funny_urls, start=1):
	print("Downloading meme "+str(i_funny))
	urllib.request.urlretrieve(image_funny[1], str(image_funny[0])+".jpg")
	time.sleep(3)
print("Completed Download from r/funny...")

print("Completed All Downloads")