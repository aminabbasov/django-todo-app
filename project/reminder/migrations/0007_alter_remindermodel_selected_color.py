# Generated by Django 4.1.1 on 2022-10-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0006_alter_remindermodel_selected_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remindermodel',
            name='selected_color',
            field=models.CharField(choices=[('hsv(0,100,100)', 'AAСolorless'), ('hsv(0,100,100)', 'BBRed'), ('hsv(31,100,100)', 'CCOrange'), ('hsv(60,100,100)', 'DDYellow'), ('hsv(128,100,87)', 'EEGreen'), ('hsv(180,100,100)', 'FFCyan'), ('hsv(209,100,100)', 'GGBlue'), ('hsv(272,81,89)', 'HHPurple')], default='#ff000000', max_length=100),
        ),
    ]