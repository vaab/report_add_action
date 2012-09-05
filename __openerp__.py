# -*- coding: utf-8 -*-

{
    "name" : "Easy Report Action",
    "description" : """This module adds a new 'Add' button in the report form view.
When clicked, an action to print this report is added in the sidebar of the targeted
model. You can also remove the action if needed.
""",
    "version" : "%%short-version%%",
    "depends" : ["base"],
    "author" : "Valentin LAB -- Simplee",
    "category": "Reports/Xml",
    "url": "https://github.com/vaab",
    "data": [ "ir_report_add_action_view.xml",
    ],
    "installable" : True,
    "active" : False,
}
