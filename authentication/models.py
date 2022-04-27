from django.db import models
from helpers.models import TrackingModel
from django.core import validators
from django.contrib.auth.models import (
    PermissionsMixin, UserManager, AbstractBaseUser)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import jwt
from datetime import datetime, timedelta
from django.conf import settings


# Validator for username to accept only letter, numbers and _
class AlphaNumericUsernameValidator(validators.RegexValidator):
    regex = r'^[\w][\w\d_]+$'
    message = _(
        "Enter a valid username. This value may contain only letters, numbers and underscore (_)"
    )
    flags = 0


class MyUserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    username_validator = AlphaNumericUsernameValidator()

    bidder_id = models.IntegerField(primary_key=True)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters and digits only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=False, unique=True)

    first_name = models.CharField(_('first name'), max_length=250, blank=False, null=False)
    last_name = models.CharField(_('last name'), max_length=250, blank=False, null=False)
    title = models.CharField(_('user title'), max_length=50, blank=True, null=True)
    address = models.CharField(_('user address'), max_length=250, blank=False, null=False)
    zipcode = models.CharField(_('user zipcode'), max_length=20, blank=False, null=False)
    city = models.CharField(_('user city'), max_length=100, blank=False, null=False)
    phone = models.CharField(_('user phone'), max_length=20, blank=False, null=False)
    office_phone = models.CharField(_('user office phone'), max_length=20, blank=True, null=True)
    country = models.CharField(_('user country'), max_length=50, blank=False, null=False)
    company = models.CharField(_('company name'), max_length=250, blank=True, null=True)

    is_bidder = models.BooleanField(
        _('bidding status'),
        default=False,
        help_text=_(
            'Designates whether the user can bid or not.'),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this users email is verified. '

        ),
    )
    phone_verified = models.BooleanField(
        _('phone_verified'),
        default=False,
        help_text=_(
            'Designates whether this users phone is verified. '

        ),
    )

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        token = jwt.encode(
            {
                'username': self.username,
                'email': self.email,
                'exp': datetime.utcnow() + timedelta(hours=12)
            },
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token
