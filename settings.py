#!/usr/bin/env python
#coding:utf-8

import web
import memcache
from web.contrib.template import render_mako

#数据库配置
db = web.database(dbn = 'mysql', db = 'davidblog', user='root', pw = 'root')

#memcache配置
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

#render_mako配置
render = render_mako(
        directories = ['/home/icefox/davidblog/templates'],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
    )
