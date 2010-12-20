#!/bin/bash

NAMEDB="/path/to/namedb/dir"
WGET="/path/to/wget"

cd $NAMEDB
echo "[x] Updating spywaredomains.zones file.."
/bin/cp spywaredomains.zones spywaredomains.zones.old
$WGET -m -nd http://mirror1.malwaredomains.com/files/spywaredomains.zones

echo "[x] Updating malwaredomains.zones file.."
/bin/cp malwaredomains.zones malwaredomains.zones.old
$WGET -m -nd http://mirror1.malwaredomains.com/files/malwaredomains.zones

echo "[x] You must now restart BIND"
