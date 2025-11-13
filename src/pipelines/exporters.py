from typing import Any, Dict, List

from pydantic import BaseModel

def _model_to_dict(model: BaseModel) -> Dict[str, Any]:
    # Pydantic v1/v2 compatibility
    if hasattr(model, "model_dump"):
        return model.model_dump()  # type: ignore[no-any-return]
    return model.dict()  # type: ignore[no-any-return]

class JsonExporter:
    """
    Utility to convert Reel models into plain JSON-serializable dicts.
    """

    @staticmethod
    def to_dict(model: BaseModel) -> Dict[str, Any]:
        return _model_to_dict(model)

    @staticmethod
    def to_list(models: List[BaseModel]) -> List[Dict[str, Any]]:
        return [_model_to_dict(m) for m in models]