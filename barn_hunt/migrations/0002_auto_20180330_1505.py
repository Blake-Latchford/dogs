# Generated by Django 2.0.3 on 2018-03-30 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barn_hunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barn_hunt.Dog')),
                ('trial_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barn_hunt.TrialClass')),
            ],
        ),
        migrations.AddField(
            model_name='trialclass',
            name='registrations',
            field=models.ManyToManyField(through='barn_hunt.Registration', to='barn_hunt.Dog'),
        ),
    ]
