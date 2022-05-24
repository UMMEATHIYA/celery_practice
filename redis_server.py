# celery -A tasks worker --loglevel=info

from tasks import add 

res = add.delay(2,5)
print(res)

res.ready()
res.get(timeout=1)