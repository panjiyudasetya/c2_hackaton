---
id: confluence:181075975
source: confluence
type: page
space: TC
title: Add Slack deployment message to your project
author: Damon Asberg
date: '2023-05-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181075975
explicit_links: []
---
# Add Slack deployment message to your project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181075975  

## Content

1. Get your slack webhook URL for a channel of choice here by clicking “add to slack” <https://teqplaydev.slack.com/apps/A0F7VRE7N-circleci?next_id=0>
2. Make sure the attached `postpublish.py` script is in the /scripts folder inside the root of the repository. Replace `<ADD_YOUR_WEBHOOK_HERE>` inside the script on the last line with the webhook you retrieved from step 1.

   pyimport json
   import time
   import urllib2
   import sys
   def send\_notification(hook, url, branch, user, color, commit\_msg, circleCIURL):
   package = json.load(open("package.json"))
   body = {
   'attachments': [{
   'fallback': 'Version %s has been deployed to %s' % (package['version'], url),
   'color': color,
   'title': 'Version %s has been deployed to %s' % (package['version'], url),
   'text': '%s' % (commit\_msg),
   'fields': [
   {'title': 'User', 'value': user},
   {'title': 'Version', 'value': package['version'], 'short': True},
   {'title': 'Branch', 'value': branch, 'short': True}
   ],
   'ts': str(int(time.time())),
   }, {
   'type': 'button',
   'name': 'circle',
   'text': '<%s|View on CircleCI>' % (circleCIURL),
   'mrkdwn\_in': 'text'
   }]
   }
   req = urllib2.Request(hook, json.dumps(body), {'Content-Type': 'application/json'})
   urllib2.urlopen(req)
   send\_notification('<ADD\_YOUR\_WEBHOOK\_HERE>', sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
3. Adjust your `.circleci/config.yml` file to make sure the message actually gets sent. This is the harder step as every projects `config.yml` file is a little different.

* Somewhere inside the build job before the `persist_to_workspace` step, you will need to make sure you write your last GIT commit message to a file. For the Port Reporter project, I placed it after setting the npm token part. It will write the message to the `scripts/.COMMIT_MESSAGE` file.

#!yml
- run:
name: 'Setting commit message in file'
command: |
touch scripts/.COMMIT\_MESSAGE
echo "$(git log --format=%B -n 1)" >> scripts/.COMMIT\_MESSAGE

* Next still inside the build job, you need to make sure certain files persist across multiple jobs. We do this with the `persist_to_workspace` step. Make sure this is the last step in the build job if it isn’t already.

#!yml
- persist\_to\_workspace:
root: ~/repo
paths:
- www # CHANGE THIS WITH THE NAME OF YOUR BUILD FOLDER
- package.json
- scripts/.COMMIT\_MESSAGE
- scripts/postpublish.py

* Lastly we will add the actual notification posting step inside the deploy job. This snippet should be the final thing inside of the deploy job, as the deployment has already finished and is successful. This snippet also takes multiple branches into account, so the URL would be different for different branches. Replace `portreporter.teqplay.nl` and `portreporterdev.teqplay.nl` and the `#HEX_COLOR` with your own colors of choice.

> The color you select will be the color of the lineblock, which is currently white in this line of text but can be any hex color you want. I chose two distinctive colors from the portreporter style (live: #E8A61A, dev: #0182B5) so you can easily see what is a live and dev deployment.

#!YML
- run:
name: 'Post notification to Slack'
command: |
COMMIT\_MESSAGE=$(cat "scripts/.COMMIT\_MESSAGE")
if [ "${CIRCLE\_BRANCH}" == "master" ]; then
python scripts/postpublish.py portreporter.teqplay.nl $CIRCLE\_BRANCH $CIRCLE\_USERNAME '#e8a61a' "$COMMIT\_MESSAGE" $CIRCLE\_BUILD\_URL
else
python scripts/postpublish.py portreporterdev.teqplay.nl $CIRCLE\_BRANCH $CIRCLE\_USERNAME '#0182b5' "$COMMIT\_MESSAGE" $CIRCLE\_BUILD\_URL
fi

Thats it! Run your build and you should be good to go. For reference see the portreporter-frontend `config.yml` <https://bitbucket.org/teqplay/portreporter-frontend/src/develop/.circleci/config.yml> to see a working version.