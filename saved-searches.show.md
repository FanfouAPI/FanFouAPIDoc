#GET: /saved_searches/show

返回搜索关键字的详细信息

##路径

    http://api.fanfou.com/saved_searches/show.[json|xml|rss]

##调用方法

    GET

##限制条件

    用户登录

##参数:

###id

- 作用: 指定需要浏览的关键字id

- 格式: `id=query_id`

- 字段说明: 必选

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

        返回一个`saved search object`，`saved search object`的格式参见示例

##示例

###请求URL

``curl -u u:pwd http://api.fanfou.com/saved_searches/show.json?id=21071``

###返回结果

    {
        "id": 21071,
        "query": "fanfou|test",
        "name": "fanfou|test",
        "created_at": "Thu Nov 10 09:05:03 +0000 2011"
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
        <td>int</td>
        <td>收藏搜索关键字id</td>
    </tr>
    <tr>
        <td>query</td>
        <td>string</td>
        <td>收藏的搜索关键字</td>
    </tr>
    <tr>
        <td>name</td>
        <td>string</td>
        <td>收藏搜索关键字别名</td>
    </tr>
    <tr>
        <td>created_at</td>
        <td>string</td>
        <td>关键字收藏时间</td>
    </tr>
</table>
