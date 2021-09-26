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