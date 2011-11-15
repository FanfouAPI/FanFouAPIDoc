#GET /saved_searches/list

列出登录用户保存的搜索关键字

##路径

    http://api.fanfou.com/saved_searches/list.[json|xml|rss]

##调用方法

    GET 

##参数：

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

        返回一个由`saved search object`组成的数组，`saved search object`的格式参见[[saved_searches show]](/saved_searches/show)

            {
                saved_search_0,
                saved_search_1,
                saved_search_2,
                saved_search_3,
                ...
            }
