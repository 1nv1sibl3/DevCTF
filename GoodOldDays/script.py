#!/usr/bin/env python3
import requests

my_user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'

Old_user_agent='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'

headers = {
    'User-Agent': Old_user_agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}

response = requests.get('https://web.ctf.devclub.in/web/5/', headers=headers)

print(response.text)