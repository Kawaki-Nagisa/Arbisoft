Write a Django management command update/create records in the database

Writing A Django Management Command that will run and store Records in the Database. Inserts Dummy Users in the Database using management commands. It will also store 100 PST date times in a separate table. There will be a scheduled Cron Job, that will run after every 5 minutes and update 10 date times in UTC. Once all 100 date times are in UTC, the cron job will start converting date time objects in PST. and this will continue
