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
```

Definitely need
```
exit
sudo supervisorctl restart wwf  # restart django process
```


## Supervisor

Config in `/etc/supervisor/conf.d/wwf.conf`


# Local

To connect to prod database locally, port forward to your machine. The database is used read-only by the code (by convention only, be careful).

```
ssh -N -f -L localhost:3306:localhost:3306 dac-wwf.cs.vt.edu
```
