Redis, which stands for "REmote DIctionary Server," is an open-source, in-memory data storage system. It is often referred to as a data structure server because it can store various types of data structures, including strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, and more. Redis is designed for high-performance, low-latency data storage and retrieval.

Here are some key features and use cases of Redis:

1. In-Memory Data Store: Redis stores all data in RAM, which makes it extremely fast for read and write operations.

2. Key-Value Store: Data is stored as key-value pairs, allowing for efficient and straightforward data access.

3. Data Structures: Redis supports a wide range of data structures, making it suitable for various use cases, such as caching, real-time analytics, messaging, and more.

4. Pub-Sub Messaging: Redis provides a publish-subscribe (pub-sub) messaging system that enables real-time message broadcasting to multiple subscribers.

5. Persistence: While Redis primarily stores data in memory, it offers options for data persistence to disk, allowing data to be recovered after server restarts.

6. Clustering: Redis can be configured in a cluster mode to distribute data across multiple nodes, improving scalability and high availability.

7. Caching: Redis is commonly used as a cache because of its high-speed data retrieval capabilities, which can significantly reduce the load on backend databases.

8. Real-Time Analytics: Redis can be used to store and analyze real-time data, making it suitable for applications that require up-to-the-minute insights.

9. Session Store: It's often used to store user sessions in web applications, allowing for quick session data retrieval.

10. Geospatial Data: Redis includes geospatial data structures and commands, making it suitable for location-based applications.

11. Queues: Redis can be used to implement message queues and task queues, helping with background processing and distributed systems.

Redis is popular in a wide range of applications, including web and mobile apps, gaming, real-time analytics, IoT (Internet of Things), and more. Its speed and versatility make it a valuable tool for managing and processing various types of data in memory.

```
sudo apt install redis-server
redis-cli
ping

set 321434 -1
set 588432  "(33.43, 89.21)"

get 588432

```


if you wnat to set password for redis:
```
sudo vim /etc/redis/redis.conf

# uncomment below: 
requirepass foo



```



```
set name test EX 20  # expire after 20 second
PERSIST name

# get key with regular expersion
keys 58*
keys na*

type name


# delete key
del name


set name1 sdf
set name2 seq

mget name1 name2

mset key1 value1 key2 value2




```


### Hash structure
```
 hset user1 name ali
 hset user1 age 32
 hset user1 city isfa


hget user1 city
hget user1 age

hgetall user1
```


## lists
```
LPUSH teh name1 name2 name3
RPUSH teh name4
LRANGE teh 0 10


```