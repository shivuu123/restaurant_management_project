from django import template
register = template.Library()
@register.filter
def availability(item):
    """
    Returns the item name if available, otherwise 'Coming Soon'.
    """
    if hasattr(item, 'available') and not item.available:
        return f"{item.name} (Coming Soon)"
    return item.name