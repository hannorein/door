#!/bin/bash
export TZ="EST"
rrdtool update temperature.rrd N:`python temp.py`
rrdtool update door_counter.rrd N:`cat door_counter.txt`
rrdtool update sound_counter.rrd N:`cat sound_counter.txt`
rrdtool update movement_counter.rrd N:`cat movement_counter.txt`
rrdtool update alarm_counter.rrd N:`cat alarm_counter.txt`



rrdtool graph temperature_hour.png -v "temp" --start -3600 --end now DEF:temperature=temperature.rrd:temperature:AVERAGE LINE2:temperature#FF0000
rrdtool graph temperature.png -v "temp" --start -86400 --end now DEF:temperature=temperature.rrd:temperature:AVERAGE LINE2:temperature#FF0000
rrdtool graph temperature_week.png -v "temp" --start -604800 --end now DEF:temperature=temperature.rrd:temperature:AVERAGE LINE2:temperature#FF0000
rrdtool graph door_hour.png -v "door" --start -3600 --end now DEF:door=door_counter.rrd:door:MAX LINE2:door#00FF00
rrdtool graph door.png -v "door" --start -86400 --end now DEF:door=door_counter.rrd:door:MAX LINE2:door#00FF00
rrdtool graph door_week.png -v "door" --start -604800 --end now DEF:door=door_counter.rrd:door:MAX LINE2:door#00FF00
rrdtool graph sound_counter_hour.png -v "sound_counter" --start -3600 --end now DEF:sound=sound_counter.rrd:sound:MAX LINE2:sound#00FF00
rrdtool graph sound_counter.png -v "sound_counter" --start -86400 --end now DEF:sound=sound_counter.rrd:sound:MAX LINE2:sound#00FF00
rrdtool graph sound_counter_week.png -v "sound_counter" --start -604800 --end now DEF:sound=sound_counter.rrd:sound:MAX LINE2:sound#00FF00
rrdtool graph movement_counter_hour.png -v "movement_counter" --start -3600 --end now DEF:movement=movement_counter.rrd:movement:MAX LINE2:movement#00FF00
rrdtool graph movement_counter.png -v "movement_counter" --start -86400 --end now DEF:movement=movement_counter.rrd:movement:MAX LINE2:movement#00FF00
rrdtool graph movement_counter_week.png -v "movement_counter" --start -604800 --end now DEF:movement=movement_counter.rrd:movement:MAX LINE2:movement#00FF00
rrdtool graph alarm_counter_hour.png -v "alarm_counter" --start -3600 --end now DEF:alarm=alarm_counter.rrd:alarm:MAX LINE2:alarm#00FF00
rrdtool graph alarm_counter.png -v "alarm_counter" --start -86400 --end now DEF:alarm=alarm_counter.rrd:alarm:MAX LINE2:alarm#00FF00
rrdtool graph alarm_counter_week.png -v "alarm_counter" --start -604800 --end now DEF:alarm=alarm_counter.rrd:alarm:MAX LINE2:alarm#00FF00


cp temperature_hour.png /var/www/html/
cp temperature.png /var/www/html/
cp temperature_week.png /var/www/html/
cp door_hour.png /var/www/html/
cp door.png /var/www/html/
cp door_week.png /var/www/html/
cp sound_counter_hour.png /var/www/html/
cp sound_counter.png /var/www/html/
cp sound_counter_week.png /var/www/html/
cp movement_counter_hour.png /var/www/html/
cp movement_counter.png /var/www/html/
cp movement_counter_week.png /var/www/html/
cp alarm_counter_hour.png /var/www/html/
cp alarm_counter.png /var/www/html/
cp alarm_counter_week.png /var/www/html/
