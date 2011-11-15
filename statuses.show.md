#GET: /statuses/show

返回好友或未设置隐私用户的某条消息

##路径

    http://api.fanfou.com/statuses/show.[json|xml|rss]

##调用方法

    GET

##限制条件

    用户登录

##参数:

###id

- 作用: 指定需要浏览的消息id

- 格式: `id=msg_id`

- 字段说明: 必选

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

- 字段说明: 可选

###format

- 作用: 当format=html时,返回消息中@提到的用户,网址等输出html链接

- 格式: format=html

- 字段说明: 可选

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

        `json格式解释请见下方示例`

###失败

####试图访问隐私用户的消息
- HTTP Status Code
    `403 Forbidden HTTP/1.1`

- 返回值

    * json格式

            {
            "request":"/statuses/show.json?id=OkBUI7A90Ew",
            "error":"你没有通过这个用户的验证"
            }

    * xml格式

            <?xml version="1.0" encoding="UTF-8"?>
            <hash>
            <request>/statuses/show.rss?id=OkBUI7A90Ew</request>
            <error>你没有通过这个用户的验证</error>
            </hash>

####id所指定的消息不存在
- HTTP Status Code

    `404 Not Found HTTP/1.1`

- 返回值

    * json格式

            {
            "request":"/statuses/show.json",
            "error":"没有这条消息"
            }

    * xml格式

            <?xml version="1.0" encoding="UTF-8"?>
            <hash>
            <request>/statuses/show.xml?id=OkBUI7A90</request>
            <error>没有这条消息</error>
            </hash>

##示例

###请求URL

``GET http://api.fanfou.com/statuses/show.json?id=UcIlC04F2pQ``

###返回结果

    {
        "created_at": "Wed Nov 09 07:15:21 +0000 2011",
        "id": "UcIlC04F2pQ",
        "text": "看看",
        "source": "网页",
        "truncated": false,
        "in_reply_to_status_id": "",
        "in_reply_to_user_id": "",
        "in_reply_to_screen_name": "",
        "repost_status_id": "gcIghPhCxQ",
        "repost_user_id": "clock",
        "repost_screen_name": "钟钟",
        "favorited": false,
        "is_self": false,
        "user": {"id": "superisaac",
                 "name": "杲i杲",
                 "screen_name": "杲i杲",
                 "location": "北京 朝阳区",
                 "gender": "男",
                 "birthday": "",
                 "description": "爱工作, 爱编程, 爱摄影, 爱暴走, 也爱哗哗的灌水. 我不是富二代, 我是技术宅男, 我要减肥.",
                 "profile_image_url": "http://avatar3.fanfou.com/s0/01/3a/ve.jpg?1304991298",
                 "profile_image_url_large": "http://avatar3.fanfou.com/l0/01/3a/ve.jpg?1304991298",
                 "url": "",
                 "protected": false,
                 "followers_count": 1329,
                 "friends_count": 2011,
                 "favourites_count": 29,
                 "statuses_count": 5259,
                 "following": true,
                 "notifications": true,
                 "created_at": "Thu Feb 24 10:01:24 +0000 2011",
                 "utc_offset": 28800,
                 "profile_background_color": "#C4B9A3",
                 "profile_text_color": "#3C2215",
                 "profile_link_color": "#BC834A",
                 "profile_sidebar_fill_color": "#F0EADC",
                 "profile_sidebar_border_color": "#FFFFFF",
                 "profile_background_image_url": "http://static.fanfou.com/img/bg/14.jpg",
                 "profile_background_tile": false
                }
        "photo": {"imageurl":"http://photo.fanfou.com/m0/02/f2/7q_317973.jpg",
                  "thumburl":"http://photo.fanfou.com/t0/02/f2/7q_317973.jpg",
                  "largeurl":"http://photo.fanfou.com/n0/02/f2/7q_317973.jpg"
                 }
    }

###字段说明

<table>
    <tr>
        <td>字段返回值</td>
        <td>字段类型</td>
        <td>字段说明</td>
    </tr>
    <tr>
        <td>created_at</td>
        <td>string</td>
        <td>消息发送时间</td>
    </tr>
    <tr>
        <td>id</td>
        <td>string</td>
        <td>消息id</td>
    </tr>
    <tr>
        <td>text</td>
        <td>string</td>
        <td>消息内容</td>
    </tr>
    <tr>
        <td>source</td>
        <td>string</td>
        <td>消息来源</td>
    </tr>
    <tr>
        <td>truncated</td>
        <td>boolean</td>
        <td>消息是否被截断</td>
    </tr>
    <tr>
        <td>in_reply_to_status_id</td>
        <td>string</td>
        <td>回复的消息id</td>
    </tr>
    <tr>
        <td>in_reply_to_user_id</td>
        <td>string</td>
        <td>回复的用户id</td>
    </tr>
    <tr>
        <td>favorited</td>
        <td>boolean</td>
        <td>消息是否被登录用户收藏</td>
    </tr>
    <tr>
        <td>in_reply_to_screen_name</td>
        <td>string</td>
        <td>回复用户的昵称</td>
    </tr>
    <tr>
        <td>user</td>
        <td>object</td>
        <td>发送此消息之用户信息, 详情参见<a href="../user/show">User Show</a></td>
    </tr>
    <tr>
        <td>photo</td>
        <td>object</td>
        <td>消息中图片信息</td>
    </tr>
</table>

图片的详细信息


<table>
    <tr>
        <td>字段返回值</td>
        <td>字段类型</td>
        <td>字段说明</td>
    </tr>
    <tr>
        <td>imageurl</td>
        <td>string</td>
        <td>图片地址</td>
    </tr>
    <tr>
        <td>thumburl</td>
        <td>string</td>
        <td>缩略图地址</td>
    </tr>
    <tr>
        <td>largeurl</td>
        <td>string</td>
        <td>图片原图地址</td>
    </tr>
</table>
