<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>添加图片</title>
<script language="javascript">
<!--
function isok(theform)
{
if (myform.title.value=="")
  {
    alert("请填写图片标题！");
    myform.title.focus();
    return (false);
  }
  if (myform.url.value=="")
  {
    alert("请填写图片描述！");
    myform.url.focus();
    return (false);
  }
return (true);
}
-->
</script>
<style type="text/css">
<!--
body {
	margin-left: 0px;
	margin-top: 0px;
	margin-right: 0px;
	margin-bottom: 0px;
}
-->
</style>
</head>

<body>
<table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
  </table>
  
  <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
    <tr>
      <td height="30" align="center" bgcolor="799AE1">&nbsp;</td>
    </tr>
	<tr>
      <td height="30" align="center" bgcolor="">&nbsp;</td>
    </tr>
  </table>
<table width="650" border="0" align="center" cellpadding="5" cellspacing="1" >
  <tr>
    <td><form id="myform" name="myform"  enctype="multipart/form-data" method="post" action="upload.php" onSubmit="return isok(this)">
     <table width="650" border="0" align="center" cellpadding="5" cellspacing="1" bgcolor="#DEDFDE">
        <tr>
          <td height="40" colspan="2" bgcolor="#CBD7EE"><div align="center">添加图片信息</div></td>
          </tr>
        <tr>
          <td width="16%" align="center" bgcolor="#FFFFFF">图片标题：</td>
          <td bgcolor="#FFFFFF"><input name="title" type="text" id="title" size="50" /></td>
          </tr>
        <tr>
          <td height="22" align="center" bgcolor="#FFFFFF">图片描述：</td>
          <td height="22" bgcolor="#FFFFFF"><input name="url" type="text" id="url" size="50" /></td>
          </tr>        
        <tr>
          <td height="22" align="center" bgcolor="#FFFFFF">上传图片：</td>
          <td height="22" bgcolor="#FFFFFF"><input name="pic" type="file" id="pic" size="50" /></td>
          </tr>
       
        <tr>
          <td bgcolor="#FFFFFF">&nbsp;</td>
          <td bgcolor="#FFFFFF">            <input type="submit" name="Submit" value="发布图片" />          </td>
          </tr>
      </table>
        </form>
    </td>
  </tr>
</table>
</body>
</html>
