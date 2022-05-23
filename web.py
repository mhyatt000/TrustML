import requests
from bs4 import BeautifulSoup
import re

def scrape_model_hub(url):
    '''TF hub, Pytorch hub, modelhub, huggingface'''

    hub = url.split('/')[2].split('.')[0]

    print(hub)

    page = requests.get(url)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())

    body = soup.find('body')

    blob = ''

    if hub == 'huggingface':
        pass

    if hub == 'tfhub':

        desc = soup.find_all(class_='overview')
        print(body.prettify())


    if 'hub_c':
        pass

    return blob


def main():

    hub = 'https://tfhub.dev/deepmind/mmt/architecture-ft_language-q-24/1'
    # hub = 'https://huggingface.co/docs/transformers/main/en/model_doc/gpt2#transformers.GPT2LMHeadModel'

    scrape_model_hub(hub)

if __name__ == '__main__':
    main()
