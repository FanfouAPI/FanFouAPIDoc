#GET /blocks/ids

获取用户黑名单id列表

##路径

	http://api.fanfou.com/blocks/ids.[json|xml|rss]

##调用方法

	GET

##限制条件

	用户登录

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式
 
		`json格式解释请见下方示例`

##示例

``GET http://api.fanfou.com/blocks/ids.json``

	{
		"loginname1",
		"loginname2",
		...
	}
