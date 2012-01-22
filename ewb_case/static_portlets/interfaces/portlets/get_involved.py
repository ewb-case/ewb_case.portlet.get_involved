from zope import schema

from plone.portlets.interfaces import IPortletDataProvider


class IGetInvolved(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """
    
    join_url = schema.URI(
        title=_(u"Join URL"),
        description=_(u"URL the join section links to."),
        required=False
    )
    
    sponsor_url = schema.URI(
        title=_(u"Sponsor URL"),
        description=_(u"URL the sponsor section links to."),
        required=False
    )
    
    mentor_url = schema.URI(
        title=_(u"Mentor URL"),
        description=_(u"URL the mentor section links to."),
        required=False
    )