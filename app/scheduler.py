from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from app.worker.tasks import collect_price


def start_scheduler() -> BackgroundScheduler:
    scheduler = BackgroundScheduler(timezone="UTC")

    scheduler.add_job(
        func=lambda: collect_price.delay(),
        trigger=CronTrigger(minute="*"),
        id="get_price_job",
        replace_existing=True,
    )
    scheduler.start()
    return scheduler
