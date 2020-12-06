import json
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)

def publish_data_on_redis(data, channel_name):
    redis_client.publish(channel_name, json.dumps(data))

def subscribe(topic):
    redis_sub = redis_client.pubsub()
    return redis_sub
    
def get_data(redis_sub, topic):
    redis_sub.subscribe(topic)
    for item in redis_sub.listen():
        print(item["data"])
        i = item
        break
    return i