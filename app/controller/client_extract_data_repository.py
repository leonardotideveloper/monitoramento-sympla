class ExtractDataController:
    def __init__(self, extract_data_repository) -> None:
        self.extract_data_repository = extract_data_repository

    def handle(self):
        try:
            self.extract_data_repository.get_data_repository()
        except Exception as e:
            raise f"An unexpected error occurred: {e}"
        finally:
            self.extract_data_repository.exit()
