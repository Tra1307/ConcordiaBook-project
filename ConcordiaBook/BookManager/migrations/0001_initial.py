# Generated by Django 5.1.6 on 2025-03-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('edition', models.CharField(blank=True, max_length=200, null=True)),
                ('condition', models.CharField(choices=[('new', 'New'), ('used', 'Used'), ('old', 'Old'), ('damaged', 'Damaged')], max_length=50)),
                ('course_code', models.CharField(max_length=50)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]
