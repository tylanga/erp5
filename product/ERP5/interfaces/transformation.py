# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 Nexedi SA and Contributors. All Rights Reserved.
#                    Jean-Paul Smets-Solanes <jp@nexedi.com>
#                    Łukasz Nowak <luke@nexedi.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from zope.interface import Interface

class ITransformation(Interface):
  """
    Common Interface to implementing querying of Indirect Amount
    Models (TaxModelLine, InvoiceModelLine, etc) shall be based on this
    interface
  """

  def getAggregatedAmountList(context, movement_list=None, rounding=False):
    """Returns list of amounts generated by set of models

    context - represents object on which calculation shall happen

    movement_list - optional argument, movement list to apply on, if not passed
      it will be generated from passed context

    rounding - boolean argument, which controls if rounding shall be applied on
      generated movements or not

    Returns list of instance of AggregatedAmountList class

    Note: This method shall be linear in case if context is order, line,
    applied rule or movement. In case of built delivery this method shall
    be wise enough to CORRECTLY un-linearise calculation, eg. tax is
    time dependent, paysheet build from invoices.
    """
    pass

  def updateAggregatedAmountList(context, movement_list=None, rounding=False):
    """Updates existing movement and returns new or deleted if any according to model

    context - represents object on which update shall happen

    movement_list - optional argument, movement list to apply on, if not passed
      it will be generated from passed context

    rounding - boolean argument, which controls if rounding shall be applied on
      generated movements or not

    Returns a dictionary of list of instances of AggregatedAmountList class.
    Dictionary contain lists described by keys:
      * movement_to_add_list - list for movements which shall be added
      * movement_to_delete_list - list of movements which shall be deleted
    """
    pass
