import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def create_product_stripe(course_name):
    stripe_product = stripe.Product.create(name=course_name)
    return stripe_product.get("id")

def create_stripe_price(course_price, stripe_product_id):
    stripe_price=stripe.Price.create(
        currency="rub",
        unit_amount=course_price*100,
        product_data={"name": "payments"},
        product=stripe_product_id,
        )
    return stripe_price


def create_stripe_session(stripe_price):
    session=stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": stripe_price.get("id"),
                     "quantity": 1}],
        mode="payments",
        )
    return session.get("id"), session.get("url")
