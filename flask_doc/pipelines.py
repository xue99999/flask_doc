# -*- coding: utf-8 -*-
import re
import json
import redis

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        item['text'] = re.sub('\s+', ' ', item['text'])
        self.redis.lpush('flask_doc:items', json.dumps(dict(item)))
        return item


    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
