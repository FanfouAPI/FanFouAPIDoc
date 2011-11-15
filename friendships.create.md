#POST:/friendships/create

添加用户为好友

##路径

	http://api.fanfou.com/friendships/create.[json|xml|rss]

##调用方法

	POST

##限制条件

	用户登录

##参数:

###id

- 作用: 指定需要添加的好友的user_id，或者loginname

- 格式: `id=user_id|loginname`

- 字段说明: 必选

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

- 字段说明: 可选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式

        新添加好友的详细信息，格式参见[[users show]](/users/show)
