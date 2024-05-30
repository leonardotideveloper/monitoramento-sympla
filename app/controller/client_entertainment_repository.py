import requests


class EntertainmentController:
    def __init__(self, entertainment_repository) -> None:
        self.entertainment_repository = entertainment_repository

    def handle(self):
        try:
            results = []
            page = 1
            while True:
                response = self.entertainment_repository.get_entertainment_response(
                    page
                )
                if response == 404:
                    break

                repositories = (
                    self.entertainment_repository.get_entertainment_repository(response)
                )
                results += repositories
                page += 1
            return results

        except requests.exceptions.RequestException as e:
            raise f"An error occurred: {e}"
        except Exception as e:
            raise f"An unexpected error occurred: {e}"
