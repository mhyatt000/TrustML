import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import re
import functools
import time


def show(func):
    '''prints result'''
    @functools.wraps(func)
    def wrap_show(*args, **kwargs):
        value = func(*args, **kwargs)
        print(value)
        return value

    return wrap_show


def timer(func):
    '''prints runtime'''
    @functools.wraps(func)
    def wrap_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished {func.__name__!r} in {round(end-start,4)} secs")
        return value

    return wrap_timer


# @timer
# @show
def get_websites(body, site):
    '''websites can be:
        personal websites
        datasets
        other
    '''

    return body.select(f'a[href*="{site}"]')

def spaceout(iter):
    for i in iter:
        print(i); print('\n\n')

def re_empty():
    '''uses regex to evaluate string emptiness'''

def scrape_model_hub(url):
    '''TF hub, Pytorch hub, modelhub, huggingface'''

    hub = url.split('/')[2].split('.')[0]

    print(hub)

    page = requests.get(url)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())

    body = soup.find('body')
    # print(body.prettify())

    data = {
        'factors1' : {
            'homepage' : ,
            'downloads' : ,
            'version' : ,
            'license' : ,
            'gh-stars' : ,
            'forks' : ,
            'issues' : ,
            'pull-requests' : ,
            'last-publish' : ,
            'authors' : ,
            'dependencies' : ,
            'os' : ,
            'badges' : ,
            'library.io' : ,
        },
        'factors2' : {
            'desc' : ,
            'architecture' : ,
            'dataset': ,
            'trainable' : ,
            'framework' : ,
            'applications' : ,
            'performance' : {
                'flops' : ,
                'accuracy' : ,
                'latency' : ,
            },
            'domain' : ,
            'demo' : ,
            'preprocessing' : ,
            'postprocessing' : ,
            'docker' : ,
            'inference' : ,

        }
    }
    
    if hub == 'huggingface':

        header_container = body.find(class_='container relative')
        name = header_container.find('a', class_='font-mono font-semibold break-words').get_text()

        a = get_websites(body, "github.io")

        desc = [item for item in body.find_all('section') if type(item) is Tag]

        # print(len(desc), desc[1].prettify())

        dataset = body.select('h2 svg')[0].parent.children

        application = body.select('nav[class="max-w-full flex flex-wrap gap-x-2.5 gap-y-2"]')

        # spaceout(application)

        # h1 = body.find('h1')
        # print(len(h1))


    if hub == 'tfhub':

        desc = soup.find_all(class_='overview')


    if 'hub_c':
        pass


    return blob


def main():

    # hub = 'https://tfhub.dev/deepmind/mmt/architecture-ft_language-q-24/1'
    hub = 'https://huggingface.co/distilgpt2'

    scrape_model_hub(hub)

if __name__ == '__main__':
    main()
