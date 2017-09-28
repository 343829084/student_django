# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begindate', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('enddate', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('term', models.CharField(unique=True, max_length=16, verbose_name='\u5b66\u671f')),
                ('excellent', models.IntegerField(verbose_name='\u4f18')),
                ('good', models.IntegerField(verbose_name='\u826f')),
                ('ordinary', models.IntegerField(verbose_name='\u4e2d')),
            ],
            options={
                'db_table': 'assessment',
                'verbose_name_plural': '\u4e92\u8bc4\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='AssessmentRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=1, verbose_name='\u8bc4\u4ef7\u7ed3\u679c', choices=[(b'0', b'\xe4\xbc\x98'), (b'1', b'\xe8\x89\xaf'), (b'2', b'\xe4\xb8\xad'), (b'3', b'\xe6\x97\xa0')])),
                ('assessment', models.ForeignKey(verbose_name=b'\xe4\xba\x92\xe8\xaf\x84', to='webadmin.Assessment')),
            ],
            options={
                'db_table': 'assessmentrecord',
                'verbose_name_plural': '\u4e92\u8bc4\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='AssessmentRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excellent', models.IntegerField(verbose_name='\u4f18')),
                ('good', models.IntegerField(verbose_name='\u826f')),
                ('ordinary', models.IntegerField(verbose_name='\u4e2d')),
                ('assessment', models.ForeignKey(verbose_name=b'\xe4\xba\x92\xe8\xaf\x84', to='webadmin.Assessment')),
            ],
            options={
                'db_table': 'assessmentrow',
                'verbose_name_plural': '\u6bcf\u4eba\u4e92\u8bc4\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actlevel', models.CharField(max_length=1, verbose_name='\u7ea7\u522b', choices=[(b'0', b'\xe5\xad\xa6\xe6\xa0\xa1'), (b'1', b'\xe5\xad\xa6\xe9\x99\xa2')])),
                ('name', models.CharField(max_length=16, verbose_name='\u540d\u79f0')),
            ],
            options={
                'db_table': 'behavior',
                'verbose_name_plural': '\u65e5\u5e38\u884c\u4e3a\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classid', models.CharField(unique=True, max_length=10, verbose_name='\u73ed\u53f7')),
                ('classname', models.CharField(max_length=20, verbose_name='\u73ed\u7ea7\u540d\u79f0')),
            ],
            options={
                'db_table': 'class',
                'verbose_name_plural': '\u73ed\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Comperformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excellent', models.FloatField(verbose_name='\u4f18\u5206\u6570')),
                ('good', models.FloatField(verbose_name='\u826f\u5206\u6570')),
                ('ordinary', models.FloatField(verbose_name='\u4e2d\u5206\u6570')),
                ('physical', models.FloatField(verbose_name='\u4f53\u80fd\u5206\u6570')),
                ('behavior', models.FloatField(verbose_name='\u65e5\u5e38\u884c\u4e3a\u5206\u57fa\u7840\u5206')),
                ('development', models.FloatField(verbose_name='\u5355\u9879\u6700\u9ad8\u5206')),
                ('moral', models.FloatField(verbose_name='\u4e92\u8bc4\u6700\u9ad8\u5206')),
                ('behaviorup', models.FloatField(verbose_name='\u65e5\u5e38\u884c\u4e3a\u5206\u6700\u9ad8')),
                ('term', models.CharField(unique=True, max_length=16, verbose_name='\u5b66\u671f')),
            ],
            options={
                'db_table': 'comperformance',
                'verbose_name_plural': '\u7efc\u5408\u6d4b\u8bc4\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='ComperformanceBehaviorScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True, verbose_name='\u5206\u6570', blank=True)),
                ('behavior', models.ForeignKey(verbose_name=b'\xe6\x97\xa5\xe5\xb8\xb8\xe8\xa1\x8c\xe4\xb8\xba', to='webadmin.Behavior')),
                ('comperformance', models.ForeignKey(verbose_name=b'\xe7\xbb\xbc\xe5\x90\x88\xe6\x88\x90\xe7\xbb\xa9\xe7\xae\xa1\xe7\x90\x86', to='webadmin.Comperformance')),
            ],
            options={
                'db_table': 'comperformancebehaviorscore',
                'verbose_name_plural': '\u65e5\u5e38\u6d3b\u52a8\u52a0\u5206',
            },
        ),
        migrations.CreateModel(
            name='ComperformanceDevelopmentScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True, verbose_name='\u5206\u6570', blank=True)),
                ('comperformance', models.ForeignKey(verbose_name=b'\xe7\xbb\xbc\xe5\x90\x88\xe6\x88\x90\xe7\xbb\xa9\xe7\xae\xa1\xe7\x90\x86', to='webadmin.Comperformance')),
            ],
            options={
                'db_table': 'comperformancedevelopmentscore',
                'verbose_name_plural': '\u4e2a\u6027\u53d1\u5c55\u52a0\u5206',
            },
        ),
        migrations.CreateModel(
            name='ComperformancePhysicalScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True, verbose_name='\u5206\u6570', blank=True)),
                ('comperformance', models.ForeignKey(verbose_name=b'\xe7\xbb\xbc\xe5\x90\x88\xe6\x88\x90\xe7\xbb\xa9\xe7\xae\xa1\xe7\x90\x86', to='webadmin.Comperformance')),
            ],
            options={
                'db_table': 'comperformancephysicalscore',
                'verbose_name_plural': '\u4f53\u80fd\u52a0\u5206',
            },
        ),
        migrations.CreateModel(
            name='ComperformanceScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True, verbose_name='\u7efc\u5408\u6210\u7ee9\u5206\u6570', blank=True)),
                ('assessmentscore', models.FloatField(null=True, verbose_name='\u4e92\u8bc4\u5206\u6570', blank=True)),
                ('comperformance', models.ForeignKey(verbose_name=b'\xe7\xbb\xbc\xe5\x90\x88\xe6\x88\x90\xe7\xbb\xa9\xe7\xae\xa1\xe7\x90\x86', to='webadmin.Comperformance')),
            ],
            options={
                'db_table': 'comperformancescore',
                'verbose_name_plural': '\u7efc\u5408\u6d4b\u8bc4\u5206\u6570',
            },
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent', models.CharField(blank=True, max_length=1, null=True, verbose_name='\u4e2a\u6027\u53d1\u5c55\u5927\u7c7b', choices=[(b'0', b'\xe7\xbb\x84\xe7\xbb\x87\xe7\xae\xa1\xe7\x90\x86'), (b'1', b'\xe5\x88\x9b\xe6\x96\xb0'), (b'2', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('name', models.CharField(max_length=11, verbose_name='\u4e2a\u6027\u53d1\u5c55\u540d\u79f0')),
            ],
            options={
                'db_table': 'development',
                'verbose_name_plural': '\u4e2a\u6027\u53d1\u5c55\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.CharField(max_length=16, verbose_name='\u5b66\u671f')),
                ('score', models.FloatField(verbose_name='\u5206\u6570')),
            ],
            options={
                'db_table': 'grade',
                'verbose_name_plural': '\u6210\u7ee9',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=16, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(max_length=1, verbose_name='\u6027\u522b', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
                ('theclass', models.ForeignKey(verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7', to='webadmin.Class')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student',
                'verbose_name_plural': '\u5b66\u751f',
            },
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='comperformancescore',
            name='student',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='comperformancephysicalscore',
            name='student',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='comperformancedevelopmentscore',
            name='development',
            field=models.ForeignKey(verbose_name=b'\xe4\xb8\xaa\xe6\x80\xa7\xe5\x8f\x91\xe5\xb1\x95', to='webadmin.Development'),
        ),
        migrations.AddField(
            model_name='comperformancedevelopmentscore',
            name='student',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='comperformancebehaviorscore',
            name='student',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='assessmentrow',
            name='student',
            field=models.ForeignKey(verbose_name=b'\xe8\xa2\xab\xe8\xaf\x84\xe4\xbb\xb7\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='assessmentrecord',
            name='dstudent',
            field=models.ForeignKey(related_name='dstuent', verbose_name=b'\xe8\xa2\xab\xe8\xaf\x84\xe4\xbb\xb7\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
        migrations.AddField(
            model_name='assessmentrecord',
            name='ostudent',
            field=models.ForeignKey(related_name='ostuent', verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe5\x90\x8c\xe5\xad\xa6', to='webadmin.Student'),
        ),
    ]
