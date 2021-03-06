# Generated by Django 2.2 on 2022-06-14 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220613_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='terrenodetalle',
            name='cantidad_dias',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terrenodetalle',
            name='monto_diario',
            field=models.IntegerField(null=True),
        ),
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
