#POST: /saved_searches/destroy

删除收藏的搜索关键字

##路径

    http://api.fanfou.com/saved_searches/destroy.[json|xml|rss]

##调用方法

    POST

##限制条件

    用户登录, id所指定的关键字已被用户收藏

##参数:

###id

- 作用: 指定需要删除的关键字id

- 格式: `id=query_id`

- 字段说明: 必选

###callback

- 格式: callback=javascript函数名

- 作用: 当使用json格式时,生成的json对象将作为参数传给指定的javascript函数

- 字段说明: 可选

##返回结果

###成功

返回被删除关键字的详细内容

- HTTP Status Code

    `200 OK HTTP/1.1`

- 返回值

    * json格式

    被删除关键字的详细内容，关键字格式参见[[saved_searches create]](/saved_searches/create)
