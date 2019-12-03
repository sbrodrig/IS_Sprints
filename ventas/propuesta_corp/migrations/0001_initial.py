# Generated by Django 2.2.5 on 2019-12-02 23:45

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas_juridicas', '0001_initial'),
        ('reporte_contacto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropuestaCorporativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_propuesta', models.CharField(blank=True, max_length=20)),
                ('version', models.PositiveIntegerField()),
                ('nombre_propuesta', models.CharField(max_length=250)),
                ('estado', models.CharField(choices=[('SG', 'Seguimiento'), ('PD', 'Pendiente'), ('ACP', 'Aceptada'), ('NACP', 'No aceptada')], default='SG', max_length=15)),
                ('fecha_solicitud', models.CharField(max_length=12)),
                ('numero_participantes', models.PositiveIntegerField()),
                ('total_horas', models.TimeField()),
                ('cantidad_cursos', models.PositiveIntegerField()),
                ('monto_propuesta', models.FloatField()),
                ('margen_contribucion', models.FloatField(max_length=3)),
                ('utilidad_esperada', models.FloatField()),
                ('exito', models.FloatField(max_length=4)),
                ('lugar', models.CharField(max_length=25)),
                ('servicios_incluidos', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CBR', 'Coffe Break'), ('ALM', 'Almuerzo'), ('MIP', 'Material impreso'), ('MDG', 'Material digital')], max_length=15, null=True)),
                ('fecha_inicio_estimada', models.CharField(max_length=12)),
                ('observacion', models.CharField(blank=True, max_length=250, null=True)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('nombre', models.CharField(max_length=50)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_juridicas.Juridica')),
                ('reporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reporte_contacto.ReporteContacto')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_juridicas.Sector')),
                ('tipo_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_juridicas.TipoEmpresa')),
            ],
        ),
    ]
