__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from orderedmodeladmin import OrderedModelAdmin

class LicenseAdmin(OrderedModelAdmin):
    prepopulated_fields = {"slug": ("type",)}
    list_display = ('type', 'url', 'jurisdiction', 'hidden', 'move_up_down_links')
