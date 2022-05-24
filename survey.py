'''get emails for survey'''

import selenium
import functools
import re
import time
from pprint import pprint
import json

import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from tqdm import tqdm

from web import *

def get_args():

    ap = ArgumentParser()

    ap.add_argument('-i', '--input', type=str, nargs='+', default='https://huggingface.co/')

    args = ap.parse_args()
    return args

def main(driver):

    args = get_args()
    urls = args.input

    # [extract(url) for url in tqdm(urls)]

    path = 'huggingface.txt'
    with open(path, 'r') as file:
        originals = [item for item in file.read().split('\n')]

        for url in tqdm(originals):
            huggingface(url)
            time.sleep(5)

def huggingface(url):

    try:
        page = requests.get(url)
        content = page.content
        soup = BeautifulSoup(content, "html.parser")

        atags = unpack(soup.find_all('a'))
        atags = list(map(lambda x: x['href'], atags))

        prefix = 'https://huggingface.co'
        atags = [prefix + x for x in atags]
    except:
        return

    # print(atags)
    path = 'huggingface.txt'

    try:
        with open(path, 'r') as file:
            originals = [item for item in file.read().split('\n')]
        new = atags + originals
    except:
        new = atags
    new = set(new)

    with open(path, 'w') as file:
        [file.write(item + '\n') for item in new]


def extract(url):
    # url = 'https://huggingface.co/spaces/aubmindlab/Arabic-NLP'
    # url = 'https://huggingface.co/distilgpt2'

    data = {
        'githubs' : [

        ]
    }

    # driver.implicitly_wait(10)
    # driver.get(url)
    #
    # def find(xpath):
    #     return driver.find_elements(By.XPATH, xpath)
    #
    # class Element(selenium.webdriver.remote.webelement.WebElement):
    #     pass
    #     # __init__(self,element):
    #     #     super().__init__(self)
    #     #
    #     #     self.innerHTML = self.get_attribute('innerHTML')
    #
    # def scroll(elem):
    #     a = ActionChains(driver)
    #     a.key_down(Keys.COMMAND).perform()
    #     elem.send_keys(Keys.DOWN)
    #     # .key_up(Keys.COMMAND).perform()

    #
    # html = find('/html')[0]
    # time.sleep(1)
    # html.send_keys(Keys.END)
    # time.sleep(1)
    # # scroll(html)
    # #
    # # html.send_keys(Keys.COMMAND, Keys.DOWN)
    # # time.sleep(0.2)
    # # html.send_keys(Keys.COMMAND, Keys.UP)
    # # time.sleep(0.2)
    # #
    #
    # body = find('/html/body')[0]
    #
    # gh = find('//a')#[@href*="github"]')
    # gh = list(map(lambda x: x.get_attribute('href'), gh))
    # gh = [i for i in gh if 'github' in i]
    #
    match = 'href="https://github.*"'
    # print((gh))
    #
    # innerhtml = html.get_attribute('innerHTML')
    #
    # print(type(innerhtml))
    # print(re.findall('.*github.*',innerhtml))
    #
    # # allows inspect element
    # while True:
    #     time.sleep(5)
    # quit()
    #



    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, "html.parser")

    atags = unpack(soup.find_all('a'))
    atags = list(map(lambda x: x['href'], atags))
    gh = [x for x in atags if 'github' in x]

    pprint((gh))

    # quit()

    # print(re.findall('\w*@\w', body))
    # print(re.findall('https://github.com/', body))
    #
    #
    # url = url.replace('/','.')

    with open(f'githubs.json', 'r') as file:
        try:
            temp = json.load(file)
        except:
            temp = dict()
        try:
            temp[url] = list(set(temp[url] + gh))
        except:
            temp[url] = gh
    with open(f'githubs.json', 'w') as file:
        json.dump(temp, file)

if __name__ == '__main__':
    main(None)

    # try:
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     main(driver)
    # except Exception as ex:
    #     driver.quit()
    #     raise(ex)
