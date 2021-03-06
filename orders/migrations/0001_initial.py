# Generated by Django 2.0.3 on 2020-03-12 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_quantity', models.IntegerField()),
                ('pasta_quantity', models.IntegerField()),
                ('salads_quantity', models.IntegerField()),
                ('dinner_platter_quantity', models.IntegerField()),
                ('subs_quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dinner_platters', models.ManyToManyField(to='orders.DinnerPlatters')),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('sub_type', models.CharField(max_length=50)),
                ('topping_quantity', models.IntegerField()),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='SubAddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='pasta',
            field=models.ManyToManyField(to='orders.Pasta'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pizza',
            field=models.ManyToManyField(to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='orders',
            name='salads',
            field=models.ManyToManyField(to='orders.Salads'),
        ),
        migrations.AddField(
            model_name='orders',
            name='sub_add_on',
            field=models.ManyToManyField(to='orders.SubAddOn'),
        ),
        migrations.AddField(
            model_name='orders',
            name='subs',
            field=models.ManyToManyField(to='orders.Subs'),
        ),
        migrations.AddField(
            model_name='orders',
            name='topping',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
