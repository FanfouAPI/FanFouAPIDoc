#POST /statuses/update

发送消息

##路径

    http://api.fanfou.com/statuses/update.[json|xml|rss]

##调用方法

    POST 

##限制条件

    用户登录, 发送消息频率限制

##参数：

###status

- 作用: 消息内容

- 格式: `status=status_text`

- 字段说明: 必选，长度不大于140

###in\_reply\_to\_status\_id

- 作用: 回复的消息id

- 格式: `in_reply_to_status_id=msg_id`

- 字段说明: 可选

###in\_reply\_to\_user\_id

- 作用: 回复的用户id

- 格式: `in_reply_to_user_id=user_id`

- 字段说明: 可选

###source

- 作用: 消息来源

- 格式: `source=source_str`

- 字段说明: 可选, source应为英文字符串

###location

- 作用: 发布消息的地点

- 格式: `location=location_str`

- 字段说明: 可选, 最多30个字符, 使用'地点名称' 或 '一个半角逗号分隔的经纬度坐标'。如：`北京市海淀区` 或者 `39.9594049,116.298419`

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

        返回发送完成的消息，详细格式参见[[status show]](/statuses/show)
