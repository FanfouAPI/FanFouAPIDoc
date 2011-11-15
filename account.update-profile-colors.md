#POST: /account/update_profile_colors

通过 API 更新用户自定义颜色

##路径
	http://api.fanfou.com/account/update_profile_colors.[json|xml]

##调用方法
	POST


##条件限制
	需要登陆

##参数： 

###profile_background_color

- 作用：用户自定义背景颜色
- 格式：#FFFFFF;
- 字段说明：可选

###profile_text_color 

- 作用：用户自定义文字颜色 
- 格式：#FFFFFF;
- 字段说明：可选

###profile_link_color

- 作用：用户自定义链接颜色 
- 格式：#FFFFFF;
- 字段说明：可选

###profile_sidebar_fill_color

- 作用：用户自定义侧栏颜色 
- 格式：#FFFFFF;
- 字段说明：可选

###profile_sidebar_border_color 

- 作用：用户自定义侧栏边框颜色 
- 格式：#FFFFFF;
- 字段说明：可选

##返回值：

###成功：
		
- HTTP Status Code

        `200 OK HTTP/1.1`

###失败：
