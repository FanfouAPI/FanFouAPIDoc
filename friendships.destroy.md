#POST /friendships/destroy

取消关注好友

##路径

    http://api.fanfou.com/friendships/destroy.[json|xml|rss]

##调用方法

    POST

##限制条件

    用户登录

##参数:

###id

- 作用: 指定需要添加的好友的user_id，或者loginname

- 格式: `id=user_id|loginname`

- 字段说明: 必选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`
 
- 返回值
 
    * json格式
 
        被取消关注用户的详细信息,格式参见[users show](/users/show)
