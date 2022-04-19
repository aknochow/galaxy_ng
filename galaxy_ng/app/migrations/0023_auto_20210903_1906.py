# Generated by Django 3.2.6 on 2021-09-03 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0020_update_push_repo_perms'),
        ('galaxy', '0022_enforce_retain_repo_versions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='containersynctask',
            name='repository',
        ),
        migrations.RemoveField(
            model_name='containersynctask',
            name='task',
        ),
        migrations.AlterField(
            model_name='containerregistryrepos',
            name='repository_remote',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='registry', serialize=False, to='container.containerremote'),
        ),
        migrations.DeleteModel(
            name='CollectionSyncTask',
        ),
        migrations.DeleteModel(
            name='ContainerSyncTask',
        ),
    ]