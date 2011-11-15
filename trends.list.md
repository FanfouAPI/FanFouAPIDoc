#GET /trends/list

列出饭否热门话题

##路径

    http://api.fanfou.com/trends/list.[json|xml|rss]

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

        返回的格式参见示例

##示例

###请求URL

``curl -u u:pwd http://api.fanfou.com/trends/list.json``

###返回结果

    {"as_of":"Thu Nov 10 09:57:23 +0000 2011",
     "trends":[{"name":"萤火一号",
                "query":"萤火一号|火星|变轨",
                "url":"http://fanfou.com/q/%E8%90%A4%E7%81%AB%E4%B8%80%E5%8F%B7%7C%E7%81%AB%E6%98%9F%7C%E5%8F%98%E8%BD%A8"},
                {"name":"土耳其地震",
                 "query":"土耳其|地震",
                 "url":"http://fanfou.com/q/%E5%9C%9F%E8%80%B3%E5%85%B6%7C%E5%9C%B0%E9%9C%87"
                },
                {"name":"《失恋33天》",
                 "query":"33天|白百何",
                 "url":"http://fanfou.com/q/33%E5%A4%A9%7C%E7%99%BD%E7%99%BE%E4%BD%95"
                },
                {"name":"股市大跌",
                 "query":"股市|国债",
                 "url":"http://fanfou.com/q/%E8%82%A1%E5%B8%82%7C%E5%9B%BD%E5%80%BA"
                },
                {"name":"光棍节",
                 "query":"光棍|神棍|六一",
                 "url":"http://fanfou.com/q/%E5%85%89%E6%A3%8D%7C%E7%A5%9E%E6%A3%8D%7C%E5%85%AD%E4%B8%80"
                },
                {"name":"北方降温",
                 "query":"降温|冷空气",
                 "url":"http://fanfou.com/q/%E9%99%8D%E6%B8%A9%7C%E5%86%B7%E7%A9%BA%E6%B0%94"
                }
            ]
    }

###字段说明

<table>
    <tr>
        <td>字段返回值</td>
        <td>字段类型</td>
        <td>字段说明</td>
    </tr>
    <tr>
        <td>as_of</td>
        <td>string</td>
        <td>服务器时间(UTC)</td>
    </tr>
    <tr>
        <td>trends</td>
        <td>array</td>
        <td>trends object 数组</td>
    </tr>
</table>

trends object 字段说明

<table>
    <tr>
        <td>字段返回值</td>
        <td>字段类型</td>
        <td>字段说明</td>
    </tr>
    <tr>
        <td>name</td>
        <td>string</td>
        <td>热词名称</td>
    </tr>
    <tr>
        <td>query</td>
        <td>string</td>
        <td>热词搜索关键字</td>
    </tr>
    <tr>
        <td>url</td>
        <td>string</td>
        <td>饭否网站搜索链接</td>
    </tr>
</table>
