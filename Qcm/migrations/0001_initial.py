# Generated by Django 2.1.5 on 2019-01-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=150)),
                ('answer', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Qcm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('dateEdited', models.DateField(auto_now=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('id_qcm', models.ForeignKey(on_delete='CASCADE', to='Qcm.Qcm')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='id_question',
            field=models.ForeignKey(on_delete='CASCADE', to='Qcm.Question'),
        ),
    ]
