#POST: /account/update_profile_background_image

通过 API 更新用户自定义背景图片

##路径
    http://api.fanfou.com/account/update_profile_background_image.[json|xml]

##调用方法
    POST

##条件限制
    用户登录

##参数： 

###image 

- 作用：指定上传背景图片
- 格式：
- 字段说明：必选

###tile

- 作用：指定是否平平铺
- 格式： `tile=true`
- 字段说明： 可选

##返回值：

###成功
- HTTP Status Code

        `200 OK HTTP/1.1`

- 返回值

###失败：返回错误信息

##示例
