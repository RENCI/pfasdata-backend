# Edit the crontab file (I use nano here but you can use any text editor you like)
EDITOR=nano crontab -e

# Add the following line to the crontab file
0 0 * * * bash /home/jmpmcman/dbbackups/pg_backup_rotated.sh >> /projects/pfas/dbbackups/logs/backup.log 2>&1

# verify that the cron job was created
crontab -l
