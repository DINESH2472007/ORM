# Generated by Django 5.1.3 on 2024-12-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankLoan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=30)),
                ('loan_amt', models.IntegerField()),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_acno', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
