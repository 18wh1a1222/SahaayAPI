# Generated by Django 3.0.1 on 2022-01-31 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadharId', models.CharField(max_length=12, unique=True)),
                ('phno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('dop', models.DateField()),
                ('doe', models.DateField()),
                ('lastDay', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Needs',
            fields=[
                ('needId', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=300)),
                ('pay', models.IntegerField()),
                ('dop', models.DateField()),
                ('doc', models.DateField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('aadharNo', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('type', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackNeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.IntegerField()),
                ('dop', models.DateField()),
                ('desc', models.CharField(blank=True, max_length=100)),
                ('needId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sahaay.Needs')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sahaay.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sahaay.Events')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sahaay.Users')),
            ],
        ),
        migrations.AddField(
            model_name='needs',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sahaay.Users'),
        ),
        migrations.AddField(
            model_name='events',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sahaay.Users'),
        ),
    ]
