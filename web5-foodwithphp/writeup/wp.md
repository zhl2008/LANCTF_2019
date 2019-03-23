### 1.题目名称
关于吃吃吃
### 2.题目类型

web(middle hard)



### 3.题目描述

一个关于吃吃吃的网站


### 4.考察知识点

信息收集，文件包含，代码审计，session构造


### 5.解题思路

1. 注册一个账户，登录后会访问`/user.php?page=guest`，猜测存在文件包含，使用php://filter/convert.base64-encode/resource读源码 user.php function.php等
2. 代码审计，发现无法构造SQL注入，管理员可以访问info.php，继续读info.php，提示include("templates/info.html")
3. 访问templates/info.html在网页源代码中发现hint，m4nageee.php，不能直接访问，使用文件包含访问。
4. 进入后发现是管理界面，同时m4nageee.php源代码包含了profile233.html，直接访问发现

```
 <?php
if(isset($_GET['nick']))
    $_SESSION['nick']=$_GET['nick'];
if(isset($_SESSION['nick']))
    echo "hello ".$_SESSION['nick'];                              
else 
    echo "hello admin, input your nickname."
?>
```
5. 在管理界面构造session一句话，包含/var/lib/php5/sess_xxxx文件即可

