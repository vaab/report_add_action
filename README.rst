==================
Easy Report Action
==================

Provides a simple button at the bottom of the form view of report objects which
adds or remove the report launching action on the object targeted by the report.

This module is really small and can be used as a good way to learn OpenERP
module creation.

Besides, adding the action manually can be tedious, so this could be of some
value for some of you out there.


Requirements
------------

Was tested successfully with:

 - OpenERP 6.0.3
 - OpenERP 6.1
 - OpenERP 7.0

No other needs.


Installation
------------

Please make sure to launch:

  ./autogen.sh

prior to installing this module to generate the version and the changelog.

Then you can install it as any other OpenERP module.


Usage
-----

1. Ensure that you are are an OpenERP administrator with Extended Interface.
2. Then go to the "Settings" Tab,
3. And in the left menu, follow Customization / Low Level Objects / Actions / Reports
4. On any reports (previously created or newly created) you'll find at the
   bottom a Convenient "Add Report" button with a "+" symbol or a "Remove
   Report" button with a "-" symbol.  Upon click, an action will be added in
   the view of the model targeted by the report.  This action will be located
   in the sidebar of the view in the "Reports" section.
