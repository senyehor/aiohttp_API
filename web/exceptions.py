from typing import Any, Optional

from aiohttp.typedefs import LooseHeaders
from aiohttp.web_exceptions import HTTPBadRequest, HTTPInternalServerError

from utils.exceptions import AppExceptionWithMessageForUser
from web.utils import CommonQueryParameters


class DataWasNotFoundOrIncorrect(HTTPBadRequest, AppExceptionWithMessageForUser):
    data_name = None

    # pylint: disable-next=too-many-arguments
    def __init__(
            self, *, headers: Optional[LooseHeaders] = None, reason: Optional[str] = None,
            body: Any = None, text: Optional[str] = None,
            content_type: Optional[str] = None
    ) -> None:
        if reason:
            raise ValueError('Reason is auto-generated via data_name attribute')
        composed_reason = self.__compose_reason()
        super().__init__(
            headers=headers, reason=composed_reason, body=body,
            text=text, content_type=content_type
        )

    def __compose_reason(self) -> str:
        return f'Failed to get {self.data_name} from the request, ' \
               f'is it present and has correct format?'


class PageSizeIncorrect(DataWasNotFoundOrIncorrect):
    data_name = CommonQueryParameters.PAGE_SIZE


class PageNumberIncorrect(DataWasNotFoundOrIncorrect):
    data_name = CommonQueryParameters.PAGE_NUMBER


class ObjectIdNotFoundOrIncorrect(DataWasNotFoundOrIncorrect):
    data_name = CommonQueryParameters.OBJECT_ID


class FailedToDeleteObject(HTTPInternalServerError):
    pass


class FailedToUpdateObject(HTTPInternalServerError):
    pass
