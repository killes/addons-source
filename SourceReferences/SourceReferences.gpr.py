#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2011      Nick Hall
# Copyright (C) 2011      Tim G L Lyons
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id: SourceReferences.gpr.py 2374 2014-05-02 13:29:19Z romjerome $

#------------------------------------------------------------------------
#
# Register Gramplet
#
#------------------------------------------------------------------------
register(GRAMPLET,
         id="Source References",
         name=_("Source References"),
         description = _("Gramplet showing the references for a source"),
         version = '1.0.6',
         gramps_target_version="5.0",
         include_in_listing = False,
         status = UNSTABLE,
         fname="SourceReferences.py",
         height=200,
         gramplet = 'SourceReferences',
         gramplet_title=_("References"),
         navtypes=["Source"],
         )
