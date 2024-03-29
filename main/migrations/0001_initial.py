# Generated by Django 3.2.6 on 2024-02-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('status', models.CharField(default='Submitted', max_length=100)),
            ],
        ),
    ]
