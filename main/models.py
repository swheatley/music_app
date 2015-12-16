from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Genres(models.Model):
    genre_id = models.IntegerField(null=True, blank=True)
    genre_parent_id = models.IntegerField(null=True, blank=True)
    genre_title = models.CharField(max_length=255, null=True, blank=True)
    genre_slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural='Genres'

    # # class Meta:
    #     ordering = ('created', )

    def __unicode__(self):
        return self.genre_title


class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_url = models.URLField(max_length=255, null=True, blank=True)
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    artist_bio = models.TextField(null=True, blank=True)
    artist_location = models.CharField(max_length=255, null=True, blank=True)
    artist_website = models.CharField(max_length=255, null=True, blank=True)
    artist_handle = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.artist_name  


class Albums(models.Model):
    album_id = models.IntegerField(primary_key=True)
    artist = models.ForeignKey('main.Artist', null=True)
    album_title = models.CharField(max_length=255, null=True)
    album_date_released = models.IntegerField(null=True, blank=True)
    album_image = models.ImageField(upload_to="album_images")

    class Meta:
        verbose_name_plural='Albums'

    def __unicode__(self):
        return self.album_title


class Tracks(models.Model):
    track_id = models.IntegerField(null=True, blank=True)
    album = models.ForeignKey('main.Albums', null=True)
    genre = models.ForeignKey('main.Genres', null=True)
    track_title = models.CharField(max_length=255, null=True)
    track_file = models.FileField(upload_to="tracks")

    class Meta:
        verbose_name_plural='Tracks'

    def __unicode__(self):
        return self.track_title


class CustomUserManager(BaseUserManager):  
    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if username != None:
            email = username

        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


