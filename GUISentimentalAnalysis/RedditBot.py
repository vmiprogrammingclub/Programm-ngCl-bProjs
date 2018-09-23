import praw
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                   client_id='********', client_secret="*******",
                     username='*****', password='*****')

#submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')



all = reddit.subreddit("technology")

for i in all.search("intel", limit=5):
    link = "https://www.reddit.com"
    link += i.permalink
    print(link)
    submission = reddit.submission(url=link)
    for top_level_comment in submission.comments:
        string = top_level_comment.body

        string.encode('utf-8')
        print(top_level_comment.body)