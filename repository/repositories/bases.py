from abc import ABC

from utils.crud_protocol import CRUDOperationsBase, ModelObject


class CRUDRepositoryBase(CRUDOperationsBase, ABC):
    model_class: type[ModelObject]
