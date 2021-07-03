# Generated by Django 3.1.7 on 2021-07-03 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default='user_default.png', null=True, upload_to='users_profile')),
                ('country', models.CharField(choices=[('UK', 'United Kingdom of Great Britain and Northern Ireland'), ('CA', 'CANADA'), ('AU', 'AUSTRALIA'), ('FR', 'FRANCE'), ('US', 'UNITED STATES'), ('HK', 'HONG KONG'), ('KR', 'KOREA, REPUBLIC OF'), ('DE', 'GERMANY, FEDERAL REPUBLIC OF GERMANY'), ('CH', 'SWITZERLAND'), ('RU', 'Russian Federation'), ('IL', 'ISRAEL'), ('NZ', 'New Zealand'), ('IT', 'ITALY'), ('MY', 'Malaysia'), ('SG', 'Singapore'), ('SE', 'SWEDEN'), ('IN', 'INDIA'), ('FI', 'FINLAND'), ('CN', 'CHINA'), ('TW', 'TAIWAN,REPUBLIC OF CHINA'), ('NA', 'OTHER')], default='TW', max_length=50)),
                ('gender', models.BooleanField(default=True)),
                ('BOD', models.DateField(null=True)),
                ('self_introduction', models.TextField(blank=True, default='')),
                ('expertise', models.TextField(blank=True)),
                ('upload_date', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
