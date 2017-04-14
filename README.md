# AdobeSyncAlert
Generates an alert if the Adobe User Sync Tool returns an error. This is accomplished by reading the log files generated by the User Sync Tool.

##Expects:
- Environment Variables
-- LOGPATH - full path to your Adobe User Sync logs
-- ARN - the ARN for your SNS topic
-- AWS\_ACCESSKEY\_ID - The AccessKey ID for the IAM user that will be publishing to your SNS topic
-- AWS\_SECRET\_ACCESS\_KEY - If I told you it wouldn't be a secret anymore
-- AWS\_DEFAULT\_REGION - The default AWS region (surprised?)
-- LOOKBACK - How far back the script should look through the logs, in seconds. This should be the same as the interval between calls to the Adobe User Sync tool.
- Python Packages
-- boto3 (the AWS SDK/API for Python)
- Configuration Changes
-- The User Sync Tool must be configured to write to a log file. This is done in its configuration (log\_to\_file: True).

##So how do I use this?
Install and configure the Adobe User Sync Tool (https://github.com/adobe-apiplatform/user-sync.py). Write a brief script/batch file that will run the User Sync Tool, followed by this tool. Add a crontab entry for that script. If on Windows, use the Task Scheduler. You may wish to use the included start.sh script if you are on Linux to set the appropriate environment variables. I would recommend setting up logrotate or something similar, as the logs from the User Sync Tool will eventually fill your disk.

SNS code is from comment in https://gist.github.com/tfhartmann/8956049
