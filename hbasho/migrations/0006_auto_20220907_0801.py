# Generated by Django 3.2.15 on 2022-09-07 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hbasho', '0005_auto_20220907_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='wrestlers',
            field=models.ManyToManyField(through='hbasho.TournamentWrestler', to='hbasho.Wrestler'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='champion', to='hbasho.wrestler'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('HBASHO_MAKUUCHI', 'Makuuchi'), ('HBASHO_JURYO', 'Juryo')], max_length=128)),
                ('order_by', models.IntegerField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hbasho.tournament')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='winner', to='hbasho.wrestler')),
                ('wrestler_east', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='wrestler_east', to='hbasho.wrestler')),
                ('wrestler_west', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='wrestler_west', to='hbasho.wrestler')),
            ],
        ),
    ]
