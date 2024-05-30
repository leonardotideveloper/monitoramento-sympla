import requests


class EntertainmentRepository:
    def __init__(self) -> None:
        self.host = "https://www.sympla.com.br/eventos/rio-de-janeiro-rj/mais-vistos/entretenimento-dia?ordem=location-score"

    def get_entertainment_response(self, page: int):
        headers = {
            "accept": "application/json",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.sympla.com.br",
            "priority": "u=1, i",
            "referer": "https://www.sympla.com.br/eventos/rio-de-janeiro-rj/mais-vistos/entretenimento-dia?ordem=location-score",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }

        json_data = {
            "service": "/v4/mapsearch",
            "params": {
                "only": "name,start_date,end_date,images,event_type,duration_type,location,id,global_score,start_date_formats,end_date_formats,url,company,type",
                "has_banner": "1",
                "themes": "104,105,99,110,113,117,221",
                "sort": "location-score",
                "type": "normal",
                "collections": "200001",
                "city": "Rio%20de%20Janeiro",
                "page": page,
            },
        }
        response = requests.post(
            "https://www.sympla.com.br/api/v1/search", headers=headers, json=json_data
        ).json()

        if len(response["result"]["events"]["data"]) == 0:
            return 404

        return response

    def get_entertainment_repository(self, repositoy_data):

        repositories = []
        if len(repositoy_data["result"]["events"]["data"]) > 0:
            for repository in repositoy_data["result"]["events"]["data"]:

                data = {
                    "url": repository["url"],
                }

                repositories.append(data)
        return repositories
