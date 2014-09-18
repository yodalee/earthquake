# -*- coding: utf-8 -*-

# Scrapy settings for earthquake project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'earthquake'

SPIDER_MODULES = ['earthquake.spiders']
NEWSPIDER_MODULE = 'earthquake.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'earthquake (+http://www.yourdomain.com)'
