# Generated by Django 2.2 on 2022-06-19 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20220619_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='banco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colaboradors', to='core.Banco'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='banco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proveedors', to='core.Banco'),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terrenos', to='core.Proyecto'),
        ),
        migrations.AlterField(
            model_name='terrenodetalle',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terrenodetalles', to='core.Colaborador'),
        ),
        migrations.AlterField(
            model_name='terrenomovilizacion',
            name='conductores',
            field=models.ManyToManyField(related_name='terrenomovilizacions', to='core.Colaborador'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vuelos', to='core.Colaborador'),
        ),
    ]
