#coding:utf-8
import urllib

page = urllib.urlopen('https://cnodejs.org/')
htmlcode = page.read()
print(htmlcode)