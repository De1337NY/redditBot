import os
import praw
import lists

# only one stream will run concurrently so desired one needs to be uncommented before run time

r = praw.Reddit(client_id=os.environ['ID'],
                client_secret=os.environ['secret'],
                user_agent=os.environ['useragent'],
                username=os.environ['username'],
                password=os.environ['password'])
sub = r.subreddit('test')
print('I have risen.')

while True:
    # reads all new comments looking for any words in lists.searchtext and shows data on the post
    for comment in sub.stream.comments():
        for phrase in lists.searchtext:
            if phrase.lower() in comment.body.lower():
                link = str(comment.link_id)
                submission = r.submission(link[3:])
                print("Title: ", submission.title)
                print("Text: ", submission.selftext)
                print("Subreddit: ", submission.subreddit)
                print("Score: ", submission.score)
                print("---------------------------------\n")
"""
  # reads all new post titles for words in lists.searchtext and shows data on the post
  for submission in sub.stream.submissions():
      if lists. searchText.lower() in submission.title.lower():
          print("Title: ", submission.title)
          print("Text: ", submission.selftext)
          print("Subreddit: ", submission.subreddit)
          print("Score: ", submission.score)
          print("---------------------------------\n")
"""
"""
  # reads all new comments and upon finding "Mousepad" in comment will reply "Militia" 
  for comment in sub.stream.comments(skip_existing=True):
    try:
      if "Mousepad" in comment.body: # 
        comment.reply("Militia") 
        print('replying')
    except praw.exceptions.APIException:
      print("probably a rate limit...")
"""
