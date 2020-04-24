# Generated by Django 2.0.6 on 2020-04-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_ipo_ipo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipo',
            name='content',
            field=models.TextField(default=models.CharField(max_length=20, verbose_name='公司名称'), verbose_name='募集资金的运用'),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='content2',
            field=models.TextField(default=models.CharField(max_length=20, verbose_name='公司名称'), verbose_name='股权分配'),
        ),
    ]