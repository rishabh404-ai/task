# Generated by Django 3.1.2 on 2020-10-12 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RegisteredUsers', to='app.register')),
            ],
        ),
    ]