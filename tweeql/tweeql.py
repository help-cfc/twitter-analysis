import psycopg2
import redis
import hashlib
import time

redis_sk = redis.StrictRedis.from_url("rediss://admin:BGXUJOSJVOSHTTSK@portal1122-32.bmix-dal-yp-9ed0e99e-4d7f-42bc-bd29-68826c7e3ca3.261504680.composedb.com:57374")


try:
    conn = psycopg2.connect("postgres://admin:BDSRQAQSNPMWDLWF@sl-us-south-1-portal.24.dblayer.com:57376/compose")
except:
    print("unable to connect to database")

cur = conn.cursor()



while True:
    packed = redis_sk.brpop(['queue:tweet'], 10)

    print(packed)

    if not packed:
        time.sleep(10)
        continue

    if "coordinates" not in packed['queue:tweet']:
        continue
    if "place" not in packed['queue:tweet']:
        continue
    if "created_at" not in packed['queue:tweet']:
        continue

    # locations
    coords = packed['queue:tweet']["coordinates"]
    addr = packed['queue:tweet']["place"]
    zipc = 0
    city = "null"
    l = hashlib.sha1()
    l.update(coords)
    l.update(addr)
    l.update(zipc)
    l.update(city)
    print(coords)
    print(addr)
    print(zipc)
    print(city)
    l_key = l.digest()

    # disaster
    uuid = l_key
    tp = "null"
    ts = packed['queue:tweet']["created_at"]
    d = hashlib.sha1()
    d.update(uuid)
    d.update(tp)
    d.update(ts)
    d_key = d.digest()


    cur.execute("""insert into disaster_node.disaster
        (key, uuid, type, ts) values ({}, {}, {}, {})
        ;""".format(d_key, uuid, tp, ts))
    cur.execute("""insert into disaster_node.location
        (key, coords, zip, city) values ({}, {}, {}, {})
        ;""".format(l_key, coords, zipc, city))
