class Api1Session:
    def get(self, member_id: str):
        # Just return mock data
        return {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}


class Api2Session:
    def get(self, member_id: str):
        # Just return mock data
        return {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}


class Api3Session:
    def get(self, member_id: str):
        # Just return mock data
        return {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}
