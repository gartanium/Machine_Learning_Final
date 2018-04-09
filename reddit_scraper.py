import json, requests
import praw
from praw.models import MoreComments
import pickle
import urllib

reddit = praw.Reddit(client_id='Fn7V-T4nmOdYrw',
                     client_secret='xmRaNM8itwOty-_kBx_5dWBtetE',
                     password='looploop',
                     user_agent='testscript by /u/fakebot3',
                     username='waldo1478')

print(reddit.user.me())
subreddits = ['askreddit', 'worldnews', 'videos', 'funny', 'todayilearned', 'pics', 'gaming']
# subreddits = ['askreddit', 'worldnews', 'videos', 'funny', 'todayilearned', 'pics', 'gaming', 'movies', 'news', 'gifs', 'midlyinteresting', 'aww', 'showerthoughts', 'television', 'jokes', 'science', 'oldschoolcool', 'sports', 'iama']
# subreddits['funny', 'DIY', 'pics', 'gaming', 'upliftingnews', 'sports', 'dataisbeautiful', 'aww', 'tifu']

# submissions = reddit.subreddit('learnpython').top(limit=5)
#
# submission = reddit.submission(url='https://www.reddit.com/r/redditdev/comments/4a7oh0/beginner_trying_to_pull_my_comments_via_api/')

# for top_level_comment in submission.comments:
#     print(top_level_comment.body + '\n')

filename = 'finalized_model.sav'
clf = pickle.load(open(filename, 'rb'))

for subreddit in subreddits:
    submissions = reddit.subreddit(subreddit).top(limit=5)
    print('---------------------------------------------')
    print(subreddit)
    for submission in submissions:
        print('---------------------------------------------')
        i = 0;
        print('Title: ' + submission.title + '\n')
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            print i, ')', clf.predict([top_level_comment.body]), ':', top_level_comment.body
            i += 1

# subreddit = 'learnpython'
#
# r = requests.get(
#     'http://www.reddit.com/r/{}.json'.format(subreddit),
#     headers={'user-agent': 'Mozilla/5.0'}
# )
#
# print(json.dumps(r.json(), indent=4))
#
# view structure of an individual post
# print(json.dumps(r.json()['data']['children'][0]))
#
# for post in r.json()['data']['children']:
#     print(post['data']['url'])
    # r2 = requests.get(
    #     post['data']['url'],
    #     headers={'user-agent': 'Mozilla/5.0'}
    # )
    # r2 = requests.get(post['data']['url'] + '.json?limit=1')
    #
    # print(json.dumps(r2.json(), indent=4))
    # print(json.dumps(r2.json(), indent=4))
    # for comment in r2.json()['data']['children']:
    # comments = post
    # op = post.pop(0)
    #
    # for comment in comments:
    #     for reply in comment['data']['children']:
    #         print(reply['data']['author'])
    #         print(reply['data']['body'])

# comments = r.json()
# op = comments.pop(0)
#
# for comment in comments:
#     for reply in comment['data']['children']:
#         print(reply['data']['author'])
#         print(reply['data']['body'])