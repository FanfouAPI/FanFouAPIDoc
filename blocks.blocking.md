#GET:/blocks/blocking

获取用户黑名单列表

##路径

	http://api.fanfou.com/blocks/blocking.[json|xml|rss]

##调用方法

	GET

##限制条件

	用户登录

##参数:

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

- 字段说明: 可选

###page

- 作用: 用以返回指定页号的结果

- 举例: `page=3`

- 字段说明: 可选 (默认值为0)

##count

- 作用: 用以指定每页返回结果的数量

- 举例: `count=10`

- 字段说明: 可选（默认值为20）

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式
 
        返回一个由用户的详细信息组成的数组，用户的详细信息格式参见[[user show]](/user/show)

            {
                user_0,
                user_1,
                ...
            }
