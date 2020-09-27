from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def get_default_text():
    return 'my new default text'

def validate_year(value):
    today = now()
    if value > today.year:
        raise ValidationError(_(f'{value} превышает текущий год!'))


class Post(models.Model):

    myid = models.AutoField(
        _("myid"),
        primary_key=True
    )

    YEAR = [
        (None, '========'),
        (2009, 2009),
        (2010, 2010),
        (2011, 2011),
        (2012, 2012),
        (2013, 2013),
        (2022, 2022),
    ]

    choice_year = models.PositiveSmallIntegerField(
        _("year"),
        choices=YEAR,
        validators=[validate_year]
    )

    slug = models.SlugField(
        _("url"),

        unique=True,

        help_text='<i>Введите УРЛ для записи</i>',

        # ? Разобраться почему не переопределилось сообщение 'blank'
        error_messages={
            'unique': 'Поле должно быть уникальным!',
            'blank': 'Поле надо заполнить!'
        } # null, blank, invalid, invalid_choice, unique, и unique_for_date.
    )

    name = models.CharField(
        verbose_name=_("name"),

        db_column='some_name',

        unique=True,
        null=True,
        blank=True,

        max_length=150
    )

    pub_date = models.DateField(_("published date"))

    text = models.TextField(
        _("text"),
        blank=True,

        unique_for_date='pub_date',
        # unique_for_month='pub_date',
        # unique_for_year='pub_date',

        default=get_default_text,

        db_index=True,
        # db_tablespace='name_tablespace',

        # editable=False,
    )

    fk = models.ForeignKey("self", verbose_name=_("fk self"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        db_table = 'posts'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
