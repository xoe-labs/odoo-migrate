# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

_TEXT_ERRORS = {
    "*": {
        "web_settings_dashboard":
        "[V13] Reference to 'web_settings_dashboard'"
        ". This module has been removed."
    },
    ".py": {
        r".*@api.returns.*\n":
        "[13] Use of deprecated decorator '@api.returns'",
        r".*@api.cr.*\n":
        "[13] Use of deprecated decorator '@api.cr'",
        r".*@api.model_cr.*\n":
        "[13] Use of deprecated decorator '@api.model_cr'",
        r".sudo\(":
        "[13] Use of deprated function sudo(). Use with_user instead."
    },
}

_TEXT_REPLACES = {
    ".py": {
        r".*@api.multi.*\n": "",
        r".*@api.one.*\n": "",
    },
}
