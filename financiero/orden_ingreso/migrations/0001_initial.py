# Generated by Django 2.2.4 on 2019-10-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], max_length=15)),
                ('fecha', models.CharField(max_length=12)),
                ('cod_orden_ing', models.CharField(blank=True, max_length=15)),
                ('numeroTramite', models.PositiveIntegerField()),
                ('numeroFactura', models.PositiveIntegerField()),
                ('ruc_ci', models.CharField(max_length=13)),
                ('razon_nombres', models.CharField(max_length=50)),
                ('centroCosto', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('formaPago', models.CharField(choices=[('cheque', 'Cheque'), ('transferencia', 'Transferencia'), ('deposito', 'Depósito'), ('tarjeta', 'Tarjeta de Crédito')], default='cheque', max_length=30)),
                ('valor', models.FloatField()),
                ('anexo', models.FileField(upload_to='uploads/')),
                ('fechaPago', models.CharField(max_length=12)),
                ('numeroDocumento', models.PositiveIntegerField()),
                ('banco', models.CharField(max_length=30)),
                ('emisoraTarjeta', models.CharField(blank=True, choices=[('visa', 'Visa'), ('mastercard', 'Mastercard'), ('american', 'American Express'), ('diners', 'Diners'), ('discover', 'Discover')], help_text='Obligatorio con Tarjeta Crédito.', max_length=20)),
                ('estado', models.BooleanField(blank=True, default=None, null=True)),
            ],
            options={
                'ordering': ['-cod_orden_ing'],
            },
        ),
    ]
