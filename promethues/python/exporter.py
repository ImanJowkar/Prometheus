import prometheus_client as prom
import random
import time
import numpy as np


counter1 = prom.Counter('counter1_func', 'the name of counter1')
counter2 = prom.Counter('counter2_func', 'the name of counter2')


gauge1 = prom.Gauge("sin_function", 'this is sin(x) function')


prom.start_http_server(8003)
print("app listen on port 8003")
i=0
while True:
    
    counter1.inc(random.randint(0, 100))
    counter2.inc(random.randint(0, 100))
    gauge1.set(10 * np.sin(random.randint(0, 100)))
    time.sleep(5)
    i+=5
    if i == 100:
        i = 0
    