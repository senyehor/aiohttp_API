class AppExceptionBase(Exception):
    """base class for all app exception"""


class AppExceptionWithMessageForUser(AppExceptionBase):
    """also includes .message to provide meaningful feedback to user"""
