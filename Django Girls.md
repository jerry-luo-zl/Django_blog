# Blog Of Django

## 2021.2.24

### 环境部署:

#### pythonanywhere:

username:lzl

mail:qq

#### functions of pythonanywhere:

The Django Girls tutorial includes a section on what is called Deployment, which is the process of taking the code that powers your new web application and moving it to a publicly accessible computer (called a server) so other people can see your work.

就是把驱动web应用的代码放到服务器上，让大家都可以访问

这里牵扯到web应用程序中的部署概念

### how internet works

DNS解析通常是网络运营商做的

### other preparation work

virtualenv(virtual environment) 虚拟环境用来隔离各个项目

https://blog.csdn.net/u012206617/article/details/90294421

### the configuration of Django

以下修改均针对Django框架中的setting.py

0.languge,time,host

1.database

SQLITE

轻型数据库，对标python中的PySQLite模块

python manage.py migrate(部署数据库)

![image-20210225171743821](C:\Users\lzl\AppData\Roaming\Typora\typora-user-images\image-20210225171743821.png)

2.测试server端

python manage.py runserver

![image-20210225171806308](C:\Users\lzl\AppData\Roaming\Typora\typora-user-images\image-20210225171806308.png)

初始界面是favicon.ico？？？？not found

![image-20210225171647969](C:\Users\lzl\AppData\Roaming\Typora\typora-user-images\image-20210225171647969.png)



### Django中的url处理过程

(根据官方文档)

When a user requests a page from your Django-powered site, this is the algorithm the system follows to determine which Python code to execute:

1. Django determines the root URLconf module to use. Ordinarily, this is the value of the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-ROOT_URLCONF) setting, but if the incoming `HttpRequest` object has a [`urlconf`](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest.urlconf) attribute (set by middleware), its value will be used in place of the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-ROOT_URLCONF) setting.
2. Django loads that Python module and looks for the variable `urlpatterns`. This should be a [sequence](https://docs.python.org/3/glossary.html#term-sequence) of [`django.urls.path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path) and/or [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.re_path) instances.
3. Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL.
4. Once one of the URL patterns matches, Django imports and calls the given view, which is a simple Python function (or aclass-based view). The view gets passed the following arguments:
   - An instance of [`HttpRequest`](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest).
   - If the matched URL pattern returned no named groups, then the matches from the regular expression are provided as positional arguments.
   - The keyword arguments are made up of any named parts matched by the path expression, overridden by any arguments specified in the optional `kwargs` argument to [`django.urls.path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path) or [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.re_path).
5. If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view. See [Error handling](https://docs.djangoproject.com/en/2.2/topics/http/urls/#error-handling) below.

1.首先Django决定采取什么样的URLconf module

2.Django加载python模板(具体的来说应该是指urls.py)，然后引入一个uelpatterns的对象

3.然后Django去匹配url

4.然后如果匹配到的话就会转向urlpatterns中指定的python函数去处理请求(view.py中)

5.匹配不到的话就报错

tips:

1.可以使用正则表达式

2.处理请求时不会考虑参数的问题，例如

For example, in a request to `https://www.example.com/myapp/`, the URLconf will look for `myapp/`.

In a request to `https://www.example.com/myapp/?page=3`, the URLconf will look for `myapp/`.

3.include其他的URLconfs（！！有待尝试）

这里的用途如下:

```python
# 存在问题：Django 项目里多个app目录共用一个 urls 容易造成混淆，后期维护也不方便。

# 解决：使用路由分发（include），让每个app目录都单独拥有自己的 urls。

# 步骤：

# 1、在每个 app 目录里都创建一个 urls.py 文件。
# 2、在项目名称目录下的 urls 文件里，统一将路径分发给各个 app 目录。

from django.contrib import admin
from django.urls import path,include # 从 django.urls 引入 include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("app01/", include("app01.urls")),
    path("app02/", include("app02.urls")),
]
```



### Django中的view处理函数

