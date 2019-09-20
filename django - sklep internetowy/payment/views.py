import braintree
from django.shortcuts import render,redirect, get_object_or_404
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
# import weasyprint
from io import BytesIO


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # Pobranie tokena nonce
        nonce = request.POST.get('payment_methon_nonce', None)
        # Utworzenie i przesłanie transakcji
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # Oznaczenie zamówienia jako opłącone
            order.paid = True
            # Zapisanie unikatowego identyfikatora transkcji
            order.braintree_id = result.transaction.id
            order.save()
            # Utworzenie wiadomości email zawierającej rachunek
            """
            subject = 'Mój sklep - rachunek nr {}'.format(order.id)
            message = 'W załączniku przesyłamy rachunek dla ostatniego zakupu.'
            email = EmailMessage(subject, message, 'admin@myshop.com',[order.email])
            """
            # Wygenerowanie dokumentu pdf
            """
            html = render_to_string('orders/order/pdf.html', {'order': order})
            out = BytesIO()
            stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
            """
            # Dołączenie pliku w formacie pdf
            """
            email.attach('order_{}.pdf'.format(order.id),out.getvalue(),'application/pdf')
            """
            # Wysłanie wiadomości email
            """
            email.send()
            """
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # Wygenerowanie tokena
        client_token = braintree.ClientToken.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
