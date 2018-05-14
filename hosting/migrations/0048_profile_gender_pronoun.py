# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import hosting.fields


def populate_genders(app_registry, schema_editor):
    Gender = app_registry.get_model('hosting', 'Gender')
    Gender.objects.bulk_create([
        Gender(id=1,  name_en='Akava\'ine',                 name='Akava\'ine'),
        Gender(id=2,  name_en='bigender',                   name='ambaŭgenra'),
        Gender(id=3,  name_en='androgynous',                name='androgena'),
        Gender(id=4,  name_en='Baklâ',                      name='Baklâ'),
        Gender(id=5,  name_en='Bissu',                      name='Bissu'),
        Gender(id=6,  name_en='Calabai',                    name='Calabai'),
        Gender(id=7,  name_en='Calalai',                    name='Calalai'),
        Gender(id=8,  name_en='cisgender woman',            name='cisgenra virino'),
        Gender(id=9,  name_en='cisgender man',              name='cisgenra viro'),
        Gender(id=10, name_en='cis woman',                  name='cis-ino'),
        Gender(id=11, name_en='cis man',                    name='cis-viro'),
        Gender(id=12, name_en='pangender',                  name='ĉiugenra'),
        Gender(id=13, name_en='bi-gender',                  name='dugenra'),
        Gender(id=14, name_en='two-spirit',                 name='du-spirita'),
        Gender(id=15, name_en='genderfluid',                name='fluidgenra'),
        Gender(id=16, name_en='genderqueer',                name='genrokvira'),
        Gender(id=17, name_en='gender nonconforming',       name='genro-nekonforma'),
        Gender(id=18, name_en='gender neutral',             name='genro-neŭtra'),
        Gender(id=19, name_en='gender questioning',         name='genro-priduba'),
        Gender(id=20, name_en='gender variant',             name='genro-varia'),
        Gender(id=21, name_en='intersex',                   name='interseksa'),
        Gender(id=22, name_en='other gender',               name='ne-difinanta genron'),
        Gender(id=23, name_en='non-binary gender',          name='neduumgenra'),
        Gender(id=24, name_en='gender non-conforming',      name='ne-laŭanta genron'),
        Gender(id=25, name_en='Neutrois',                   name='Neutrois'),
        Gender(id=26, name_en='demiwoman',                  name='partgenre ina'),
        Gender(id=27, name_en='demiman',                    name='partgenre vira'),
        Gender(id=28, name_en='agender',                    name='sengenra'),
        Gender(id=29, name_en='trans*',                     name='trans*'),
        Gender(id=30, name_en='trans*person',               name='trans*persono'),
        Gender(id=31, name_en='trans female',               name='transfemala'),
        Gender(id=32, name_en='transgender',                name='transgenra'),
        Gender(id=33, name_en='transgender woman',          name='transgenra virino'),
        Gender(id=34, name_en='transgender man',            name='transgenra viro'),
        Gender(id=35, name_en='trans feminine',             name='trans-ineca'),
        Gender(id=36, name_en='trans woman',                name='trans-ino'),
        Gender(id=37, name_en='trans male',                 name='transmaskla'),
        Gender(id=38, name_en='transsexual',                name='transseksa'),
        Gender(id=39, name_en='trans masculine',            name='trans-vireca'),
        Gender(id=40, name_en='trans man',                  name='trans-viro'),
        Gender(id=41, name_en='Travesti',                   name='Travesti'),
        Gender(id=42, name_en='third gender',               name='tria-genra'),
        Gender(id=43, name_en='third gender (Chhakka)',     name='tria-genra (Chhakka)'),
        Gender(id=44, name_en='third gender (Fa\'afafine)', name='tria-genra (Fa\'afafine)'),
        Gender(id=45, name_en='third gender (Hijra)',       name='tria-genra (Hijra)'),
        Gender(id=46, name_en='third gender (Kathoey)',     name='tria-genra (Kathoey)'),
        Gender(id=47, name_en='third gender (Khanīth)',     name='tria-genra (Khanīth)'),
        Gender(id=48, name_en='third gender (Māhū)',        name='tria-genra (Māhū)'),
        Gender(id=49, name_en='third gender (Muxhe)',       name='tria-genra (Muxhe)'),
        Gender(id=50, name_en='trigender',                  name='trigenra'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0047_preferences_public_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255, unique=True, verbose_name='name (in English)')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'genders',
                'verbose_name': 'gender',
            },
        ),
        migrations.RunPython(
            populate_genders, reverse_code=migrations.RunPython.noop
        ),
        migrations.AddField(
            model_name='profile',
            name='pronoun',
            field=models.CharField(blank=True, choices=[(None, ''), ('She', 'she'), ('He', 'he'), ('They', 'they')], max_length=5, verbose_name='personal pronoun'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=hosting.fields.ForeigKeyWithSuggestions(blank=True, choices='hosting.Gender', to_field='name', verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, help_text='Short biography. \nProvide here further details about yourself. If you indicated that your gender is non-binary, it will be helpful if you explain more.', verbose_name='description'),
        ),
    ]
