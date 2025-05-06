from django.db import models
from django.template.context_processors import request
from user.models import User  # Предполагаем, что модель User находится в приложении user
from service.models import Service  # Предполагаем, что модель Service находится в приложении service


class Payment(models.Model):
      PAYMENT_STATUS_CHOICES = [
                ('PENDING', 'Pending'),
                ('COMPLETED', 'Completed'),
                ('FAILED', 'Failed'),
                ('CANCELLED', 'Cancelled'),
            ]
user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')  # Связь с пользователем
service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='payments')  # Связь с сервисом
amount = models.DecimalField(max_digits=10, decimal_places=2) # Сумма
payment_method = models.CharField(max_length=100)  # Метод оплаты
status = models.CharField(
                max_length=10,
                choices=PAYMENT_STATUS_CHOICES,
                default='PENDING'
            )  # Статус оплаты
transaction_error = models.TextField(blank=True, null=True)  # Ошибка транзакции (если есть)
currency = models.CharField(max_length=10)  # Валюта
transaction_id = models.CharField(max_length=255, unique=True)  # Уникальный ID транзакции
created_at = models.DateTimeField(auto_now_add=True)  # Время создания
updated_at = models.DateTimeField(auto_now=True)  # Время последнего обновления

def __str__(self):
    return f"Payment {self.transaction_id} - {self.amount} {self.currency} - {self.status}"

    def mark_as_completed(self):
        self.status = 'COMPLETED'
        self.save()

    def mark_as_failed(self):
        self.status = 'FAILED'
        self.save()

    def cancel_payment(self):
        self.status = 'CANCELLED'
        self.save()


def doctor_queue_view(request):
    doctors = Doctor.objects.all()
    data = []

    for doc in doctors:
        queue_count = doc.patients.filter(in_queue=True).count()
        data.append({
            'doctor': doc,
            'queue_count': queue_count
    })

    return render(request, 'doctors_queue.html', {'data': data})


def adding_doctors_to_clinics(request):


