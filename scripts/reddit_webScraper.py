'''
	This script was used to scrape reddit data using Praw library in python.
	After scraping data this script saves the data in a csv file for further processing.

'''
import praw
from praw.models import MoreComments
import pandas as pd


#OAuth with reddit API.
reddit = praw.Reddit(client_id = "0hliVZBlDhlipQ",client_secret = "pjUJDMMXhYaEmyJaLkQYb_2Fccg",user_agent = "Reddit Flair Detector",username = "chandan21121998",password = "Chandan@1234")
#Subreddit of which data is to be scraped.
subreddit = reddit.subreddit('india')


#List of all the flairs. These will be the keys in classification.
flairs = ["AskIndia", "Non-Political", "[R]eddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]

#List of associated data for all posts.
topics_dict = {"title":[],"score":[],"id":[],"url":[],"comms_num":[],"created":[],"body":[],"author":[],"flair":[],"comment":[],"authors":[]}

for flair in flairs:
	'''
		The posts' data is collected by searching by the flair name in the list. Top 100 posts are recorded and stored for analysis.
	'''
	relevant_subreddits = subreddit.search(f"flair_name:{flair}",limit=100)

	for submission in relevant_subreddits:
		topics_dict["title"].append(submission.title)
		topics_dict["score"].append(submission.score)
		topics_dict["id"].append(submission.id)
		topics_dict["url"].append(submission.url)
		topics_dict["comms_num"].append(submission.num_comments)
		topics_dict["created"].append(submission.created)
		topics_dict["body"].append(submission.selftext)
		topics_dict["author"].append(submission.author)
		topics_dict["flair"].append(flair)	



		'''
			Only top ten comments and their authors are considered. The comments are not threads but the main
			ones.
		'''
		submission.comments.replace_more(limit=None)
		comment = ''
		authors = ''
		count = 0
		for top_level_comment in submission.comments:
		 	comment = comment + ' ' + top_level_comment.body
		 	authors = authors + ' ' + str(top_level_comment.author)
		 	count+=1     
		 	if(count > 10):
		 		#print(count)
		 		break
		
		topics_dict["comment"].append(comment)
		topics_dict["authors"].append(authors)

#Saving the file

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('reddit-india-data-sample.csv', index=False)
