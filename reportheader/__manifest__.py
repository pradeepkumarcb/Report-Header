# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017 GSIT IT Solutions Pvt Ltd
#    (http://www.globalsourcesinfotech.com)
#    info@GSIT.com
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
    'name': 'Letter Header',
    'version' : '1.0',
    'depends': ['base','report'],
    'author': 'GSIT',
    'category': 'Hidden/Dependency',
    'description': """
Installer for knowledge-based Hidden.
=====================================

Makes the Knowledge Application Configuration available from where you can install
document and Wiki based Hidden.
    """,
    'website': 'www.globalsourcesinfotech.com',
    'data': [
        'views/company_view.xml',
        'views/report_header.xml',
#         'views/report_invoice.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
