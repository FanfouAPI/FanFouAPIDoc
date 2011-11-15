#POST: /account/find_friends

通过手机通讯录查找好友

##路径

	http://api.fanfou.com/account/find_friends.json

##调用方法

	POST

##条件限制

	用户登录

##参数

###hashes
	
- 作用：指定通讯录信息hash类型和值
- 格式：`hashes=4;ddce269a1e3d054cae349621c198dd52`
- 字段说明： 
	
	- 参数有 hash type 和 hash value 组成，用 ; 分隔
	- hash type: 
		
		phone = 1
		msn = 2
		qq = 3
		email = 4
		gtalk = 7

	- hashv value: 是对应 hash type 的值的md5

##返回值

	［
		｛
			hash: $hash,
			type: $type,
			user: $userJson
		}+
	］
