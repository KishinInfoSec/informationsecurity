---
title: lab-3-perform-footprinting-through-social-networking-sites
tags: [ceh, mindmaps, recon-and-information-gathering, type/lab, phase/recon]
---

# Lab 3: Perform Footprinting Through Social Networking Sites

## Task 1: Gather Employee's Information from LinkedIn using theHarvester

Use theHarvester tool to gather information about the employees (name and job title) of a target organization (eccouncil.org) available on LinkedIn. Enter the option to specify the data source as LinkedIn.

```
theHarvester -d eccouncil -l 200 -b linkedin
```

\-d: specifies domain name

\-l: specifies the number of results to be retrieved

\-b: specifies the data source as Linkedin

## Task 2: Gather Personal Information from Various Social Networking Sites using Sherlock

```
python3 sherlock.py satya nadella
```

## Task3: Gather Information using Followerwonk

Use the Followerwonk online tool ( to gather Twitter information about Satya Nadella. What is the name of rating Followerwonk uses to rate a user's influence and engagement on Twitter?

Social Authority
