## Payments

> Intro: What we offer

- Stripe payment gateway

> How to use it 

- Create a `.env` file in the root directory and add the following credentials
```bash
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
```

> Codebase: related app, model, template, js 

- The payment gateway is rendered from
    - Apps `apps/payments`
    - Model `apps/common/models.py`
    - Template `templates/apps/payments`
