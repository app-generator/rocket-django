## Extended User Model

> Intro: What we offer

An extended Django user model is a custom Django model that inherits from Django's built-in User model and adds additional fields or methods to provide more functionality or store more information about users. This is useful when you need to store additional user-specific data or implement custom user management logic beyond what the built-in User model offers.


### Reasons for extending the Django User model

Here are some common reasons for extending the Django user model:

- Store additional user data: If you need to store additional user information, such as a profile picture, date of birth, or phone number, you can add these fields to the extended user model.

- Implement custom user management logic: If you need to implement custom user management logic, such as adding custom registration or authentication workflows, you can override the methods of the built-in User model in your extended user model.

- Integrate with third-party services: If you need to integrate your Django application with third-party services, such as social login providers or payment gateways, you can add fields or methods to your extended user model to store and manage the necessary information.

- Extending the Django user model allows you to tailor the user management functionality of your application to your specific needs and requirements.

> Codebase: related app, model, template, js 

### Rocket Django User model

**Rocket Django** uses an extended user model that allows additional user information to be saved. An authenticated user can save their information and an image avatar. The extended user model is defined in the `apps/users/models.py` file. The `Profile` model in `apps/users/models.py` stores additional user information like full name, address, and avatar.

```py
# apps/users/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


ROLE_CHOICES = (
    ('admin'  , 'Admin'),
    ('user'  , 'User'),
)
class Profile(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    role      = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    full_name = models.CharField(max_length=255, null=True, blank=True)
    country   = models.CharField(max_length=255, null=True, blank=True)
    city      = models.CharField(max_length=255, null=True, blank=True)
    zip_code  = models.CharField(max_length=255, null=True, blank=True)
    address   = models.CharField(max_length=255, null=True, blank=True)
    phone     = models.CharField(max_length=255, null=True, blank=True)
    avatar    = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.user.username
```

The model is implemented by creating a new model called `Profile` that holds a One-To-One relationship with the existing `User` Model through a `OneToOneField`. This allows extra information to be associated with a user. This can be customised to suit your project needs.


### The `ProfileForm`
The `Profile` model has it's form called `ProfileForm` that can be used to add profile details. The `ProfileForm` can be found in `apps/users/forms.py`.
```py
# apps/users/forms.py
...
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'role', 'avatar',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            self.fields[field_name].widget.attrs['required'] = False
```

- To enable the use of the form, it is sent as a context from the views, and rendered on the template. The `profile` function of `apps/users/views.py` shows how this is done.
```py
# apps/users/views.py
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'form': form,
        'segment': 'profile',
    }
    return render(request, 'dashboard/profile.html', context)
```

- This form is used in the `templates/dashboard/profile.html` to allow the update of user data as seen below:
```jinja
<!--templates/dashboard/profile.html line 88-->
{% for field in form %}
    <div class="col-span-6 sm:col-span-3">
        <label for="first-name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ field.label }}</label>
        {{ field }}
    </div>
{% endfor %}
```

Visit http://localhost:8000/users/profile to interact with the **Rocket Django** profile form. This can be adapted easily into any page of the route you want for your application.

![Rocket Django - Styled with Tailwind-Flowbite AppSeed - User profile page](https://github.com/app-generator/dummy/assets/57325382/5488a471-2398-4565-aaf1-fbcfa5b9843b)


## Conclusion
Easily store additional user data, implement custom authentication logic, and integrate with third-party services, all while maintaining the security and reliability of Django's built-in user model. Take control of your user management and tailor it to your specific needs with Rocket Django.

## ✅ Resources
- 👉 [Rocket Django](https://docs.appseed.us/products/rocket/django/) product offering
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**
