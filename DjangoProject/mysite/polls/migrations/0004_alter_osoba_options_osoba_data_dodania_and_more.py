# Generated by Django 4.2.16 on 2024-10-18 16:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Mezczyzna'), (2, 'Kobieta'), (3, 'Inne')], default=1),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='stanowisko',
            field=models.ForeignKey(db_column='Stanowisko_nazwa', on_delete=django.db.models.deletion.CASCADE, to='polls.stanowisko'),
        ),
    ]
