from django.http import HttpResponse


# Handle Stripe webhooks
class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    # Handle webhook event
    def handle_event(self, event):
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    # Handle payment_intent.succeeded webhook
    def handle_payment_intent_succeeded(self, event):
        
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Handle the payment_intent.payment_failed webhook
    def handle_payment_intent_payment_failed(self, event):
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)