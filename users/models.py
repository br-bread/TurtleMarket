from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(UserManager):
    def _create_user(self, email, login, password, **extra_fields):

        if not email:
            raise ValueError('Необходимо указать почту')
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            login=login,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, login, password, **extra_fields)

    def create_superuser(self, email, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, login, password, **extra_fields)


class User(AbstractBaseUser):
    login = models.CharField('имя пользователя',
                             max_length=100,
                             help_text='Максимальная длина 100 символов')
    email = models.EmailField('почта',
                              max_length=150,
                              blank=False,
                              unique=True)

    is_staff = models.BooleanField('администрирование', default=False)
    is_superuser = models.BooleanField('админ', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['login', 'password']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.login

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    birthday = models.DateField('день рождения',
                                blank=True,
                                null=True)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return self.user.login


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
