from django.contrib.auth.models import User


def project_context(request):
    """
    Define a keyword to reference a User object that contains the information
    for the site user (i.e. the person whose credentials and projects are being
    showcased on the website)
    """
    context = {
        'me': User.objects.first(),
    }

    return context
