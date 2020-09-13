from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):

    name = models.CharField(_("name"), max_length=150)
    slug = models.SlugField(_("url"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        db_table = 'posts'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
