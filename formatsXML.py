import xml.etree.ElementTree as ET

def parse_file(file):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file, parser)
    root = tree.getroot()
    return(root)

def get_data(parsed_file):
    xml_items = parsed_file.findall('channel/item')
    data_list = []
    for item in xml_items:
        data_list.append(item.find("description").text)
    return(data_list)

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

word_counter(get_data(parse_file('newsafr.xml')))