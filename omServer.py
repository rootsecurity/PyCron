# coding=utf-8
from datetime import datetime
from rpyc import Service
from crontab import CronTab
from rpyc.utils.server import ThreadedServer

class ManagerService(Service):
    def exposed_cronList(self):
    	jobList=[]
        cron = CronTab(user=True)
        for job in cron:
            if job.is_enabled():
                schedule = job.schedule(date_from=datetime.now())
                
                jobList.append((job.comment,datetime.strftime(schedule.get_prev(),'%Y-%m-%d %H:%M:%S'),datetime.strftime(schedule.get_next(),'%Y
-%m-%d %H:%M:%S'),job.command))
        return jobList
        
s=ThreadedServer(ManagerService,port=7777,auto_register=False)
s.start()
