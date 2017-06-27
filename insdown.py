#!/usr/local/bin/python3

# <meta property="og:image" 
# content="https://instagram.fykz1-1.fna.fbcdn.net/t51.2885-15/e35/
# 19425484_281693612239114_7780086077041147904_n.jpg">

import urllib.request
import sys
import os
import re
import datetime


def inst_img(url):
    try: 
        with urllib.request.urlopen(url) as response:
            img_url_pt = r"content\=\"(http.*)\""
            html = response.read(5000).decode('utf-8')
            lines = html.split('\n')
            for line in lines:
                if "og:image" in line:
                    try:
                        return re.search(img_url_pt, line).groups()[0]
                    except AttributeError:
                        print("No image URL found")
                        return None

    except urllib.error.HTTPError as e:
        print(e, "URL is not correct!")


def download(url, path):
    with open(path, 'wb') as f:
        f.write(urllib.request.urlopen(url).read())


def main():
    if len(sys.argv) < 2:
        usage = '''Please enter the URL of the Instagram image:

insdown https://www.instagram.com/p/BV0wxuBF_Be/ /path/to/save/img.jpeg
        '''
        print(usage) 
        exit(1)

    url = sys.argv[1]
    path = sys.argv[2]
    img_url = inst_img(url)
    download(img_url, path)


if __name__ == '__main__':
    main()

