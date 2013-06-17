# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Keyboard shortcuts',
    'version': '1.1',
    'category': 'Tools',
    'description': """
Shortcuts and GUI Improvement.
==============================
    
Shortcuts: 
----------
    * **Ctrl + s** -  For Save Current Object(Require:form in edit mode)
    * **Ctrl + e** -  For Edit Current Object(Require:form in saved mode)
    * **Ctrl + space** -  For Create New Record(Open Form).
    * **Alt** -  In Form View Press Alt key and then press AccessKey Passed from Button.
    * **Ctrl + k** -  Switch to Kanban View.
    * **Ctrl + l** -  Switch to List View.
    * **Ctrl + ;** -  Switch to Form View.
    * **Ctrl + F** -  Focus on Search view(Press This shortcut and start searching).
    * **Ctrl + D** -  Disable search view (Hide search view).
    * **Ctrl + >** -  Display Next Page(In Form View).
    * **Ctrl + <** -  Display Previous Page(In Form View).
    * **Ctrl + Backspace** -  Go in to on stap back if use open page from from view (Example **Sales Orders / SO007 / Invoice** if you press this shortcut then S0007 Display).
    * **Ctrl + esc** -  For Discard Current Change (Effect Like press Discard Link)
    * **Ctrl + ↓** -  Expand lines(Need Group By in Tree View ).
    * **Ctrl + ↑** -  Collapse All lines(Need Group By in Tree View ).
    * **Ctrl + 1 to Ctrl + 9** -  Change Main Manu according to Number Perssed.
    * **For Secondary Menu** -  Press **Ctrl + `** (Key above Tab) and then press ↑ or ↓ for movement and then Press Enter
    * **Ctrl + P** -  Give Screenshots of Tree Or Form Or Graph ( Without Menus ).
    * **Ctrl + F11** -  Enable Full Screen Mode.
    * **Esc** -  Disable Full Screen Mode.
Search Hint: 
------------
After installing Search View supports hints. You can redirect to any menu from search view.

**How to use**
    * Add any tree in to shortcut(with help of star)
    * Now open search view and type first character of name of view. Ex.You added "Sales/Sales/Customers" shortcut then type "C"(case sensitive).this will shows a hint. 
    * Now press right arrow key and then press enter, you will redirect to that view.

You can also custom hints from Menu: **Setting > Technical > User Interface > Search Hint Setup**
    """,
    "author": "OpenERP SA",
    "website": "http://www.openerp.com",
    'depends': ["base","web_shortcuts","web_gui"],
    'init_xml': [],
    'data': [
             "ir_ui_menu_view.xml"
             ],
        'css':[
        'static/src/css/focus_menu.css',
    ],
    "js" : [
        "static/src/js/html2canvas.js",
        "static/src/js/jquery.cookie.js",
        "static/src/js/web_keyboard_shortcuts.js",
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: