#POST /blocks/destroy

将指定id用户解除黑名单

##路径

	http://api.fanfou.com/blocks/destroy.[json|xml|rss]

##调用方法

	POST

##限制条件

	用户登录

##参数:

###id

- 作用: 指定目标用户的user_id或者loginname

- 举例: `id=testUser`

- 字段说明: 必选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式
 
        用户详细信息，格式参见[[users show]](/users/show)
