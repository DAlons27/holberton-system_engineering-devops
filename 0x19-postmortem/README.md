# 0x19. Postmortem

<p align="center">
    <img src="meme.JPG" />
</p>

#
<h4>Incident #666</h2>
<h4>Name: Diego Alonso Morey Quispe</h2>
<h4>Date: 2021-12-23</h2>

<h4>Status: Solved </h2>

## Issue Summary:
At approximately 10:00 a.m. on December 23, some of our users are having difficulty loading our website. The BackOffice team began to receive queries and requests from users who were unable to access our platform. The event fired at 10:05 and what happened: A programmer made a typo in the last update to our code base, this error caused our website to fail to load properly and stop with an error, which caused the server to go down, the event in question was detected by the monitoring system at 10:07 which set off alarms and the development team was notified, who began working to find and fix the problem. immediate. This event affected 45% of users in Latin America.

## Timeline:
- **09:45 UTC:** A new update has been uploaded to our website codebase
- **10:00 UTC:** Our BackOffice team started receiving emails from users who had problems loading our website
- **10:04 UTC:** Our monitoring system triggered an alert indicating that the website was down
- **10:07 UTC:** The team received the alert and began working to fix the issue.
- **10:16 UTC:** The team ran some tests and found that the cause was a typo in a library name in an import statement
- **10:20 UTC:** The team fixed the bug and ran tests to make sure it was resolved correctly
- **10:22 UTC:** The corrected version of the code was uploaded to the server
- **10:24 UTC:** The website is back up and running

## Root cause and resolution:

A new code base is successfully uploaded and the developer did not run the tests as usual before committing their changes and uploading the code to production. After the problem was alerted, the team in record time ran the tests to find the problem that caused the server to crash, discovering that it was just a typo in the php file called `wp-settings.php` located in `/var/www /html /`, the problem that caused the problem was an invalid import due to a typo in the file extension of a module being imported.

## Corrective and preventative measures:

From this accident it was learned that the version control system should be automated to not let anyone upload or merge new lines of code if they have not been tested before, this means that programmers in a hurry test their code and identify errors.

