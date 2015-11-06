# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='choreType',
            field=models.CharField(default='R', max_length=1, choices=[('A', 'Automatic'), ('R', 'Reported')]),
        ),
        migrations.AlterField(
            model_name='chore',
            name='periodHours',
            field=models.IntegerField(default=168),
        ),
        migrations.AlterField(
            model_name='chore',
            name='status',
            field=models.CharField(default='D', max_length=1, choices=[('D', 'Done'), ('U', 'Unimportant'), ('N', 'Needs Doing'), ('I', 'Important!'), ('V', 'Very Urgent!!!')]),
        ),
    ]
