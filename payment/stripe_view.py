import stripe
from career_studio import settings

# configure stripe key
stripe.api_key = settings.STRIPE_SECRET_KEY


def generate_account_key(email):
    obj = stripe.Account.create(
        type="express",
        country="US",
        email=email,
        capabilities={
            "card_payments": {"requested": True},
            "transfers": {"requested": True},
        },
    )
    if obj.id:
        return obj.id
    return None


def generate_account_link(account_key):
    stripe_obj = stripe.AccountLink.create(
        account=account_key,
        refresh_url="https://example.com/reauth",
        return_url="https://example.com/return",
        type="account_onboarding",
    )
    if stripe_obj:
        return stripe_obj
    return None


def stripe_charge_create(expiry, amount, card_number, cvc):
    exp_month = expiry[0:2]
    exp_year = expiry[3:5]
    amount_sent = int(amount) * 100
    account = stripe.Token.create(
        card={
            "number": card_number,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc,
        },
    )
    if account.id:
        charge_create = stripe.Charge.create(
            amount=amount_sent,
            currency="usd",
            source=account.id,
            description="My First Test Charge (created for API)",
        )
        if charge_create:
            return charge_create.id
        return False
    return False
