import schedule
import time
from app.controller.client_entertainment_repository import EntertainmentController
from app.controller.client_extract_data_repository import ExtractDataController
from app.services.extract_data_repository import ExtractDataRepository
from app.services.entertainment_repository import EntertainmentRepository
from app.utils.created_folder import create_root_folder


def job():
    create_root_folder()
    entertainment_repository = EntertainmentRepository()
    entertainment_controller = EntertainmentController(entertainment_repository)
    urls = entertainment_controller.handle()

    extract_data_repository = ExtractDataRepository(urls)
    extract_data_controller = ExtractDataController(extract_data_repository)
    extract_data_controller.handle()


if __name__ == "__main__":
    job()
    schedule.every().day.at("00:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
