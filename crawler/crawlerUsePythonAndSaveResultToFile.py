#coding:utf-8
import urllib

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def save_html_to_file(fileName, html):
    pageFile = open(fileName, 'w')
    pageFile.write(html)
    pageFile.close()

save_html_to_file('index.html', get_html('https://cnodejs.org/'))