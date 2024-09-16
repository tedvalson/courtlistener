# Generated by Django 5.0.7 on 2024-08-05 20:19

import pgtrigger.compiler
import pgtrigger.migrations
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "people_db",
            "0016_remove_abarating_update_or_delete_snapshot_update_and_more",
        ),
        ("search", "0032_update_docket_numbering_fields"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="opinion",
            name="update_or_delete_snapshot_delete",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="opinion",
            name="update_or_delete_snapshot_update",
        ),
        migrations.AddField(
            model_name="opinion",
            name="ordering_key",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="opinionevent",
            name="ordering_key",
            field=models.IntegerField(blank=True, null=True),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="opinion",
            trigger=pgtrigger.compiler.Trigger(
                name="update_or_delete_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM (NEW."id") OR OLD."date_created" IS DISTINCT FROM (NEW."date_created") OR OLD."cluster_id" IS DISTINCT FROM (NEW."cluster_id") OR OLD."author_id" IS DISTINCT FROM (NEW."author_id") OR OLD."author_str" IS DISTINCT FROM (NEW."author_str") OR OLD."per_curiam" IS DISTINCT FROM (NEW."per_curiam") OR OLD."joined_by_str" IS DISTINCT FROM (NEW."joined_by_str") OR OLD."type" IS DISTINCT FROM (NEW."type") OR OLD."sha1" IS DISTINCT FROM (NEW."sha1") OR OLD."page_count" IS DISTINCT FROM (NEW."page_count") OR OLD."download_url" IS DISTINCT FROM (NEW."download_url") OR OLD."local_path" IS DISTINCT FROM (NEW."local_path") OR OLD."plain_text" IS DISTINCT FROM (NEW."plain_text") OR OLD."html" IS DISTINCT FROM (NEW."html") OR OLD."html_lawbox" IS DISTINCT FROM (NEW."html_lawbox") OR OLD."html_columbia" IS DISTINCT FROM (NEW."html_columbia") OR OLD."html_anon_2020" IS DISTINCT FROM (NEW."html_anon_2020") OR OLD."xml_harvard" IS DISTINCT FROM (NEW."xml_harvard") OR OLD."html_with_citations" IS DISTINCT FROM (NEW."html_with_citations") OR OLD."extracted_by_ocr" IS DISTINCT FROM (NEW."extracted_by_ocr") OR OLD."ordering_key" IS DISTINCT FROM (NEW."ordering_key"))',
                    func='INSERT INTO "search_opinionevent" ("author_id", "author_str", "cluster_id", "date_created", "date_modified", "download_url", "extracted_by_ocr", "html", "html_anon_2020", "html_columbia", "html_lawbox", "html_with_citations", "id", "joined_by_str", "local_path", "ordering_key", "page_count", "per_curiam", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "plain_text", "sha1", "type", "xml_harvard") VALUES (OLD."author_id", OLD."author_str", OLD."cluster_id", OLD."date_created", OLD."date_modified", OLD."download_url", OLD."extracted_by_ocr", OLD."html", OLD."html_anon_2020", OLD."html_columbia", OLD."html_lawbox", OLD."html_with_citations", OLD."id", OLD."joined_by_str", OLD."local_path", OLD."ordering_key", OLD."page_count", OLD."per_curiam", _pgh_attach_context(), NOW(), \'update_or_delete_snapshot\', OLD."id", OLD."plain_text", OLD."sha1", OLD."type", OLD."xml_harvard"); RETURN NULL;',
                    hash="7137855274503cc2c50a17729f82e150d2b7d872",
                    operation="UPDATE",
                    pgid="pgtrigger_update_or_delete_snapshot_update_67ecd",
                    table="search_opinion",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="opinion",
            trigger=pgtrigger.compiler.Trigger(
                name="update_or_delete_snapshot_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "search_opinionevent" ("author_id", "author_str", "cluster_id", "date_created", "date_modified", "download_url", "extracted_by_ocr", "html", "html_anon_2020", "html_columbia", "html_lawbox", "html_with_citations", "id", "joined_by_str", "local_path", "ordering_key", "page_count", "per_curiam", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "plain_text", "sha1", "type", "xml_harvard") VALUES (OLD."author_id", OLD."author_str", OLD."cluster_id", OLD."date_created", OLD."date_modified", OLD."download_url", OLD."extracted_by_ocr", OLD."html", OLD."html_anon_2020", OLD."html_columbia", OLD."html_lawbox", OLD."html_with_citations", OLD."id", OLD."joined_by_str", OLD."local_path", OLD."ordering_key", OLD."page_count", OLD."per_curiam", _pgh_attach_context(), NOW(), \'update_or_delete_snapshot\', OLD."id", OLD."plain_text", OLD."sha1", OLD."type", OLD."xml_harvard"); RETURN NULL;',
                    hash="98fb52aa60fd8e89a83f8f7ac77ba5892739fb37",
                    operation="DELETE",
                    pgid="pgtrigger_update_or_delete_snapshot_delete_1f4fd",
                    table="search_opinion",
                    when="AFTER",
                ),
            ),
        ),
        migrations.AddConstraint(
            model_name="opinion",
            constraint=models.UniqueConstraint(
                fields=("cluster_id", "ordering_key"),
                name="unique_opinion_ordering_key",
            ),
        ),
    ]
