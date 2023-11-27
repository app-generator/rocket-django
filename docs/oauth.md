## OAuth

> Intro: What we offer

- Google and GitHub login using [django-allauth](https://docs.allauth.org/en/latest/installation/quickstart.html) library.

> How to use it 

- Create a `.env` file in the root directory and add the following credentials
```bash
GOOGLE_CLIENT_ID=
GOOGLE_SECRET_KEY=

GITHUB_CLIENT_ID=
GITHUB_SECRET_KEY=
```

> Codebase: related app, model, template, js 

- The oath is rendered from
    - Template `templates/authentication/sign-in.html`
