import requests
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models import Asset

def check_assets_health():
    """
    Called by the scheduler every minute.
    Checks each asset's health by sending a GET request to its 'name' (treated as URL).
    """
    db: Session = SessionLocal()
    assets = db.query(Asset).all()

    for asset in assets:
        try:
            response = requests.get(asset.name, timeout=3)
            if response.status_code == 200:
                asset.status = "Online"
            else:
                asset.status = "Unstable"
        except Exception:
            asset.status = "Offline"

    db.commit()
    db.close()


def start_scheduler():
    """
    Initializes and starts the background scheduler when the app boots.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_assets_health, "interval", seconds=60)
    scheduler.start()
