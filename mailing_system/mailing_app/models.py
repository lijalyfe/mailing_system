from django.db import models


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    comment = models.TextField()


class MailingSettings(models.Model):
    TIME_CHOICES = [
        ('once a day', 'Once a day'),
        ('once a week', 'Once a week'),
        ('once a month', 'Once a month'),
    ]

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('created', 'Created'),
        ('started', 'Started'),
    ]

    sending_time = models.TimeField()
    frequency = models.CharField(max_length=20, choices=TIME_CHOICES)
    mailing_status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class MailingMessage(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()


class MailingLog(models.Model):
    last_attempt_datetime = models.DateTimeField()
    ATTEMPT_STATUS_CHOICES = [
        ('success', 'Success'),
        ('error', 'Error'),
    ]
    attempt_status = models.CharField(max_length=10, choices=ATTEMPT_STATUS_CHOICES)
    mail_server_response = models.TextField()


class Mailing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE)
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE)
    logs = models.ForeignKey(MailingLog, on_delete=models.CASCADE)

