import functools
import re
import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def show(func):
    """prints result"""

    @functools.wraps(func)
    def wrap_show(*args, **kwargs):
        value = func(*args, **kwargs)
        print(value)
        return value

    return wrap_show


def timer(func):
    """prints runtime"""

    @functools.wraps(func)
    def wrap_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished {func.__name__!r} in {round(end-start,4)} secs")
        return value

    return wrap_timer

def err(func):
    '''error handling'''

    @functools.wraps(func)
    def wrap_err(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except:
            print('investigate err')
        return value if value else None

    return wrap_err


# @timer
# @show
def get_websites(body, site):
    """websites can be:
    personal websites
    datasets
    other
    """

    return body.select(f'a[href*="{site}"]')


def spaceout(iter):
    if type(iter) is str:
        print(iter)
        return
    for i in iter:
        print("\n\n")
        try:
            print(i.prettify())
        except:
            print(i)

def unpack(res):
    '''unpacks bs4 ResultSet object nicely'''
    return list(res) #[0]


def nostr(iter):
    '''removes NavigableString objects from iter'''
    return [i for i in iter if not type(i) is NavigableString]


def scrape_model_hub(url):
    """TF hub, Pytorch hub, modelhub, huggingface"""

    hub = url.split("/")[2].split(".")[0]

    print(hub)

    page = requests.get(url)
    content = page.content

    soup = BeautifulSoup(content, "html.parser")
    # print(soup.prettify())

    body = soup.find("body")
    # print(body.prettify())

    data = {
        'name': None,
        "homepage": None,
        "downloads": None,
        "version": None,
        "license": None,
        "gh-stars": None,
        "forks": None,
        "issues": None,
        "pull-requests": None,
        "last-publish": None,
        "authors": None,
        "dependencies": None,
        "os": None,
        "badges": None,
        "library.io": None,
        "desc": None,
        "architecture": None,
        "dataset": None,
        "trainable": None,
        "framework": None,
        "applications": None,
        "performance": {
            "flops": None,
            "accuracy": None,
            "latency": None,
        },
        "domain": None,
        "demo": None,
        "preprocessing": None,
        "postprocessing": None,
        "docker": None,
        "inference": None,
    }

    if hub == "huggingface":
        prefix = "https://huggingface.co"

        header_container = body.find(class_="container relative")

        data['name'] = header_container.find(
            "a", class_="font-mono font-semibold break-words"
        ).get_text()

        a = get_websites(body, "github.io")

        desc = [item for item in body.find_all("section") if type(item) is Tag]

        '''
            how to parse desc for architecture and accuracy ...
            perplexity
            layers, heads, params

        '''


        # print(len(desc), desc[1].prettify())

        downloads = list(body.find('div', {'class' : 'model-graph flex-none'}).parent.children)[0].get_text()
        data['downloads'] = int(re.sub('\D','',downloads))

        dataset = nostr(unpack(body.select("nav article a")).children)

        data['dataset'] = {
            'name' : dataset[0].find('h4').get_text(),
            'link' : prefix + dataset[0].parent['href'],
            'last-updated' : None,
            'downloads' : None,
            'likes' : None
        }

        # [0].parent.children)


        # spaceout(dataset)
        # print(dataset.prettify())

        # quit()

        applications = list(
            body.select('nav[class="max-w-full flex flex-wrap gap-x-2.5 gap-y-2"]')[
                0
            ].children
        )
        data["applications"] = list(
            map(
                lambda x: {"app-name": x.get_text()[3:-2], "link": prefix + x["href"]},
                applications,
            )
        )

        pprint(data)

        # h1 = body.find('h1')
        # print(len(h1))

    if hub == "tfhub":

        desc = soup.find_all(class_="overview")

    if "hub_c":
        pass

    return data


def main():

    # hub = 'https://tfhub.dev/deepmind/mmt/architecture-ft_language-q-24/1'
    hub = "https://huggingface.co/distilgpt2"

    scrape_model_hub(hub)


if __name__ == "__main__":
    main()
