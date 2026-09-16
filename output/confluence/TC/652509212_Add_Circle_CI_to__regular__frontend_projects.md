---
id: confluence:652509212
source: confluence
type: page
space: TC
title: Add Circle CI to "regular" frontend projects
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652509212
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652509212
---
# Add Circle CI to "regular" frontend projects

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652509212  

## Content

## Setup files in project folder

1. Create a .circleci folder in the root of the project
2. In the following [snippet](https://bitbucket.org/teqplay/workspace/snippets/4najx6) there are 3 files. The `config.yml` should be directly in the `.circleci` folder.
3. The `images/primary/Dockerfile` should also be in the `.circleci` folder but within the folders as shown in the filename. This file is not used since the docker instance is created and runs on Docker. When you want to update for example the node version, you can edit this file and upload/run a new instance. (Something like [this](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html))
4. The last file is for sending a slack message (if you don't need this you can skip this file). So the `postpublish.py` should be in a new folder `scripts` in the root again.
5. The `config.yml` has a few project specific variables that you need to update: 2x `<PROJECT_URL_LIVE>`, `<CLOUDFRONT_ID_LIVE>`, 2x `<PROJECT_URL_DEV>`, `<CLOUDFRONT_ID_DEV>`.
6. Also in the `postpublish.py` there's 2 variables: 2x `<PROJECT_NAME>` and `<SLACK_HOOK_FOR_CHANNEL>`. The last one you need to retreive from slack. [Click](https://teqplaydev.slack.com/apps/A0F7VRE7N-circleci?next_id=0) on `Add to Slack`. For more info about the slack message go to [this wiki page](https://bitbucket.org/teqplay/teqplay-wiki/wiki/How%20to%20add%20a%20fancy%20slack%20CircleCI%20deployment%20message%20to%20your%20frontend%20project).
7. `- run: npm run lint` For this line you need to have a scripts setup in your package.json. If it's not there remove this line from the config. An example of the script: `"eslint --ext .js,.jsx,.ts,.tsx src --color && prettier --check --config ./.prettierrc \"./src/**/*.ts\" \"./src/**/*.tsx\"",`
8. Make sure you have the `predeploy` scripts setup in the package.json. For example: `"predeploy": "react-scripts build && CI=true npm run test",`
9. The full section of `Security vulnerability check` is to run an npm audit. At this moment it's not enable but you can replace the `fill-in-master-to-enable-check` with the branch you want this to run to enable.
10. You can commit this to any branch (master will be automatically run the first time so that's the easiest).

## Setup Circle CI in dashboard

1. Go to the [Circle CI dashboard](https://app.circleci.com/)
2. When logged in, go to projects on the left. Find your repository and click on `Set Up Project`
3. We already setup our own config so click the button on the top `Use Existing Config` and click `Start Building`
4. It will start building the `master` branch. But we do still need to add the config variables. When your project is active you should see a button at the top `Project Settings` go there and select on the left `Environment Variables`. Here you should add two variables: - `DOCKERHUB_PASSWORD`: Search in lastpass on <http://docker.com> and copy the password for teqplay. - `NPM_TOKEN`: Search in lastpass on <http://npmjs.com> and check the notes for teqplay-developer. Here should be the `new token`.

After that you can rebuild the failed one, and it should work.