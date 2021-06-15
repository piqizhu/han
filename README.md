
# han
![PyPI](https://img.shields.io/pypi/v/han?style=plastic)

han = 汉    
han = 汉(字) 

一个python常用函数库，里面的函数都是中文汉字

>该项目翻译了部分函数，但没有对原函数做任何修改,不会影响你以前的代码      
>该项目并非生硬的翻译python标准库，而是在某些地方做了修改，减少歧义，   
>如 `round()` 是python里做四舍五入运算的，   
>`round(1.675, 2)` # 返回值 1.68，小数部分是68    
>`round(2.675, 2)` # 返回值 2.67，小数部分是67    
>返回值里的最后一位小数点则充满了歧义，一个是8,一个是7，违反了人类直觉    
>
>而本项目的函数  `四舍五入()` 则没有这种违反直觉的歧义， 
>
>你可以根据自己的需要使用本项目的 `四舍五入()` 或者用python自带的 `round()`
>
>注：经过简单测试，在以下语言中，round函数的返回值是符合直觉的，这让我们有底气重写 `四舍五入()` :    
>php（round）、c++（round）、c#（Math.Round）、office Excel(round)      
>其他语言，软件 没有测试，不太懂
 
 
 
## 使用前提:
 * python > 3.8+ （3.8以上的版本）

## 安装

`pip install han`

## 用法

```python
from han.数学 import *

求绝对值(-123)
 
```

## 文档

gitee（速度快） https://xxxxx.com   
github（速度慢） https://xxxxx.com   



## 测试
 1、下载代码到本地,进入代码根目录    
 2、执行 `pip install poetry `   
 3、执行 `poetry install`   
 4、执行 `pytest`    

 