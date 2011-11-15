#GET: /friends/ids

返回用户好友的id列表

##路径

    http://api.fanfou.com/friends/ids.[json|xml|rss]

##调用方法

    GET

##限制条件

    用户登录, 目标用户为当前用户关注者或未设置隐私

##参数:

###id

- 作用: 目标用户的id，未设置则为当前登录用户

- 格式: `id=user_id`

- 字段说明: 可选

###page

- 作用: page用于指定返回结果的页码

- 格式: `page=page_id`

- 字段说明: 可选

###count

- 作用: 指定指定返回结果的条数

- 格式: `count=uid_count`

- 字段说明: 可选, count in [1, 20]

###callback

- 格式: callback=javascript函数名

- 作用: 当使用json格式时,生成的json对象将作为参数传给指定的javascript函数

- 字段说明: 可选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`

- 返回值

    * json格式

        返回一个由用户id组成的数组

            {
                'user_id_0',
                'user_id_1',
                'user_id_2',
                'user_id_3',
                ...
            }
