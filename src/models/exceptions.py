class ModelNotFoundError(Exception):
    """
    Raised when the equipment model ID is not found in the dataset.
    """
    def __init__(self, model_id: str):
        super().__init__(f"Model ID '{model_id}' not found.")
        self.model_id = model_id


class InvalidYearError(Exception):
    """
    Raised when the requested year is not found and no default ratios are available.
    """
    def __init__(self, year: str, model_id: str):
        super().__init__(f"Year '{year}' not found for model ID '{model_id}', and no default ratios available.")
        self.year = year
        self.model_id = model_id