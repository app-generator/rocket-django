## Multilanguage

> Intro: What we offer

- Multilanguage for English, German and Italian

> How to use it 
- Currently it only works for http://127.0.0.1:8000/i18n/ this page.
- Load `i18n` tag in the template
```bash
{% load i18n %}
```
- Wrap the translatable content with `{% trans "" %}` tag
```bash
{% trans "CONTENT_NAME" %}
``` 
- Make and compile messages
```bash
django-admin makemessages -l de    # for a specific language
django-admin compilemessages
```
- You will notice that in root directory inside the `local` directory `django.po` file is created. Add your translated content inside the `msgstr`
```bash
msgid "CONTENT_NAME"
msgstr ""
```

> Codebase: related app, model, template, js 

- Multilanguage items are rendered from
    - Templates `templates/pages/i18n.html`
