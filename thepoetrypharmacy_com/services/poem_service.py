import json
import random

poems_list = list()

def _prepare_poem_list():
    
    global peoms_list 

    with open('/Users/sean/Documents/ThePoetryPharmacy/thepoetrypharmacy_com/data/poems.jsonl', 'r') as json_file:
        json_list = list(json_file)

        for json_str in json_list:
            result = json.loads(json_str)
            poems_list.append(result)
            
def get_authors():
    _prepare_poem_list()

    author_list = list()
    for item in poems_list:
        if item['author'] not in author_list:
            author_list.append(item['author'])

    return author_list

def get_poems_by_author(author_name: str):
    _prepare_poem_list()
    return [item['poem'] for item in poems_list if item['author'] == author_name and item['poem'] != '']

def get_titles():
    _prepare_poem_list()

    title_list = list()
    for item in poems_list:
        if item['title'] not in title_list:
            title_list.append(item['title'])

    return title_list

def get_poems_by_title(title_name: str):
    _prepare_poem_list()
    return [item['poem'] for item in poems_list if item['title'] == title_name and item['poem'] != '']

def get_latest_poems(num_of_poems: int=1):
    _prepare_poem_list()
    ret_poems = list()
    while len(ret_poems) < num_of_poems:
        index = random.randint(0, len(poems_list)-1)
        if poems_list[index]['poem'] != '':
            ret_poems.append(poems_list[index])
    return ret_poems

def main():
    poems = get_latest_poems(3)
    for poem in poems:
        print(poem)
    """
    poems = get_poems_by_author('Gina Myers')
    for poem in poems:
        print(poem)
    """

if __name__ == '__main__':
    main()