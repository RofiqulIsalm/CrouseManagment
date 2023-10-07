# Generated by Django 4.2.3 on 2023-10-05 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_profile', models.ImageField(upload_to='Media/author')),
                ('name', models.CharField(max_length=100, null=True)),
                ('about_author', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(null=True, upload_to='Media/featured_img')),
                ('featured_video', models.CharField(max_length=300, null=True)),
                ('title', models.CharField(max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0, null=True)),
                ('discount', models.IntegerField(null=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=500, null=True)),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
                ('lavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.lavel')),
            ],
        ),
    ]