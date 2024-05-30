from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from app.utils.writer_file import write_csv
import json
import re
import requests


class ExtractDataRepository:
    def __init__(self, url) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        self.host = url
        self.driver = webdriver.Chrome(options=options)

    def exit(self):
        self.driver.quit()

    def get_data_repository(self):
        results = []
        for url in self.host:
            if not "bileto" in url["url"]:
                self.driver.get(url["url"])

                if "404" in self.driver.current_url:
                    continue

                wait = WebDriverWait(self.driver, 60)
                content = wait.until(
                    EC.presence_of_element_located((By.ID, "__NEXT_DATA__"))
                )
                script_content = content.get_attribute("innerHTML")
                data = json.loads(script_content)
                name = data["props"]["pageProps"]["hydrationData"]["eventHydration"][
                    "event"
                ]["name"]
                detail = data["props"]["pageProps"]["hydrationData"]["eventHydration"][
                    "event"
                ]["strippedDetail"]
                detail = re.sub(r"&nbsp;", " ", detail)
                detail = re.sub(r"\s+", " ", detail).strip()

                address = data["props"]["pageProps"]["hydrationData"]["eventHydration"][
                    "event"
                ]["eventsAddress"]

                address_completed = (
                    address["address"]
                    + ","
                    + address["addressNum"]
                    + " - "
                    + address["neighborhood"]
                )
                date_event = data["props"]["pageProps"]["hydrationData"][
                    "eventHydration"
                ]["event"]["startDateMultiFormat"]["ptBR"]
                about = data["props"]["pageProps"]["hydrationData"]["eventHydration"][
                    "event"
                ]["eventsHost"]["name"]

                data = {
                    "Nome do evento": name,
                    "Data do evento": date_event,
                    "Endereco do evento": address_completed,
                    "Descricao do evento": detail,
                    "Sobre o produtor": about,
                }

                results.append(data)
            else:
                id = re.findall(r"\d+", url["url"])[0]
                url_bileto = (
                    f"https://bff-sales-api-cdn.bileto.sympla.com.br/api/v1/events/{id}"
                )
                headers = {
                    "accept": "application/json",
                    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "no-cache",
                    "origin": "https://bileto.sympla.com.br",
                    "pragma": "no-cache",
                    "priority": "u=1, i",
                    "referer": "https://bileto.sympla.com.br/",
                    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                    "x-api-key": "cQkazy2Wc",
                }

                response = requests.get(
                    url=url_bileto,
                    headers=headers,
                ).json()

                date_time = response.get("data").get("next_local_date_time")
                if date_time:
                    date_time = (
                        date_time[8:10]
                        + "-"
                        + date_time[5:7]
                        + "-"
                        + date_time[:4]
                        + " "
                        + date_time[11:16]
                    )
                html_description = response.get("data").get("description").get("raw")
                if html_description:
                    description = re.sub(r"<.*?>", "", html_description)
                    description = re.sub(r"\s+", " ", description).strip()
                else:
                    description = None
                data = {
                    "Nome do evento": response.get("data").get("name"),
                    "Data do evento": date_time,
                    "Local do evento": response.get("data")
                    .get("venue")
                    .get("locale")
                    .get("address"),
                    "Descricao do evento": description,
                    "Sobre o produtor": "",
                }
                results.append(data)

        write_csv("eventos.csv", results)
        return results
