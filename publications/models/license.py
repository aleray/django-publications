__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'


from django.db import models
from publications.models.orderedmodel import OrderedModel


class License(OrderedModel):
    class Meta:
        ordering = ('order',)
        app_label = 'publications'

    type = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    url = models.URLField(verify_exists=False, max_length=255, blank=True)
    jurisdiction = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    hidden = models.BooleanField(help_text='Hide license from main view.')

    def __unicode__(self):
        return self.type
