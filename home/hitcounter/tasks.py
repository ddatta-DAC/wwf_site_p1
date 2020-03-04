from huey.contrib.djhuey import db_task

from .models import Hit


@db_task()
def save_hit(user_pk, view):
    Hit.objects.create(user_id=user_pk, view=view)
