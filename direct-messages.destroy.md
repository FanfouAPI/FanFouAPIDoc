#POST: /direct_messages/destroy

删除某条私信

##路径

    http://api.fanfou.com/direct_messages/destroy.[json|xml|rss]

##调用方法

    POST

##限制条件

    用户登录, 只能删除自己发出或收到的私信

##参数:

###id

- 作用: 指定需要删除的私信id

- 格式: `id=msg_id`

- 字段说明: 必选

###callback

- 格式: callback=javascript函数名

- 作用: 当使用json格式时,生成的json对象将作为参数传给指定的javascript函数

- 字段说明: 可选

##返回结果

###成功

返回被删除私信的详细内容

- HTTP Status Code

    `200 OK HTTP/1.1`

- 返回值

    * json格式

        被删除私信的详细内容，私信格式参见[[direct_messages new]](/direct_messages/new)
