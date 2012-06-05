__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.contrib import admin
from publications.models import Type, Publication, License
from typeadmin import TypeAdmin
from publicationadmin import PublicationAdmin
from licenseadmin import LicenseAdmin

admin.site.register(Type, TypeAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(License, LicenseAdmin)
