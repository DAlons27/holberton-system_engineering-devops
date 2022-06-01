#!/usr/bin/python3
"""
Recurse it
"""
import requests


def matches_words(list_posts, dict_words):
    """Function that counts the matches with the keywords.
    """
    for post in list_posts:
        for word in post.get('data').get('title').split():
            for key in dict_words.keys():
                if key.lower() == word.lower():
                    dict_words[key] += 1


def recurse(subreddit, dict_words, after=None):
    """Recursive function that queries the Reddit API and
    search keywords in titles posts.
    """
    api_header = {'User-Agent': 'Mozilla/5.0'}
    api_params = {'after': after}
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    api_res = requests.get(
        api_url,
        headers=api_header,
        params=api_params
    )
    if api_res.status_code != 200:
        return(None)

    api_data = api_res.json().get('data')
    
    list_posts = api_data.get('children')
    
    after = api_data.get('after')

    matches_words(list_posts, dict_words)

    if after is None:
        return
    recurse(subreddit, dict_words, after)

def count_words(subreddit, word_list):
    """Function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript,
    but java should not).
    """
    dict_words = dict()
    dict_clear = dict()

    for word in word_list:
        dict_clear[word.lower()] = 0
        if word.lower() in dict_clear.keys():
            if dict_words.get(word.lower()) is None:
                dict_words[word.lower()] = 1
            else:
                dict_words[word.lower()] += 1

    recurse(subreddit, dict_clear)

    for k, v in dict_clear.items():
        dict_clear[k] = v * dict_words[k]

    list_sorted = sorted(dict_clear.items(), key=lambda item: item[1])
    list_sorted.reverse()

    dict_repeat = dict()
    list_repeat = list()
    current = 0
    for dupla in list_sorted:
        if current == 0:
            current = dupla[1]
        if current == dupla[1]:
            list_repeat.append(dupla[0])
            dict_repeat[current] = list_repeat
        else:
            current = dupla[1]
            list_repeat = list()
            list_repeat.append(dupla[0])
            dict_repeat[current] = list_repeat

    for k, v in dict_repeat.items():
        if k != 0:
            if len(v) > 1:
                v.sort()
                for w in v:
                    print("{}: {}".format(w, k))
            else:
                print("{}: {}".format(v[0], k))
