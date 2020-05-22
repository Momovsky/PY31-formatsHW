import json

def get_data(file):
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        datalist = []
        for item in data['rss']['channel']['items']:
            datalist.append(item['description'])
    return(datalist)

def word_counter(data):
    common_words_dict = {}
    for item in data:
        news_article = item.split()
        for word in news_article:
            if len(word) > 6:
                if word.lower() in common_words_dict:
                    common_words_dict[word.lower()] += 1
                else:
                    common_words_dict[word.lower()] = 1
            else:
                continue
    result = []
    for key, value in common_words_dict.items():
        result.append((value, key))
    result.sort(reverse=True)
    for item in result[0:10]:
        print(f'{item[1]}: {item[0]}')

word_counter(get_data('newsafr.json'))