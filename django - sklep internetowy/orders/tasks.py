from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Zadanie wysyłające powiadomienie za pomocą wiadomości email
    po zakończonym powodzeniem utworzeniu obiektu zamówienia
    """
    order = Order.objects.get(id=order_id)
    subject = 'Zamówienie nr {}'.format(order.id)
    message = 'Witaj, {}!\nZłożyleś zamówienie w mnaszym sklepie.\ \
              Identyfikator zamówienia to {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
