from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


class ImagerProfileManager(models.Manager):
    """Create manager to track active users."""

    def get_queryset(self):
        """Get queryset and return all active users."""
        qs = super(ImagerProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Extend user profile and functionality."""

    PHOTO_TYPE = (
        ('N', 'Nature Photography'),
        ('S', 'Sports/Action Photography'),
        ('F', 'Family/Maternity'),
        ('E', 'Event/Wedding Photography'),
        ('A', 'Architectural Photography')
    )

    @property
    def is_active(self):
        """Create property that returns user active status."""
        return self.user.is_active

    def __str__(self):
        """Return string of ImageProfile user's username."""
        return self.user.username

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile', null=False)
    objects = models.Manager()
    active = ImagerProfileManager()
    camera = models.CharField(max_length=255)
    friends = models.ManyToMany(settings.AUTH_USER_MODEL,
                                related_name='friends_of')
    photography_type = models.CharField(max_length=1,
                                        choices=PHOTO_TYPE,
                                        default='N')
    location = models.CharField(max_length=255)
