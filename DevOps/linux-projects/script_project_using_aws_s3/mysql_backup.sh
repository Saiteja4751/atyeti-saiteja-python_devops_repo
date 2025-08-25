#!/bin/bash
set -e
#
## Set variables
DB_NAME="testdb"
DB_USER="root"
DB_PASS="root"
BACKUP_DIR="/home/saiteja/script_project_using_aws_s3"
DATE=$(date +%F_%T)
FILENAME="$DB_NAME-$DATE.sql"
ARCHIVE="$FILENAME.tar.gz"
S3_BUCKET="s3://your-mysql-backup-bucket0001"
#
## Create backup directory if not exists
mkdir -p $BACKUP_DIR
#
## Dump the database
mysqldump -u $DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$FILENAME
#
## Compress the SQL file
tar -czf $BACKUP_DIR/$ARCHIVE -C $BACKUP_DIR $FILENAME
#
## Upload to S3
aws s3 cp $BACKUP_DIR/$ARCHIVE $S3_BUCKET
#
## Clean up old files
rm $BACKUP_DIR/$FILENAME
find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +7 -exec rm {} \;
#
echo "✅ Backup completed and uploaded to S3: $ARCHIVE"
#
