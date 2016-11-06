# -*- coding:utf8 -*-
from wechat_sdk import WechatBasic, WechatConf

conf = WechatConf(
	token='helloworld',
	appid='wx5effce4e20e97a20',
	appsecret='2fdd281fd8a8fa78ec94859c3bdf7501',
	encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
	encoding_aes_key=''  # 如果传入此值则必须保证同时传入 token, appid
)

wechat = WechatBasic(conf=conf)

MENU_DATA = {
	'button': [
		{
			'type': 'click',
			'name': '今日歌曲',
			'key': 'V1001_TODAY_MUSIC'
		},
		{
			'type': 'click',
			'name': '歌手简介',
			'key': 'V1001_TODAY_SINGER'
		},
		{
			'name': '菜单',
			'sub_button': [
				{
					'type': 'view',
					'name': '百度',
					'url': 'http://www.soso.com/'
				},
				{
					'type': 'view',
					'name': '视频',
					'url': 'http://v.qq.com/'
				},
				{
					'type': 'click',
					'name': '赞一下我们',
					'key': 'V1001_GOOD'
				}
			]
		}
	]
}
