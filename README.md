
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
</ol>
  
  <h1> OUTPUT - <a href="https://docs.celeryq.dev/en/stable/userguide/canvas.html">Official Document Link</a></h1>
  <img width="723" alt="celery1" src="https://user-images.githubusercontent.com/43459908/169967128-348b448a-d106-4568-8245-c2ec4339edde.PNG">

  <h3>Concepts</h3>
  <ol>
  <h4><b><li> Signature </li></b></h4>
  <ul>
    <li> Generally arguments </li>
    <li> placeholders for running tasks </li>
  </ul>
    <h4><b> OUTPUT </b></h4>
    <img width="414" alt="celery5" src="https://user-images.githubusercontent.com/43459908/169971402-acf492d0-6813-4aa9-9c6d-e7f27f445ef5.PNG">
    <img width="416" alt="celery6" src="https://user-images.githubusercontent.com/43459908/169971635-93d70e2f-e225-4863-9ce6-78a28af76400.PNG">

  
  <ol>

