from zope.i18nmessageid import MessageFactory
DontateEwbMessageFactory = MessageFactory('ewb_case.static_portlets')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
