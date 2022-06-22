# Generated by Django 2.2 on 2022-06-15 03:20

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220614_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vuelo',
            old_name='fecha_inicio',
            new_name='fecha_vuelo',
        ),
        migrations.AddField(
            model_name='vuelo',
            name='documento_adjunto_1',
            field=models.FileField(null=True, upload_to=core.models.vuelo_path_1),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='documento_adjunto_2',
            field=models.FileField(null=True, upload_to=core.models.vuelo_path_2),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='documento_adjunto_3',
            field=models.FileField(null=True, upload_to=core.models.vuelo_path_3),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='monto',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='numero_vuelo',
            field=models.CharField(blank=True, max_length=30, null=True),
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