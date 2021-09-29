from django.apps import AppConfig

# Config checkout app
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals