from django import template

from nail.models import Services, Pages, Header


register =template.Library()

@register.inclusion_tag('tags/services.html')
def get_services():
    services = Services.objects.all()
    return {'services':services}

@register.inclusion_tag('tags/pages.html')
def get_pages():
    pages = Pages.objects.order_by('id')
    return {'pages': pages}

@register.inclusion_tag('tags/footer_services.html')
def get_footer_serv():
    services = Services.objects.all()
    return {'services': services}

@register.inclusion_tag('tags/footer_social.html')
def get_footer_social():
    social = Header.objects.all()
    return {'social': social}

