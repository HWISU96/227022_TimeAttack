# Generated by Django 4.0.6 on 2022-07-22 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_jobpostactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writing', models.CharField(max_length=128)),
                ('submitted', models.CharField(max_length=128)),
                ('under_review', models.CharField(max_length=128)),
                ('interview_planned', models.CharField(max_length=128)),
                ('in_recruitment_progress', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'apply',
            },
        ),
        migrations.AddField(
            model_name='jobpostactivity',
            name='apply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.apply'),
        ),
    ]
