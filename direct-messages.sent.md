#GET /direct_messages/sent

显示20条发件箱中的私信

##路径

    http://api.fanfou.com/direct_messages/sent.[json|xml|rss]

##调用方法

    GET 

##参数：

###count

- 作用: 指定指定返回私信的条数

- 格式: `count=msg_count`

- 字段说明: 可选, count in [1, 20]

###page

- 作用: 指定返回结果的页码

- 格式: `page=page_id`

- 字段说明: 可选

###since_id

- 作用: 只返回id大于`since_id`的私信

- 格式: `since_id=msg_id`

- 字段说明: 可选

###max_id

- 作用: 只返回id小于`max_id`的私信

- 格式: `max_id=msg_id`

- 字段说明: 可选

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

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

        返回一个由`direct message object`组成的数组，`direct message object`的格式参见[[direct_messages new]](/direct_messages/new)

            {
                direct_message_0,
                direct_message_1,
                direct_message_2,
                direct_message_3,
                ...
            }
