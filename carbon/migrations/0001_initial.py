# Generated by Django 3.2.3 on 2021-05-28 09:09
from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Carbon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('carbonfootprint_score', models.IntegerField()),
            ],
        ),
    ]
