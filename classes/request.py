from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    country: str
    season: str