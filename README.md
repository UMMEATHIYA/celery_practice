# celery_practice



<h2> Celery Commands </h2>
<ol>
  <li>docker run -it -p 6379:6379 -d --net-alias redisserver --name redis redis</li>
  <li>celery==5.1.0
      Django==3.2.3
      redis==3.5.3
    requests </li>
  <li>pip install --no-cache-dir -r requirements.txt</li>
  <li>celery -A Task worker --loglevel=info</li>
  <li>celery -A test_celery worker --loglevel=info --logfile="/smartedge/docker-mem.txt"</li>
