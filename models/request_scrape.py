from typing import Optional

from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    url: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    viajeros: Optional[int] = None