from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager

from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """
