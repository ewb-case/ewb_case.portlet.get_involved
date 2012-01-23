from zope.i18nmessageid import MessageFactory

_ = MessageFactory('ewb_case.portlet.get_involved')


def initialize(context):
    """Initializer called when used as a Zope 2 product.
    """
    
    # Register SVG File Extensions for CMF
    from Products.CMFCore.DirectoryView import registerFileExtension
    from Products.CMFCore.FSFile import FSFile
    
    registerFileExtension('svg', FSFile)
