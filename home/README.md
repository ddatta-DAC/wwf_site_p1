To connect to prod database locally, port forward to your machine. The database is used read-only by the code (by convention only, be careful).

```
ssh -N -f -L localhost:3306:localhost:3306 dac-wwf.cs.vt.edu
```
