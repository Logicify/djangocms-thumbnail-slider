from django import forms
from django.utils.translation import ugettext_lazy as _
from djangocms_thumbnail_slider import models


# Create your forms here
class ThumbnailSlideForm(forms.ModelForm):
    class Meta:
        model = models.ThumbnailSlide
        fields = '__all__'

    def clean(self):
        data = super(ThumbnailSlideForm, self).clean()
        if data['image'] is None and not data['link']:
            self.add_error('image', _('Image or link should be provided'))
            self.add_error('link', _('Image or link should be provided'))
        return data
