#POST /direct_messages/new

发送私信

##路径

    http://api.fanfou.com/direct_messages/new.[json|xml|rss]

##调用方法

    POST 

##限制条件

    用户登录, 发送私信频率限制

##参数：

###user

- 作用: 发送私信目的用户

- 格式: `user=user_text`

- 字段说明: 必选

###text

- 作用: 私信内容

- 格式: `text=msg_text`

- 字段说明: 必选, 长度小于140

###in\_reply\_to\_id

- 作用: 回复的私信id

- 格式: `in_reply_to_id=msg_id`

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

        已发送私信的详细内容，私信格式参见[[direct_messages new]](/direct_messages/new)

##示例

``GET http://api.fanfou.com/direct_messages/inbox.json?count=1``

###返回结果

    [
        {
            "id":"NpviVMc5l_8",
            "text":"pong",
            "sender_id":"lisztli",
            "recipient_id":"test",
            "created_at":"Thu Nov 10 03:43:14 +0000 2011",
            "sender_screen_name":"LisztLi",
            "recipient_screen_name":"test22222",
            "sender":{"id":"lisztli",
                      "name":"LisztLi",
                      "screen_name":"LisztLi",
                      "location":"北京 海淀区",
                      "gender":"男",
                      "birthday":"1986-02-07",
                      "description":"",
                      "profile_image_url":"http://avatar3.fanfou.com/s0/00/3z/3k.jpg?1308030845",
                      "profile_image_url_large":"http://avatar3.fanfou.com/l0/00/3z/3k.jpg?1308030845",
                      "url":"",
                      "protected":false,
                      "followers_count":161,
                      "friends_count":142,
                      "favourites_count":10,
                      "statuses_count":2616,
                      "following":true,
                      "notifications":true,
                      "created_at":"Wed Sep 05 01:11:07 +0000 2007",
                      "utc_offset":28800,
                      "profile_background_color":"#acdae5",
                      "profile_text_color":"#222222",
                      "profile_link_color":"#0066cc",
                      "profile_sidebar_fill_color":"#e2f2da",
                      "profile_sidebar_border_color":"#b2d1a3",
                      "profile_background_image_url":"http://avatar.fanfou.com/b0/00/3z/3k_1308411449.jpg",
                      "profile_background_tile":true
                },
            "recipient":{"id":"test",
                         "name":"test22222",
                         "screen_name":"test22222",
                         "location":"北京 海淀区",
                         "gender":"男",
                         "birthday":"2105-03-11",
                         "description":"测试帐号",
                         "profile_image_url":"http://avatar3.fanfou.com/s0/00/5n/sk.jpg?1320737096",
                         "profile_image_url_large":"http://avatar3.fanfou.com/l0/00/5n/sk.jpg?1320737096",
                         "url":"http://fanfou.com/test",
                         "protected":true,
                         "followers_count":9,
                         "friends_count":16,
                         "favourites_count":22,
                         "statuses_count":112,
                         "following":false,
                         "notifications":false,
                         "created_at":"Sat Jun 09 23:56:33 +0000 2007",
                         "utc_offset":28800,
                         "profile_background_color":"#ffffe5",
                         "profile_text_color":"#004040",
                         "profile_link_color":"#ff0000",
                         "profile_sidebar_fill_color":"#ffefbf",
                         "profile_sidebar_border_color":"#ffac80",
                         "profile_background_image_url":"http://avatar.fanfou.com/b0/00/5n/sk_1320749993.jpg",
                         "profile_background_tile":true
            }
        }
    ]

###字段说明

<table>
    <tr>
        <td>字段返回值</td>
        <td>字段类型</td>
        <td>字段说明</td>
    </tr>
    <tr>
        <td>id</td>
        <td>string</td>
        <td>私信id</td>
    </tr>
    <tr>
        <td>text</td>
        <td>string</td>
        <td>私信内容</td>
    </tr>
    <tr>
        <td>sender_id</td>
        <td>string</td>
        <td>发出私信的用户id</td>
    </tr>
    <tr>
        <td>recipient_id</td>
        <td>string</td>
        <td>收到私信的用户id</td>
    </tr>
    <tr>
        <td>created_at</td>
        <td>string</td>
        <td>发出私信的时间</td>
    </tr>
    <tr>
        <td>sender_screen_name</td>
        <td>string</td>
        <td>发出私信的用户昵称</td>
    </tr>
    <tr>
        <td>recipient_screen_name</td>
        <td>string</td>
        <td>收到私信的用户昵称</td>
    </tr>
    <tr>
        <td>sender</td>
        <td>object</td>
        <td>发出私信的用户信息, 详情参见<a href="../user/show">User Show</a></td>
    </tr>
    <tr>
        <td>recipient</td>
        <td>object</td>
        <td>收到私信的用户信息, 详情参见<a href="../user/show">User Show</a></td>
    </tr>
</table>
