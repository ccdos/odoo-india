# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

import time
from datetime import datetime
import math
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _
from openerp import tools

class indent_indent(osv.Model):
    _inherit = 'indent.indent'
    _columns = {
        'contract': fields.boolean('Contract', help="Check box True means the contract otherwise it is indent", readonly=True)
        }
    
    _defaults = {
        'contract': False
        }
    
indent_indent()

class purchase_order(osv.Model):
    _inherit = 'purchase.order'

    def _get_number_of_days(self, date_from, date_to):
        """Returns a float equals to the timedelta between two dates given as string."""

        DATETIME_FORMAT = "%Y-%m-%d"
        from_dt = datetime.strptime(date_from, DATETIME_FORMAT)
        to_dt = datetime.strptime(date_to, DATETIME_FORMAT)
        timedelta = to_dt - from_dt
        diff_day = timedelta.days + float(timedelta.seconds) / 86400
        return diff_day

    def onchange_compute_days1(self, cr, uid, ids, date_from, date_to,d1=0,d2=0):
        """
        If there are no date set for date_to, automatically set one 8 hours later than
        the date_from.
        Also update the number_of_days.
        """
        # date_to has to be greater than date_from
        if (date_from and date_to) and (date_from > date_to):
            raise osv.except_osv(_('Warning!'),_('The start date must be anterior to the end date.'))

        result = {'value': {}}

        # No date_to set so far: automatically compute one 8 hours later
        if date_from and not date_to:
            result['value']['no_of_days1'] = 0
            result['value']['total_days'] = d1+d2

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            diff_day = self._get_number_of_days(date_from, date_to)
            result['value']['no_of_days1'] = round(math.floor(diff_day))+1
            result['value']['total_days'] = d1+d2+round(math.floor(diff_day))+1
        else:
            result['value']['no_of_days1'] = 0

        return result
    
    def onchange_compute_days2(self, cr, uid, ids, date_from, date_to,d1=0,d2=0):
        """
        If there are no date set for date_to, automatically set one 8 hours later than
        the date_from.
        Also update the number_of_days.
        """
        # date_to has to be greater than date_from
        if (date_from and date_to) and (date_from > date_to):
            raise osv.except_osv(_('Warning!'),_('The start date must be anterior to the end date.'))

        result = {'value': {}}

        # No date_to set so far: automatically compute one 8 hours later
        if date_from and not date_to:
            result['value']['no_of_days2'] = 0
            result['value']['total_days'] = d1+d2

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            diff_day = self._get_number_of_days(date_from, date_to)
            result['value']['no_of_days2'] = round(math.floor(diff_day))+1
            result['value']['total_days'] = round(math.floor(diff_day))+1+d1+d2
        else:
            result['value']['no_of_days2'] = 0

        return result
    def onchange_compute_days3(self, cr, uid, ids, date_from, date_to,d1=0,d2=0):
        """
        If there are no date set for date_to, automatically set one 8 hours later than
        the date_from.
        Also update the number_of_days.
        """
        # date_to has to be greater than date_from
        if (date_from and date_to) and (date_from > date_to):
            raise osv.except_osv(_('Warning!'),_('The start date must be anterior to the end date.'))

        result = {'value': {}}

        # No date_to set so far: automatically compute one 8 hours later
        if date_from and not date_to:
            result['value']['no_of_days3'] = 0
            result['value']['total_days'] = d1+d2

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            diff_day = self._get_number_of_days(date_from, date_to)
            result['value']['no_of_days3'] = round(math.floor(diff_day))+1
            result['value']['total_days'] = round(math.floor(diff_day))+1+d1+d2
        else:
            result['value']['no_of_days3'] = 0

        return result       
    
    _columns = {
        'contract': fields.related('indent_id', 'contract', type='boolean', relation='indent.indent', string='Contract', store=True, readonly=True),
        'no_of_days1': fields.integer("No of Days1", help="Calculate number of days for contracts"),
        'no_of_days2': fields.integer("No of Days2", help="Calculate number of days for contracts"),
        'no_of_days3': fields.integer("No of Days3", help="Calculate number of days for contracts"),
        'total_days': fields.integer("Total Days", help="Calculate number of days for contracts"),
        'date_from': fields.date('From Date', required=True),
        'date_to': fields.date('To Date'),
        'extended_date_from1': fields.date('Extended From'),
        'extended_date_from2': fields.date('Extended From'),
        'extended_date_to1': fields.date('Extended Upto'),
        'extended_date_to2': fields.date('Extended Upto'),
        'retention': fields.selection([('leived', 'CONTRACTOR\'S RETENTION TO BE LEIVED'),('not_leived', 'CONTRACTOR\'S RETENTION NOT TO BE LEIVED')], "Retenstion Type"),
        }
    
    _defaults = {
        'date_from': lambda *a: datetime.now().strftime('%Y-%m-%d'),
        'date_to': lambda *a: datetime.now().strftime('%Y-%m-%d'), 
        }