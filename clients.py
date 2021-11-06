import praw
import random
from linereader import copen
import warnings

class RedditClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id="KI3xrA2NAM7JmwoSq5pTUg",
            client_secret="mbnSdxDFvmzNmUUZzxflyFgktzkX7Q",
            user_agent="BaumBot",
            check_for_async=False #yeah fuck you
        )
        self.max_responses = 20

    def get_random_subreddit(self, count, sort='top_all', onlyNSFW=False):
        count = self._check_max_count(count)
        sort = self._get_sort_string(sort)
        subreddit = self.reddit.subreddit('all').new()

        result = ""
        for i in range(0, count):
            #yield next element if it is not sticky
            if onlyNSFW:
                submission = next(x for x in subreddit if not x.stickied and x.subreddit.over18)
            else:
                submission = next(x for x in subreddit if not x.stickied)
            result += '<https://www.reddit.com/r/' + str(submission.subreddit) + sort + '>\n'
        result = self._check_answer(result)
        return result

    def get_random_post(self, count=1):
        count = self._check_max_count(count)
        #TODO

    def get_memes_of_the_day(self, count=1):
        _count = self._check_max_count(count)
        #TODO

    def _check_max_count(self, count):
        count = int(count)
        if count < 1:
            return 1
        if count > self.max_responses:
            return self.max_responses
        return count

    def _get_sort_string(self, filter):
        sorts = {
            'hot': '/',
            'new': '/new',
            'top_hour': '/top/?t=hour',
            'top_day': '/top/?t=day',
            'top_month': '/top/?t=month',
            'top_year': '/top/?t=year',
            'top_all': '/top/?t=all',
        }
        if filter in sorts:
            return sorts[filter]
        return None

    def _check_answer(self, text):
        if text == "" or text == None:
            self._restart_in_error_case()
            return "Error"
        return text

    def _restart_in_error_case(self):
        self.reddit = asyncpraw.Reddit(
            client_id="KI3xrA2NAM7JmwoSq5pTUg",
            client_secret="mbnSdxDFvmzNmUUZzxflyFgktzkX7Q",
            user_agent="BaumBot",
        )

    def _add_to_porn_subreddits(self, subreddit):
        subreddit = str(subreddit)
        file = open('documents/pornsubreddits.txt', 'r')
        lines = file.readlines()

        for line in lines:
            if line.split('\n')[0] == subreddit:
                return

        file.close()
        file = open('documents/pornsubreddits.txt', 'a')
        file.write(subreddit + '\n')
        file.close()
        print("New: ", subreddit)

class PornClient:
    def __init__(self):
        pass

class MusicClient:
    def __init__(self):
        pass

class RadioClient:
    def __init__(self, genre):
        pass