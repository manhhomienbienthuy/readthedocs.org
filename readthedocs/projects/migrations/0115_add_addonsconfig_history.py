# Generated by Django 4.2.10 on 2024-02-19 15:21

import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.before_deploy

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0114_set_timestamp_fields_as_no_null"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalAddonsConfig",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "extra_history_user_id",
                    models.IntegerField(
                        blank=True, db_index=True, null=True, verbose_name="ID"
                    ),
                ),
                (
                    "extra_history_user_username",
                    models.CharField(
                        db_index=True,
                        max_length=150,
                        null=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "extra_history_ip",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="IP address"
                    ),
                ),
                (
                    "extra_history_browser",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Browser user-agent",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=True,
                        help_text="Enable/Disable all the addons on this project",
                    ),
                ),
                ("analytics_enabled", models.BooleanField(default=False)),
                ("doc_diff_enabled", models.BooleanField(default=True)),
                ("doc_diff_show_additions", models.BooleanField(default=True)),
                ("doc_diff_show_deletions", models.BooleanField(default=True)),
                (
                    "doc_diff_root_selector",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("external_version_warning_enabled", models.BooleanField(default=True)),
                ("ethicalads_enabled", models.BooleanField(default=True)),
                ("flyout_enabled", models.BooleanField(default=True)),
                ("hotkeys_enabled", models.BooleanField(default=True)),
                ("search_enabled", models.BooleanField(default=True)),
                (
                    "search_default_filter",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "stable_latest_version_warning_enabled",
                    models.BooleanField(default=True),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="projects.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical addons config",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]