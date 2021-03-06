# Generated by Django 2.0.6 on 2020-05-12 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20200422_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipo',
            name='status',
            field=models.BooleanField(default=False, verbose_name='发行状态'),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='content',
            field=models.TextField(default='募集资金的主要用于公司主营业务，应当符合国家产业政策、投资管理、环境保护、土地管理以及其他法律、法规和规章的规定。', verbose_name='募集资金的运用'),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='content2',
            field=models.TextField(default='股权分配都遵循三个原则：公平、效率、控制力', verbose_name='股权分配'),
        ),
    ]
