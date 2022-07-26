# Generated by Django 4.0.6 on 2022-07-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('episode_id', models.IntegerField()),
                ('opening_crawl', models.TextField(max_length=1000)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(blank=True, max_length=10)),
                ('mass', models.CharField(blank=True, max_length=10)),
                ('hair_color', models.CharField(blank=True, max_length=20)),
                ('skin_color', models.CharField(blank=True, max_length=20)),
                ('eye_color', models.CharField(blank=True, max_length=20)),
                ('birth_year', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('rotation_period', models.CharField(max_length=40)),
                ('orbital_period', models.CharField(max_length=40)),
                ('diameter', models.CharField(max_length=40)),
                ('climate', models.CharField(max_length=40)),
                ('gravity', models.CharField(max_length=40)),
                ('terrain', models.CharField(max_length=40)),
                ('surface_water', models.CharField(max_length=40)),
                ('population', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('manufacturer', models.CharField(max_length=80)),
                ('cost_in_credits', models.CharField(max_length=40)),
                ('length', models.CharField(max_length=40)),
                ('max_atmosphering_speed', models.CharField(max_length=40)),
                ('crew', models.CharField(max_length=40)),
                ('passengers', models.CharField(max_length=40)),
                ('cargo_capacity', models.CharField(max_length=40)),
                ('consumables', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('classification', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('average_height', models.CharField(max_length=40)),
                ('skin_colors', models.CharField(max_length=200)),
                ('hair_colors', models.CharField(max_length=200)),
                ('eye_colors', models.CharField(max_length=200)),
                ('average_lifespan', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=40)),
                ('homeworld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw.planet')),
                ('people', models.ManyToManyField(related_name='species', to='sw.people')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='sw.planet'),
        ),
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historic', to='sw.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='characters',
            field=models.ManyToManyField(blank=True, related_name='films', to='sw.people'),
        ),
        migrations.AddField(
            model_name='film',
            name='planets',
            field=models.ManyToManyField(blank=True, related_name='films', to='sw.planet'),
        ),
        migrations.AddField(
            model_name='film',
            name='species',
            field=models.ManyToManyField(blank=True, related_name='films', to='sw.species'),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sw.transport')),
                ('vehicle_class', models.CharField(max_length=40)),
                ('pilots', models.ManyToManyField(blank=True, related_name='vehicles', to='sw.people')),
            ],
            options={
                'abstract': False,
            },
            bases=('sw.transport',),
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sw.transport')),
                ('hyperdrive_rating', models.CharField(max_length=40)),
                ('MGLT', models.CharField(max_length=40)),
                ('starship_class', models.CharField(max_length=40)),
                ('pilots', models.ManyToManyField(blank=True, related_name='starships', to='sw.people')),
            ],
            options={
                'abstract': False,
            },
            bases=('sw.transport',),
        ),
        migrations.AddField(
            model_name='film',
            name='starships',
            field=models.ManyToManyField(blank=True, related_name='films', to='sw.starship'),
        ),
        migrations.AddField(
            model_name='film',
            name='vehicles',
            field=models.ManyToManyField(blank=True, related_name='films', to='sw.vehicle'),
        ),
    ]
