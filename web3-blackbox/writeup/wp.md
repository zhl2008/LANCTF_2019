### 1.题目名称
图片上传
### 2.题目类型

web(middle hard)



### 3.题目描述

一个图片上传的站点


### 4.考察知识点

信息收集，黑盒，文件MIME检测，文件内容检测


### 5.解题思路

1. 打开后发现是一个文件上传站点，url中类似文件包含，但是限制了伪协议使用，无法获取源码，黑盒环境
2. 上传php提示上传gif和jpg，但上传图片无法进行文件包含使用，只能包含.php文件
3. 上传图片马，MIME为图片，后缀为php，发现php无法正常解析，php头<?中?被删除
4. 考虑使用script方式绕过，构造`<script language="php">system($_GET[0]);</script>`类似代码即可
