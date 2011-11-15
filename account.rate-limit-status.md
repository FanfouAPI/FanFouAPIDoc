#GET: /account/rate_limit_status

获取 API 限制

##路径

    http://api.fanfou.com/account/rate_limit_status.[json|xml]

##调用方法

    GET

##条件限制

    需要登陆

##参数

    无

##返回值

成功

- HTTP Statuse Code
    
    `200 OK HTTP/1.1`

{"reset_time":"Mon Nov 14 08:57:28 +0000 2011","remaining_hits":150,"hourly_limit":150,"reset_time_in_seconds":1321261048}

失败
