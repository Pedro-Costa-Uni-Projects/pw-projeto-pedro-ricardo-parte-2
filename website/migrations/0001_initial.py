# Generated by Django 3.2.3 on 2021-05-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clareza', models.CharField(default=3, max_length=10)),
                ('rigor', models.CharField(default=3, max_length=10)),
                ('precisao', models.CharField(default=3, max_length=10)),
                ('optimizacao', models.BooleanField(default=False, verbose_name='Boa optimização para telemóvel')),
                ('tempoResposta', models.BooleanField(default=False, verbose_name='Tempo de resposta do Website')),
                ('facilUsar', models.BooleanField(default=False, verbose_name='Fácil de Usar')),
                ('facilLer', models.BooleanField(default=False, verbose_name='Fácil de Ler')),
                ('feedBack', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('apelido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('pais', models.CharField(choices=[('pt', 'Portugal'), ('br', 'Brasil'), ('esp', 'Espanha'), ('uk', 'Reino Unido'), ('ale', 'Alemanha'), ('bel', 'Bélgica'), ('eua', 'Estados Unidos')], default='', max_length=20)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pontos', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=40)),
                ('apelido', models.CharField(max_length=40)),
                ('p1', models.IntegerField(default=0)),
                ('p2', models.CharField(default='', max_length=40)),
                ('p3', models.CharField(default='', max_length=40)),
                ('p4', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('p5', models.CharField(choices=[('Braços', 'Braços'), ('Bruços', 'Bruços'), ('Pernas', 'Pernas')], default='', max_length=40)),
                ('p6', models.CharField(default='', max_length=40)),
                ('p7', models.CharField(default='', max_length=40)),
                ('p8', models.IntegerField(default=0)),
                ('p9', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('p10', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
            ],
        ),
    ]
