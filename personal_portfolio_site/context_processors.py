from project2.models import Location


def project_context(request):
    """
    Define a keyword to reference a User object that contains the information
    for the site user (i.e. the person whose credentials and projects are being
    showcased on the website)
    """
    context = {
        'bakery': Location.objects.first()
    }

    return context
