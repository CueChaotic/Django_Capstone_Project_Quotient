from django.shortcuts import render

# All views
def store_page(request):
    """Renders the store page.

    :param request: The request object.
    :param template_name: The name of the template to render.

    :return: The rendered store page template.
    """
    return render(request, "store_page.html")
