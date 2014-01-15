# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-Today Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Opportunity to RFQ",
    "version" : "1.0",
    "author" : "OpenERP SA",
    "website" : "http://www.openerp.com",
    'sequence': 120,
    "category": "Purchase Management",
    'summary' : 'Create Request for Quotation from Opportunity',
    "description":
"""
Opportunity To Request for Quotation
============================================================
Create Request for Quotation from Opportunity.

Module will add button on Opportunity form to create Purchase Quotation directly from Opportunity.

""",    
    "depends" : ['crm', 'purchase', 'l10n_in_base'],
    "init_xml" : [],
    "update_xml" : [
        "wizard/create_rfq_wizard.xml",
        "purchase_crm_view.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: