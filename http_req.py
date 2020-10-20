import requests
import threading


def http(reqid):
    url = "http://127.0.0.1:5000/admins/"+str(reqid)
    http_req = requests.get(url)
    print(http_req.content)

count = 0
for index_range in range(5000):
    threadX1 = threading.Thread(target=http(count))
    threadX1.start()
    count = count + 1
    print("Thread no.", count ,"Started")