---
title: reverse-engineer-an-api-using-mitmweb-and-postman
tags: [api-testing, reverse-engineering, type/walkthrough, phase/recon, platform/api]
---

# Reverse Engineer an API using MITMWEB and POSTMAN

## Reverse Engineer an API using MITMWEB and POSTMAN and create a Swagger file (crAPI)

Many times when we try to Pentest an API we might not get access to the Swagger file or the documentation of the API, Today we will try to create a swagger file using Mitmweb and Postman.

First we will run mitmweb through our command line in Kali

**# mitmweb**

     alt="" height="171" width="629"><figcaption><p>Running MITMWEB</p></figcaption></figure>

and as we can see it starts to listen on the port 8080 for http/https traffic, and we will make sure that it's running by navigating to the above address which is the localhost at port 8081 and we will be greeted with something like this:

     alt="" height="211" width="700"><figcaption><p>MITMproxy is running</p></figcaption></figure>

and then we will proxy our traffic through Burp Suite proxy port 8080 because we already has mitmweb listening for this port (make sure Burp is closed)

     alt="" height="247" width="700"><figcaption><p>making the proxy port ready in the browser</p></figcaption></figure>

after this we will navigate crAPI and perform various actions like registering a user, login to the web site, forgetting password, going through different tabs, etc.

     alt="" height="421" width="700"><figcaption><p>Navigating crAPI</p></figcaption></figure>

and we can see that mitmweb is capturing the traffic

     alt="" height="427" width="651"><figcaption><p>MITMWEB is getting requests and capturing traffic</p></figcaption></figure>

and then we will check the 8081 port on the web server and find it filled with data

     alt="" height="591" width="700"><figcaption><p>Getting Flows through mitmweb</p></figcaption></figure>

then from File tab we will save the traffic flow that we captured

     alt="" height="627" width="700"><figcaption><p>Saving the traffic captured</p></figcaption></figure>

and then we will stop the capture and use mitmproxy2swagger to analyse it

`# sudo mitmproxy2swagger -i ./Downloads/flows -o spec.yml -p` ` `-f flow`

what we did here is that we used the flow file for making the swagger and then limited the results from the flow file to only be for crAPI.

     alt="" height="129" width="645"><figcaption><p>Analysing Captured file using mitmproxy2swagger</p></figcaption></figure>

after it finishes we will look at it with text editor and see what is there :

     alt="" height="519" width="651"><figcaption><p>spec.yml file after it finishes</p></figcaption></figure>

from here we will remove ignore from the files that contain APIs

     alt="" height="281" width="636"><figcaption><p>removing ignore from the APIs</p></figcaption></figure>

and we will run the previous command one more time to make a swagger file with examples:

`# sudo mitmproxy2swagger -i ./Downloads/flows -o spec.yml -p` ` `-f flow --examples`

     alt="" height="128" width="639"><figcaption><p>rerunning the mitmproxy2swagger</p></figcaption></figure>

from here we will go to swagger editor to visualize our file and we will upload it

Swagger EditorEdit descriptioneditor.swagger.io

     alt="" height="277" width="700"><figcaption><p>uploading our file to Editor.swagger.io</p></figcaption></figure>

and then we can analyse it and go through it more and try to get an idea about the API construction and structure.

     alt="" height="669" width="700"><figcaption><p>Analysing the API using Editor.swagger.io</p></figcaption></figure>

as we can see we make some sort of API documentation.\
from here we will go to Postman and import the .yml file to create a collection from what we did.

\# **postman**

and inside Postman we will import the yml file

     alt="" height="594" width="700"><figcaption><p>Importing API file</p></figcaption></figure>

and now we can see it in the API tab and see the structure better and we can start playing with the requests from postman.

     alt="" height="422" width="700"><figcaption><p>API Reverse Engineering</p></figcaption></figure>

And we can dig deeper into it

     alt="" height="332" width="700"><figcaption><p>this is the request for changing Email example</p></figcaption></figure>

As we can see mitmweb and Postman are powerful tools to see how the API is constructed and layout if you don’t have proper documentation or its a legacy API and you don’t actually know how it works and it can be useful as well for those who are doing Black Box pentesting.

***

## REFERENCES

* 
