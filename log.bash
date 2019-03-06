#!/bin/bash
export TZ="EST"
rrdtool update temperature.rrd N:`python temp.py`
rrdtool update door.rrd N:`cat door_lastminute.txt`
rrdtool update movement.rrd N:`cat movement_lastminute.txt`
rrdtool update sound.rrd N:`cat sound_lastminute.txt`


rrdtool graph temperature.png -v "temp" --start -86400 --end now DEF:myspeed=temperature.rrd:temp:AVERAGE LINE2:myspeed#FF0000
rrdtool graph door.png -v "door" --start -86400 --end now DEF:myspeed2=door.rrd:door:MAX LINE2:myspeed2#00FF00
rrdtool graph movement.png -v "movement" --start -86400 --end now DEF:myspeed2=movement.rrd:movement:MAX LINE2:myspeed2#00FF00
rrdtool graph sound.png -v "sound" --start -86400 --end now DEF:myspeed2=sound.rrd:door:MAX LINE2:myspeed2#00FF00

rrdtool graph temperature_hour.png -v "temp" --start -3600 --end now DEF:myspeed=temperature.rrd:temp:AVERAGE LINE2:myspeed#FF0000
rrdtool graph door_hour.png -v "door" --start -3600 --end now DEF:myspeed2=door.rrd:door:MAX LINE2:myspeed2#00FF00
rrdtool graph movement_hour.png -v "movement" --start -3600 --end now DEF:myspeed2=movement.rrd:movement:MAX LINE2:myspeed2#00FF00
rrdtool graph sound_hour.png -v "sound" --start -3600 --end now DEF:myspeed2=sound.rrd:door:MAX LINE2:myspeed2#00FF00

cp temperature.png /var/www/html/
cp door.png /var/www/html/
cp movement.png /var/www/html/
cp sound.png /var/www/html/

cp temperature_hour.png /var/www/html/
cp door_hour.png /var/www/html/
cp movement_hour.png /var/www/html/
cp sound_hour.png /var/www/html/
