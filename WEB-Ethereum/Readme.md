

# WEB-Ethereum





文档变更记录

（A：增加、M：修改、D：删除）

| 版本   | 状态   | 参与者       | 日期         | 描述   |
| ---- | ---- | --------- | ---------- | ---- |
| V1.0 | A    | HAOZIGEGE | 2018.09.22 | 初稿   |
|      |      |           |            |      |
|      |      |           |            |      |
|      |      |           |            |      |
|      |      |           |            |      |
|      |      |           |            |      |
|      |      |           |            |      |



### 设计思路

考察基本的sql注入漏洞查找，以及sqlmap的基本使用,以太坊的基本理解和使用，以太坊合约的基本调用知识



### 分值估计

normal

###题目背景(流浪时代2）
During the period of the Wandering-Era (II), most of the government have lost their power in controlling their ethnic population, the money-in-law become pieces of shit. In the era lacking public trust, people resort to the Ethereum coins of BlockChain to rebuild the economic incentives. 

Hack this management system of  Ethereum private key, and the world will tremble.



### 题目部署

1.使用dockerfile编译一个基本docker（基本上所有的web题都会基于这个docker)

2.使用docker.sh运行该docker



### flag设置

flag在触发Ethereum上智能合约的SendFlag事件后，自动发送到指定邮箱


> LANCTF{B10ck_cha1n_1s_7h3_fu7ur3}