from zope.interface import implements
from zope.formlib import form

from plone.app.portlets.portlets import base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from ewb_case.portlet.get_involved.interfaces import IGetInvolved


class Assignment(base.Assignment):
    """Get Involved Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IGetInvolved)

    join_url = u""
    sponsor_url = u""
    mentor_url = u""

    def __init__(self, join_url=u"", sponsor_url=u"", mentor_url=u""):
        self.join_url = join_url
        self.sponsor_url = sponsor_url
        self.mentor_url = mentor_url
        
    @property
    def title(self):
        """The title of the portlet used in the "manage portlets" screen.
        """
        return "Get Involved"


class Renderer(base.Renderer):
    """Get Involved Portlet renderer.
    """

    render = ViewPageTemplateFile('./templates/get_involved.pt')


class AddForm(base.AddForm):
    """Get Involved Portlet add form.
    """
    form_fields = form.Fields(IGetInvolved)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Get Involved Portlet edit form.
    """
    form_fields = form.Fields(IGetInvolved)
