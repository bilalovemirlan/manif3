# Generated by Django 4.0.6 on 2022-07-07 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('fio', models.CharField(max_length=64, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('phone1', models.CharField(blank=True, max_length=20)),
                ('monthly_salary', models.IntegerField(default=0, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=64)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Working_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=10)),
                ('kol_vo', models.IntegerField()),
                ('marriage_workers', models.IntegerField()),
                ('defective_machines', models.IntegerField()),
                ('Say_marriage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SalaryTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('working_days', models.IntegerField(max_length=31, null=True)),
                ('fact_work_days', models.IntegerField(max_length=31, null=True)),
                ('oklad_social_fund', models.IntegerField(max_length=256, null=True)),
                ('firm_social_fund', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('oklad_nachislen', models.IntegerField(max_length=256, null=True)),
                ('fio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacture.employee')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salary_total_occupation', to='manufacture.occupation')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employer_ocupation', to='manufacture.occupation'),
        ),
        migrations.CreateModel(
            name='CalculationPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacture.employee')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='manufacture.occupation')),
            ],
        ),
        migrations.CreateModel(
            name='CalculationEVA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacture.employee')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='manufacture.occupation', verbose_name='Απασχόληση')),
            ],
        ),
    ]