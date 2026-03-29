# Generated migration file

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('problem_statement', models.TextField(blank=True)),
                ('dataset_used', models.TextField(blank=True)),
                ('tools', models.TextField(help_text='Tools separated by commas. E.g., Python, Excel, Power BI')),
                ('key_insights', models.TextField(blank=True)),
                ('business_result', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='projects/')),
                ('link', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
