# Generated by Django 2.2.5 on 2019-09-07 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('canal_de_contacto', models.CharField(max_length=100)),
                ('motivo_de_contacto', models.CharField(max_length=500)),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('cargo', models.CharField(max_length=100)),
                ('correo_electronico', models.CharField(max_length=100)),
                ('asistentes', models.CharField(max_length=100)),
                ('situacion_actual', models.CharField(max_length=500)),
                ('situacion_deseada', models.CharField(max_length=500)),
                ('servicios_requeridos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=25)),
                ('tipo', models.CharField(choices=[('CR', 'Curso'), ('CNF', 'Conferencia'), ('WB', 'Webinario'), ('TLL', 'Taller'), ('MOD', 'Módulo'), ('PRG', 'Programa'), ('DPL', 'Diplomado')], default='CR', max_length=25)),
                ('modalidad', models.CharField(choices=[('PRS', 'Presencial'), ('SPRS', 'Semi-presencial'), ('VRT', 'Virtual')], default='PRS', max_length=25)),
                ('area', models.CharField(choices=[('A', 'ADMINISTRACIÓN Y LEGISLACIÓN'), ('B', 'AGRONOMÍA'), ('C', 'ZOOTECNIA'), ('D', 'ALIMENTACIÓN, GASTRONOMÍA Y TURISMO'), ('E', 'TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIÓN'), ('F', 'FINANZAS, COMERCIO Y VENTAS'), ('H', 'CONSTRUCCIÓN E INFRAESTRUCTURA'), ('I', 'FORESTAL, ECOLOGÍA Y AMBIENTE'), ('J', 'EDUCACIÓN Y CAPACITACIÓN'), ('K', 'ELECTRICIDAD Y ELECTRÓNICA'), ('L', 'ESPECIES ACUÁTICAS Y PESCA'), ('M', 'COMUNICACIÓN Y ARTES GRÁFICAS'), ('N', 'MECÁNICA AUTOMOTRIZ'), ('O', 'MECÁNICA INDUSTRIAL Y MINERÍA'), ('P', 'PROCESOS INDUSTRIALES'), ('Q', 'TRANSPORTE Y LOGÍSTICA'), ('R', 'ARTES Y ARTESANÍA'), ('S', 'SERVICIOS SOCIOCULTURALES Y A LA COMUNIDAD'), ('T', 'INDUSTRIA AGROPECUARIA ')], max_length=100)),
                ('nivel_organizacion', models.CharField(choices=[('OP', 'Operativos'), ('MM', 'Mandos medios'), ('D/G', 'Directivos/Gerentes')], default='OP', max_length=25)),
                ('numero_participantes', models.PositiveIntegerField()),
                ('horario_trabajo', models.CharField(max_length=50)),
                ('nivel_educacion', models.CharField(choices=[('SE', 'Sin escolaridad'), ('PRI', 'Primaria'), ('BCH', 'Bachillerato'), ('TN', 'Tercer Nivel'), ('CN', 'Cuarto Nivel'), ('NEMV', 'Nivel de educación muy variado')], default='BCH', max_length=25)),
                ('edad_promedio', models.CharField(choices=[('18_25', 'Entre 18 a 25 años'), ('26_35', 'Entre 26 a 35 años'), ('36_55', 'Entre 36 a 55 años'), ('56_65', 'Entre 56 a 65 años'), ('+65', 'Más de 65 años')], max_length=25)),
                ('lugar', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=25)),
                ('fecha_evento', models.DateField()),
                ('horario_evento_inicio', models.TimeField()),
                ('horario_evento_fin', models.TimeField()),
                ('observaciones', models.CharField(max_length=500)),
                ('acuerdos', models.CharField(max_length=500)),
                ('exclusivo_acad', models.CharField(blank=True, max_length=500, null=True)),
                ('reporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporte_contacto.ReporteContacto')),
            ],
        ),
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=500)),
                ('alcance', models.CharField(max_length=250)),
                ('con_sin_imple', models.CharField(max_length=25)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('proveedor', models.CharField(max_length=25)),
                ('entregables', models.CharField(max_length=500)),
                ('observaciones', models.CharField(max_length=500)),
                ('acuerdos', models.CharField(max_length=500)),
                ('exclusivo_acad', models.CharField(blank=True, max_length=500, null=True)),
                ('reporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporte_contacto.ReporteContacto')),
            ],
        ),
    ]