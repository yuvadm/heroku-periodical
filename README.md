# Heroku Periodical

A skeleton app based on Heroku/Python/Celery that runs a single worker executing periodical tasks.

This skeleton can be used to quickly run periodical tasks on the Heroku platform using an arbitrary `timedelta` or `crontab` entry. The code is based on a single worker which runs with an integrated `celery beat` scheduler to avoid using a separate process just for scheduling. Redis is used as the broker, based on the `redistogo:nano` plan.

## Deployment

```bash
 $ heroku create
 $ heroku addons:add redistogo:nano
 $ git push heroku master
 $ heroku ps:scale worker=1
 ```
