# Generated by Django 3.1.7 on 2021-03-24 03:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20210323_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillBreakdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blurb', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('bill_link', models.URLField()),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billbreakdownauthor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='BreakdownItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('billbreakdown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.billbreakdown', verbose_name='Bill')),
            ],
            options={
                'verbose_name_plural': 'breakdown items',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Roundup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roundups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='Image')),
                ('breakdownitem', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.breakdownitem')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
    ]
