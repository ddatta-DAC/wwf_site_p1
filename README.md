# Server

To pull changes:
```
sudo su django
cd ~/wwf_site_p1/home/
git pull origin master
```

Possibly need
```
./manage.py migrate
./manage.py collectstatic
pip install -r requirements.txt
```

Definitely need
```
exit
sudo supervisorctl restart wwf  # restart django process
```


## Supervisor

Config in `/etc/supervisor/conf.d/wwf.conf`

## Hits

To get hit counts in list of lists format that you could write out to a CSV. Do this on the server:

```
sudo su django
cd ~/wwf_site_p1/home/
./manage shell
```

In the shell do:

```
from hitcounter.models import *
hits = [[h.user.username, h.view, h.created.strftime('%Y-%m-%d')] for h in Hit.objects.all()]
```

Do whatever you need with `hits`

# Local

To connect to prod database locally, port forward to your machine. The database is used read-only by the code (by convention only, be careful).

```
ssh -N -f -L localhost:3306:localhost:3306 dac-wwf.cs.vt.edu
```
