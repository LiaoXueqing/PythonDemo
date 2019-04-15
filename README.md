# Python Demo

在安装Python的环境下运行该 Demo， 开发环境 Python 版本 2.7.10

## 爬取 Cnode网站的内容，输出到控制台
crawler 目录下，运行 python crawlerUsePython.py

## 爬取 Cnode网站的内容，输出到文件 index.html 中
crawler 目录下，运行 python crawlerUsePythonAndSaveResultToFile.py
   
   定义了两个方法：
   get_html() 获取对应 url 页面的 html 代码
   save_html_to_file() 把指定的 html 代码存到指定的文件中
    
## 从控制台获取输入
getInput 目录下，运行 python getInputFromConsole.py

结果：
```
请输入(use raw_input)：Hello Python
你输入的内容是:  Hello Python
请输入(use input)：[x*5 for x in [1,2,3]]
你输入的内容是:  [5, 10, 15]
```

## 从文件获取输入
getInput 目录下，运行 python getInputFromFile.py

结果：
```
读取的字符串是:
Hello Python.
Hello World.
How are you?
```

