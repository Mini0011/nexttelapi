# Generated by Django 4.1 on 2022-09-26 12:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operateur', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=200)),
                ('libelle', models.CharField(max_length=200)),
                ('date_effectue', models.DateTimeField(default=django.utils.timezone.now)),
                ('destinataire', models.IntegerField()),
                ('emetteur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='application.service')),
            ],
            bases=('application.service',),
        ),
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='application.service')),
            ],
            bases=('application.service',),
        ),
        migrations.CreateModel(
            name='tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accesskey', models.CharField(max_length=120, unique=True)),
                ('expirydate', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_token', to='application.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Applications_clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
                ('type_application', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_clientes', to='application.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_credit', models.IntegerField(blank=True, null=True)),
                ('nbre_sms', models.IntegerField(blank=True, null=True)),
                ('application_cliente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='abonnement', to='application.applications_clientes')),
                ('service_id', models.ManyToManyField(related_name='s_abonner', to='application.service')),
            ],
        ),
    ]
