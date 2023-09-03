# Generated by Django 4.2.4 on 2023-09-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcategory',
            name='categoryThrough',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='postThrough',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postCategory',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('T', 'Танки'), ('HM', 'Хилы'), ('DD', 'ДД'), ('TrM', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('FM', 'Кузнецы'), ('LM', 'Кожевники'), ('PM', 'Зельевары'), ('WM', 'Мастера заклинаний')], default='T', max_length=3, verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]