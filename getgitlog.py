#!/usr/bin/env python

"""
getgitlog: Tool to output git commit messages in arrray format

Usage:
  getgitlog -h | --help
  getgitlog --version

 Options:
   -h, --help       Show this message.
   -v, --version        Print the version.
"""

from docopt import docopt
from requests.api import get
from bs4 import BeautifulSoup
from pprint import pprint

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, HTTPError
def main():
    commit_messages = []

    github_url = raw_input('GitHub url: ')
    branch = raw_input('Branch: ')

    url = (github_url + '/commits/' + branch)

    html = get(url).text

    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.findAll('p', { 'class' : 'commit-title' })

    for tag in soup:
        commit_messages.append(tag.get_text().strip().encode('ascii', 'ignore'))

    print('Git commit messages:\n' + str(commit_messages))

if __name__ == '__main__':

    arguments = docopt(__doc__, version='1.0')
    pprint(arguments)
