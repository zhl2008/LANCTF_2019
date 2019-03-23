### 1.题目名称
游客不允许的上传
### 2.题目类型

web(middle hard)

### 3.题目描述

你能猜到管理员的动态口令吗？那可以买张彩票。


### 4.考察知识点

信息收集，弱类型、文件包含、代码审计、文件内容检测绕过


### 5.解题思路

1. 进入后发现游客被限制，找到备份文件index.php.bak，代码审计发现需要在cookie中输入动态密码，长度为八位。随机密码通过cookie读入json格式，之后比较时==存在弱类型，在json中有bool值可以利用，构造`{"role":"admin","passnum":[true,true,true,true,true,true,true,true]}`，绕过验证。

2. 更新cookie，进入正常功能，根据审计结果发现可以文件包含读源码，在upload.php中发现上传后的文件对文件名进行了md5存在了uploads中
3. 审计upload.php发现替换了php文件中的<?，但是可以复写<<??绕过，或者使用script绕过
4. 上传一个e.php，计算'e.php'字符串的md5，在uploads/可访问到一句话