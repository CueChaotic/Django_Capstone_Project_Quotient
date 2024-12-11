from django.shortcuts import render

# All views
def front_page(request):
    """
    Renders the front (home) page.

    :param request: The request object.
    :param template_name: The name of the template to render.

    :return: The rendered front page template.
    """
    return render(request, 'front_page.html')
