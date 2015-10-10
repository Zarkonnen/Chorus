# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choreType', models.CharField(max_length=1, choices=[(b'A', b'Automatic'), (b'R', b'Reported')])),
                ('name', models.CharField(max_length=100)),
                ('periodHours', models.IntegerField()),
                ('status', models.CharField(max_length=1, choices=[(b'D', b'Done'), (b'U', b'Unimportant'), (b'N', b'Needs Doing'), (b'I', b'Important!'), (b'V', b'Very Urgent!!!')])),
                ('lastUpdated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
