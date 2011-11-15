#POST: /account/update_profile

通过 API 更新用户资料

##路径

	http://api.fanfou.com/account/update_profile.[json|xml]

##调用方法
	
	POST


##条件限制

	需要登陆

##参数： 

###url

- 作用：指定自定义网址
- 格式：URL
- 字段说明：可选

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

- 字段说明: 可选

###location

- 作用：指定所在地位置
- 格式：字符串
- 字段说明：可选

###description 

- 作用：指定自述
- 格式：字符串
- 字段说明：可选

###name

- 作用：指定姓名
- 格式：字符串
- 字段说明： 可选

###email 

- 作用：指定电子邮件
- 格式：字符串
- 字段说明： 可选

##返回值：

成功

- HTTP Status Code

        `200 OK HTTP/1.1`
	
失败
