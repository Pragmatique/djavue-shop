# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-18 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Opened at')),
                ('closed_at', models.DateTimeField(blank=True, null=True, verbose_name='Closed at')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Is closed')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Is processed')),
                ('phone', models.CharField(max_length=32, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
                ('name', models.CharField(max_length=64, null=True, verbose_name='Contact name')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-count'],
            },
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]