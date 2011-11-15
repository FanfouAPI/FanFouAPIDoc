#POST /saved_searches/create

收藏搜索关键字

##路径

    http://api.fanfou.com/saved_searches/create.[json|xml|rss]

##调用方法

    POST 

##限制条件

    用户登录

##参数：

###query

- 作用: 欲搜保存的索关键词

- 格式: `query=query_word`

- 字段说明: 必选, 多个关键词可用 `|`分割

###callback

- 格式: `callback=javascript`函数名

- 作用: 当使用json格式时,生成的json对象将作为参数传给指定的javascript函数

- 字段说明: 可选

##返回结果

###成功

- HTTP Status Code

    `200 OK HTTP/1.1`

- 返回值

    * json格式

        返回一个`saved search object`，`saved search object`的格式参见[[saved_searches create]](/saved_searches/create)
