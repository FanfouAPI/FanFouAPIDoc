#GET:/friendships/show

返回两个用户之间follow关系的详细信息

##路径

	http://api.fanfou.com/friendships/show.[json|xml|rss]

##调用方法

	GET

##限制条件

	用户登录

##参数:

###source_screen_name

- 作用: 指定第一个用户的loginname

- 字段说明: 必选

###target_screen_name

- 作用: 指定第二个用户的loginname

- 字段说明: 必选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
	* json格式
 
		`json格式解释请见下方示例`

##示例

``GET http://api.fanfou.com/friendships/show.json?source_screen_name=test&target_screen_name=debug``

    {
        "relationship":{"source":{"id":"test",
                                  "screen_name":"测试昵称",
                                  "following":"false",
                                  "followed_by":"false",
                                  "notifications_enabled":"false",
                                  "blocking":"true"
                        },
                        "target":{"id":"debug",
                                  "screen_name":"debug",
                                  "following":"false",
                                  "followed_by":"false"
                                  }}
    }
