# Generated by Django 2.1.1 on 2018-10-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('championship', '0002_auto_20180923_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructorsChampionshipResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DriversChampionshipResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.Driver')),
            ],
        ),
        migrations.RemoveField(
            model_name='constructorschampionship',
            name='season',
        ),
        migrations.RemoveField(
            model_name='constructorschampionship',
            name='team',
        ),
        migrations.RemoveField(
            model_name='driverschampionship',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='driverschampionship',
            name='season',
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ('-year',)},
        ),
        migrations.DeleteModel(
            name='ConstructorsChampionship',
        ),
        migrations.DeleteModel(
            name='DriversChampionship',
        ),
        migrations.AddField(
            model_name='driverschampionshipresult',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers_result', to='championship.Season'),
        ),
        migrations.AddField(
            model_name='constructorschampionshipresult',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='constructors_result', to='championship.Season'),
        ),
        migrations.AddField(
            model_name='constructorschampionshipresult',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.Team'),
        ),
    ]
