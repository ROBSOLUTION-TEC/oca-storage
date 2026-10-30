# Copyright 2023 ACSONE SA/NV (https://www.acsone.eu).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from __future__ import annotations

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class FSStorage(models.Model):
    _inherit = "fs.storage"

    @property
    def _server_env_fields(self):
        env_fields = super()._server_env_fields
        env_fields.update(
            {
                "optimizes_directory_path": {},
                "autovacuum_gc": {},
                "base_url": {},
                "is_directory_path_in_url": {},
                "use_x_sendfile_to_serve_internal_url": {},
                "use_as_default_for_attachments": {},
                "force_db_for_default_attachment_rules": {},
                "use_filename_obfuscation": {},
            }
        )
        return env_fields

    # base_url and the directory are read from the environment (or from the
    # defaults stored in server_env_defaults): recompute when a default changes
    @api.depends(
        "base_url", "is_directory_path_in_url", "directory_path", "server_env_defaults"
    )
    def _compute_base_url_for_files(self):
        return super()._compute_base_url_for_files()
