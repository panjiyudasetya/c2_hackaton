---
id: confluence:206864392
source: confluence
type: page
space: TC
title: SOF OCR project design
author: Michel Wilson
date: '2023-08-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206864392
explicit_links: []
---
# SOF OCR project design

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206864392  

## Content

## Functional requirements

* Extract key/value information (Textract, initially) from one or more PDFs:

  + Information defining the visit: vessel, IMO, port, terminal, agent, etc
  + Time stamps for various points in the visit (to be defined)
  + Delays, reasons for the delays
* Query the status of the extraction process
* Run an extraction again
* Stop an ongoing extraction process
* Store all relevant output for future model training

## Non-functional requirements

* Skeleton-based, using mongo for persistence and an S3 bucket for the PDFs
* Ability to switch from Textract to PaddleOCR or something like that
* Vertical scalability, especially if we want to use PaddleOCR

## High-level sprint planning

### Sprint 1

#### Setup skeleton-based project (4d)

Create the basic project structure based on skeleton, but as a multi-module project: one module for the API application, one module for the job runners/parsing itself, and another module for the models and API. Reason for this: we want the ability to have a separate deployment for the API and for the runners, which will give us the option for horizontal scaling of the runners in the future. Ideally this multi-module project should re-use the Gradle convention plugins we started using in ais-engine.

This task should also include CI setup, deployment setup, a database (Mongo?) and an S3 bucket into which the uploaded PDFs are going to be stored.

#### Model and API definition (2d)

Envision and setup the models and an outline of the API endpoints, based on the following rough outline of the functionality of the application:

* submit a job, get token/id  
  Upload of one or more PDFs and accompanying metadata and options for the job. The reply should contain a token or id for further interaction
* get status/output based on token/id  
  Return the status for a submitted job based on the token or id. Should be something like “in progress”, “failure” (with explanation) or “complete”. If the job is complete, all the relevant information that has been extracted from the document should also be returned.
* ability to download PDFs for a job, also based on the token/id for a job  
  one endpoint to get a list of PDFs for the job (there can be multiple), maybe provide name/size(/metadata?), and one endpoint to download a single PDF, based on an id? in the previous list?
* optionally, re-process a job  
  Using the saved PDF, re-start the parsing process. This could be useful during development to retry after a new version has been deployed. Ideally, this should not overwrite the stored data of the previous run, but just add a new version of the data.
* Think about whether we want to have some form of callback mechanism instead: provide a URL during submission that gets called with status updates.

In this phase, the outline of the result model should also be created, as in, we need to define which data bits we are going to try to extract from the SOFs, and we need to define the priority. Some things that should be in the result model:

* Visit metadata

  + Ship
  + Port
  + Terminal
  + Cargo type
* Timestamps: EOSP, NOR, all lines secured, pilot on board?, those kind of things
* Delays

  + Start/end of delay
  + Reason of delay (categories need to be defined for this)
* Maybe more details of when NOR was tendered (can be done multiple times)
* Code version/commit id used for running the job
* Time when job was run, duration

#### Implement upload & job creation (1d)

Implement the endpoint where one or multiple PDFs can be uploaded to create a job. An id is generated for the job and returned to the caller. The PDFs are stored in an S3 bucket, and the job status etc is stored in the database.

### Sprint 2

#### Job runner (5d)

Implement the actual job runner infrastructure. The design must be scalable in the sense that we want to start with a single runner and be able to scale this up to multiple runners to have concurrency. The first step could be to extract some metadata from the PDF and store that as job result, just to get the basic flow up and running.

Communication between the API and the runner will be done using NATS, using a queue with multiple consumers. The API posts the job to the queue, and NATS will ensure that it is delivered to one of the runners. We need to investigate if it is possible to have a long duration between picking up the job and acknowledging it (we might need multiple minutes for OCR and parsing). The job result is posted back to the API via NATS, and the API will store the result in the database.

#### Job runner integration test (3d)

Setup an integration test framework for the job runner code, to ensure that no regressions develop. It should consist of several sets of PDFs/jobs + their expected result data. We also want to have some tests for the non-happy flow (job failure etc).

#### Job status & mgmt endpoint (1d)

Implement various job status and management endpoints:

* retrieve job status based on id
* restart job (when not running)
* cancel job (when not started yet)
* list jobs (running, completed)

### Sprint 3

#### Textract connection (3-5d?)

Add the Textract connection to the API. The API calls AWS Textract to start the OCR process, Textract reads the PDF from a specified S3 bucket. The API listens on SQS for the Textract response, and updates the job status accordingly. The job result is stored in either S3 or Mongo (depending on the size). Ensure that if a job is restarted that the results are not overwritten, but a new version of the results is stored.

#### Result extraction

Add functionality to the job runner to extract data from the Textract result. The API starts this process by posting a message to a NATS queue group, the runner(s) listen in this queue group. Things to extract:

* Location/port. This is a must-have to determine the local time zone
* Vessel name and/or IMO number
* SOF timestamp keywords

### Sprint 4

#### Tuning and tweaking

Improve things.

#### Cross-validation

Using various other data sources, we can cross-validate and increase/decrease the confidence of the data that we have extracted:

* If we have both an IMO number and a vessel name, check that they match in CSI
* Check if the vessel has a visit at the correct time at the correct port in VesselVoyage

If the cross-validation fails, the document should probably be flagged for manual intervention.

### Optional next sprints

#### Explore and setup training for PaddleOCR

Invest time to explore what we need to train a customised model for PaddleOCR tailored to extract data out of SOF PDFs, to see how feasible it is to create a better model. We can leverage the data we have collected (and validated, hopefully!) from Textract to see if we can train PaddleOCR to be as good or better as Textract is.

#### Delay extraction

Extract delay information: duration, reasons

#### Data sources

Add source of the data to the request and also add it in the response/result. The caller should decide whether it is acceptable to use the data.