import webbrowser
urls = {
    'Notion':  'https://www.notion.so/Python-e9dcfe884c944d10906d19d8cb2859ab',
    'ChatGPT': 'https://chat.openai.com/',
    'codic':   'https://codic.jp/engine'
}

for url_key in urls:
    webbrowser.open(urls[url_key])