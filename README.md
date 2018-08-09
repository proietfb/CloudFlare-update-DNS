# CloudFlare DNS Updater
This script is used to update cloudflare DNS ips on servers that are connected using a dynamic IP address.

## Add a crontab 
To automatically update Cloudflare ip address define a `crontab` that run script every a given time.

To open crontab file perform `$ crontab -e` and add the following line:

`*/5 * * * * /usr/bin/python /path/to/cloudflareUpdateDNS.py >/dev/null 2>&1`.

This run python script every 5 minutes.

To check crontab log file perform `$ less /var/log/syslog`.

## More resources
- [Cloudflare API](https://api.cloudflare.com/)
- [crontab Tutorial](http://www.adminschoice.com/crontab-quick-reference)
