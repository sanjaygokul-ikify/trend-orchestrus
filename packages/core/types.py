from typing import List, Dict

class TrendData:
    def __init__(self, id: int, name: str, values: List[float]) -> None:
        self.id = id
        self.name = name
        self.values = values

class TrendResult:
    def __init__(self, trend_data: List[TrendData], summary: Dict[str, float]) -> None:
        self.trend_data = trend_data
        self.summary = summary
