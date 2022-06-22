# Generated by Django 2.2 on 2022-06-22 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0019_auto_20220620_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='terrenomovilizacion',
            name='conductores',
        ),
        migrations.RemoveField(
            model_name='terrenomovilizacion',
            name='name',
        ),
        migrations.RemoveField(
            model_name='terrenomovilizacion',
            name='slug',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='comuna',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='terrenomovilizacion',
            name='monto',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='banco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colaboradors', to='core.Banco'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='banco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proveedors', to='core.Banco'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='banco_cuenta',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='banco_tipo_cuenta',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='contacto_email',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='contacto_nombre',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='contacto_rut',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='contacto_telefono',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
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
            name='terreno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terrenomovilizacions', to='core.Terreno'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vuelos', to='core.Colaborador'),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('numero_reserva', models.CharField(max_length=10)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to=settings.AUTH_USER_MODEL)),
                ('terreno_movilizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='core.TerrenoMovilizacion')),
                ('tipo_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='core.Colaborador')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='MovimientosContables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('monto', models.TextField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('tipo_movimiento', models.CharField(max_length=20)),
                ('tabla', models.CharField(max_length=30)),
                ('pk_referencia', models.IntegerField()),
                ('medio_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientoscontabless', to='core.MedioPago')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
