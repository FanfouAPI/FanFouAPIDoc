#GET /blocks/exists

检查用户是否被加入了黑名单

##路径

	http://api.fanfou.com/blocks/exists.[json|xml|rss]

##调用方法

	GET

##限制条件

	用户登录

##参数:

###id

- 作用: 指定目标用户的user_id或者loginname

- 举例: `id=testUser`

- 字段说明: 必需

##返回结果

###成功

如果用户已加入黑名单，返回用户详细信息

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式
 
        用户详细信息，格式参见[[users show]](/users/show)
