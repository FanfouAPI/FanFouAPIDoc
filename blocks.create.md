#POST /blocks/create

把指定id用户加入黑名单

##路径

	http://api.fanfou.com/blocks/create.[json|xml|rss]

##调用方法

	POST

##限制条件

	用户登录

##参数:

###id

- 作用: 指定目标用户的user_id或者loginname

- 举例: `id=testUser`

- 字段说明: 必需

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式

        被拉黑用户详细信息，格式参见[[users show]](/users/show)
