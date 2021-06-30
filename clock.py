from scrape import scrape

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=15)
def update():
    scrape()
    print("worldometer live updated")

sched.start()