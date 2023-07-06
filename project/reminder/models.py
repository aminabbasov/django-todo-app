from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Фабрику какую нибудь.
# Q, F объекты.
# запросы к связанным моделям чрез select и perfetch related.
# Общую оптимизацию запросов.
# Если еще и индексы будут - вообще шикарно.
# В пользователях -- сигналы показать, например.


class ReminderModel(models.Model):
    # Coloring going on in templatetags
    COLOR_CHOICES = [
        ('7', 'Сolorless'),
        ('0', 'Red'),
        ('1', 'Orange'),
        ('2', 'Yellow'),
        ('3', 'Green'),
        ('4', 'Cyan'),
        ('5', 'Blue'),
        ('6', 'Purple'),
    ]

    user           = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False
    )
    title          = models.TextField(null=False, blank=False)
    is_completed   = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    selected_color = models.CharField(
        max_length=100, choices=COLOR_CHOICES, default='7'
    )

    def get_absolute_url(self):
        return reverse('update-page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Reminder'
        verbose_name_plural = 'Reminders'
