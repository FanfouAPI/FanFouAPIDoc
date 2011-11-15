#GET:/friendships/exists

查询两个用户之间是否有follow关系 如果user_a关注user_b则返回 true, 否则返回false.

##路径
	http://api.fanfou.com/friendships/exists.[json|xml|rss]

##调用方法

	GET

##限制条件

	用户登录, 被查询用户需未设置隐私或者被登录用户关注

##参数:

###user_a

- 作用: 指定第一个用户的user_id，或者loginname

- 字段说明: 必选

###user_b

- 作用: 指定第二个用户的user_id，或者loginname

- 字段说明: 必选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式
 
		`json格式解释请见下方示例`

##示例

``GET http://api.fanfou.com/friendships/exists.json?user_a=test&user_b=debug``

	true

``GET http://api.fanfou.com/friendships/exists.json?user_a=test&user_b=debug``

	false
