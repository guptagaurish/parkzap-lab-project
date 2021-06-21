# Generated by Django 3.1.5 on 2021-05-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('mothername', models.CharField(max_length=30)),
                ('fathername', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('contact', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('physicallychallged', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=20)),
                ('admissiontype', models.CharField(max_length=20)),
                ('admissiondate', models.CharField(max_length=30)),
                ('bloodgroup', models.CharField(max_length=4)),
                ('aadhar', models.IntegerField()),
                ('gr', models.IntegerField()),
                ('rteinfo', models.CharField(max_length=30)),
                ('studylang', models.CharField(max_length=30)),
                ('rewstu', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=30)),
                ('pemail', models.EmailField(max_length=30)),
                ('pcontact', models.IntegerField(max_length=30)),
                ('religion', models.CharField(max_length=30)),
                ('cast', models.CharField(max_length=30)),
                ('subcast', models.CharField(max_length=30)),
                ('previousSchool', models.CharField(max_length=30)),
                ('yearofpass', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('schoolRecog', models.CharField(max_length=30)),
                ('schoolrollno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
