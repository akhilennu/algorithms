# from collections import defaultdict
from english_words import english_words_set
import pandas as pd
import time
start_time = time.time()
mapper = {'2': 'a', '22': 'b', '222': 'c', '3': 'd', '33': 'e', '333': 'f', '4': 'g', '44': 'h', '444': 'i', '5': 'j', '55': 'k', '555': 'l', '6': 'm',
          '66': 'n', '666': 'o', '7': 'p', '77': 'q', '777': 'r', '7777': 's', '8': 't', '88': 'u', '888': 'v', '9': 'w', '99': 'x', '999': 'y', '9999': 'z', '0': ' '}


def numberToSentence(nums: str):
    start = 0
    end = len(nums)
    lst = ['']
    while(start < end):
        for i in range(len(lst)):
            tmp = lst[i]
            if(start >= 3 and nums[start-1] == nums[start] and nums[start-2] == nums[start] and nums[start-3] == nums[start] and (nums[start] in '79')):
                if(tmp[-1] == mapper[nums[start]] and tmp[-2] == mapper[nums[start]] and tmp[-3] == mapper[nums[start]]):
                    lst += [tmp[:-3]+mapper[nums[start-3] + nums[start-2] +
                                            nums[start-1]+nums[start]]]
            if(start >= 2 and nums[start-1] == nums[start] and nums[start-2] == nums[start]):
                if(tmp[-1] == mapper[nums[start]] and tmp[-2] == mapper[nums[start]]):
                    lst += [tmp[:-2]+mapper[nums[start-2] +
                                            nums[start-1]+nums[start]]]
            if(start >= 1 and nums[start] == nums[start-1]):
                if(tmp[-1] == mapper[nums[start]]):
                    lst += [tmp[:-1]+mapper[nums[start-1]+nums[start]]]
            lst[i] += mapper[nums[start]]
        start += 1
    # print(lst)
    possibleSents = list(set(lst))
    # print(possibleSents)
    d = dict()
    maxscore = 0
    for s in possibleSents:
        score = 0
        for w in s.split():
            if(w in english_words_set):
                score += 1
        try:
            d[score].append(s)
        except KeyError:
            d.update({score: [s]})
        if(score > maxscore):
            maxscore = score

    print("max score is ", maxscore)
    return d[maxscore]

# This will split the sentence into words and get the possible solutions word by word. It can either be combined into all possible sols or can be viewed as is


def numberToSentenceOptimized(sent: str):
    d = dict()
    for word in sent.split('0'):
        d.update({word: str(numberToSentence(word))})
    print(d)
    df = pd.DataFrame.from_dict(d, orient='index')
    df.to_csv(sent+'.csv')
    print('exported the data to ', sent, 'csv file')


sent = str(input('enter a number pad format: '))
# o = numberToSentence(sent)
# print(o)
start_opt_time = time.time()
# print("--- %s seconds ---" % (start_opt_time - start_time))

numberToSentenceOptimized(sent)
print("--- %s seconds ---" % (time.time() - start_opt_time))
