#GET /search/public_timeline

搜索全站消息(未设置隐私用户的消息)

##路径

    http://api.fanfou.com/search/public_timeline.[json|xml|rss]

##调用方法

    GET 

##参数：

###q

- 作用: 欲搜索关键词

- 格式: `q=query_word`

- 字段说明: 必选, 多个关键词可用 `|`分割

###since_id

- 作用: 只返回消息id大于`since_id`的消息

- 格式: `since_id=msg_id`

- 字段说明: 可选

###max_id

- 作用: 只返回消息id小于`max_id`的消息

- 格式: `max_id=msg_id`

- 字段说明: 可选

###count

- 作用: 指定指定返回消息的条数

- 格式: `count=msg_count`

- 字段说明: 可选, count in [1, 20]

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

- 字段说明: 可选

###format

- 作用: 当`format=html`时,返回消息中@提到的用户,网址等输出html链接

- 格式: `format=html`

- 字段说明: 可选

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

        返回一个由`status object`组成的数组，`status object`的格式参见[[status show]](/statuses/show)

            {
                status_0,
                status_1,
                status_2,
                status_3,
                status_4,
                ...
            }
