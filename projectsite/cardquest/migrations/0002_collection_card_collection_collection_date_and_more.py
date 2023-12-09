# Generated by Django 4.2.7 on 2023-11-23 05:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.pokemoncard'),
        ),
        migrations.AddField(
            model_name='collection',
            name='collection_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.trainer'),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='abilities',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='attack',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='card_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='card_type',
            field=models.CharField(blank=True, choices=[('ADF', 'FADS'), ('ADFF', 'DSDF')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='evolution_stage',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='hp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='rarity',
            field=models.CharField(blank=True, choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='weakness',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
