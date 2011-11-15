#GET: /users/show

返回好友或未设置隐私用户的信息

##路径

    http://api.fanfou.com/users/show.[json|xml|rss]

##调用方法

    GET

##限制条件

    用户登录, 目标用户为登录用户关注者或未设置隐私

##参数:

###id

- 作用: 指定需要浏览的用户id

- 格式: `id=user_id`

- 字段说明: 可选

###mode

- 作用: 当`mode=default`(默认)时,返回消息中用户信息包含用户自定义profile

- 格式: `mode=mode_str`

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

##示例

###请求URL

``GET http://api.fanfou.com/users/show.json``

###返回结果

    {
        "id": "test",
        "name": "测试昵称",
        "screen_name": "测试昵称",
        "location": "北京 海淀区",
        "gender": "男",
        "birthday": "2105-03-11",
        "description": "测试帐号",
        "profile_image_url": "http://avatar3.fanfou.com/s0/00/5n/sk.jpg?1320913295",
        "profile_image_url_large": "http://avatar3.fanfou.com/l0/00/5n/sk.jpg?1320913295",
        "url": "http://fanfou.com/test",
        "protected": true,
        "followers_count": 9,
        "friends_count": 16,
        "favourites_count": 23,
        "statuses_count": 124,
        "following": false,
        "notifications": false,
        "created_at": "Sat Jun 09 23:56:33 +0000 2007",
        "utc_offset": 28800,
        "profile_background_color": "#ffffe5",
        "profile_text_color": "#004040",
        "profile_link_color": "#ff0000",
        "profile_sidebar_fill_color": "#ffefbf",
        "profile_sidebar_border_color": "#ffac80",
        "profile_background_image_url": "http://avatar.fanfou.com/b0/00/5n/sk_1320749993.jpg",
        "profile_background_tile": true,
        "status": {
            "created_at": "Thu Nov 10 09:37:34 +0000 2011",
            "id": "XRFWGErKgGI",
            "text": "这是神马？",
            "source": "<a href=\"http://abc.fanfouapps.com\" target=\"_blank\">ABC</a>",
            "truncated": false,
            "in_reply_to_lastmsg_id": "",
            "in_reply_to_user_id": "",
            "favorited": false,
            "in_reply_to_screen_name": ""
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
        <td>id</td>
        <td>string</td>
        <td>用户id</td>
    </tr>
    <tr>
        <td>name</td>
        <td>string</td>
        <td>用户姓名</td>
    </tr>
    <tr>
        <td>screen_name</td>
        <td>string</td>
        <td>用户昵称</td>
    </tr>
    <tr>
        <td>location</td>
        <td>string</td>
        <td>用户地址</td>
    </tr>
    <tr>
        <td>gender</td>
        <td>string</td>
        <td>用户性别</td>
    </tr>
    <tr>
        <td>birthday</td>
        <td>string</td>
        <td>用户生日信息</td>
    </tr>
    <tr>
        <td>description</td>
        <td>string</td>
        <td>用户自述</td>
    </tr>
    <tr>
        <td>profile_image_url</td>
        <td>string</td>
        <td>用户头像地址</td>
    </tr>
    <tr>
        <td>profile_image_url_large</td>
        <td>string</td>
        <td>用户高清头像地址</td>
    </tr>
    <tr>
        <td>url</td>
        <td>string</td>
        <td>用户页面地址</td>
    </tr>
    <tr>
        <td>protected</td>
        <td>boolean</td>
        <td>用户是否设置隐私保护</td>
    </tr>
    <tr>
        <td>followers_count</td>
        <td>int</td>
        <td>用户关注用户数</td>
    </tr>
    <tr>
        <td>friends_count</td>
        <td>int</td>
        <td>用户好友数</td>
    </tr>
    <tr>
        <td>favourites_count</td>
        <td>int</td>
        <td>用户收藏消息数</td>
    </tr>
    <tr>
        <td>statuses_count</td>
        <td>int</td>
        <td>用户消息数</td>
    </tr>
    <tr>
        <td>following</td>
        <td>boolean</td>
        <td>该用户是被当前登录用户关注</td>
    </tr>
    <tr>
        <td>notifications</td>
        <td>boolean</td>
        <td>当前登录用户是否已对该用户发出关注请求</td>
    </tr>
    <tr>
        <td>created_at</td>
        <td>string</td>
        <td>用户注册时间</td>
    </tr>
    <tr>
        <td>utc_offset</td>
        <td>int</td>
        <td>ref: <a href="http://en.wikipedia.org/wiki/UTC_offset" target="_blank">UTC offset</a></td>
    </tr>
    <tr>
        <td>profile_background_color</td>
        <td>string</td>
        <td>用户用户自定义页面背景颜色</td>
    </tr>
    <tr>
        <td>profile_text_color</td>
        <td>string</td> <td>用户用户自定义文字颜色</td>
    </tr>
    <tr>
        <td>profile_link_color</td>
        <td>string</td>
        <td>用户用户自定义链接颜色</td>
    </tr>
    <tr>
        <td>profile_sidebar_fill_color</td>
        <td>string</td>
        <td>用户用户自定义侧边栏颜色</td>
    </tr>
    <tr>
        <td>profile_sidebar_border_color</td>
        <td>string</td>
        <td>用户用户自定义侧边栏边框颜色</td>
    </tr>
    <tr>
        <td>profile_background_image_url</td>
        <td>string</td>
        <td>用户用户自定义背景图片地址</td>
    </tr>
    <tr>
        <td>profile_background_tile</td>
        <td>boolean</td>
        <td>是否平铺用户用户自定义背景图片地址</td>
    </tr>
    <tr>
        <td>status</td>
        <td>object</td>
        <td>用户发出的最后一条消息，其中各个字段参照<a href="/statuses/show">Statuses Show</a>中对应字段的解释</a></td>
    </tr>

</table>
