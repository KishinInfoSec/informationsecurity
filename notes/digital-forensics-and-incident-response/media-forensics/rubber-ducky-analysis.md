---
title: rubber-ducky-analysis
tags: [digital-forensics-and-incident-response, media-forensics, type/reference, phase/forensics]
---

# Rubber Ducky Analysis

## Theory

### What is a USB Rubber Ducky

A Rubber Ducky Attack is a cyberattack in which a custom USB device emulates a USB keyboard to attack a workstation. When plugged in, the device immediately begins to imitate a user "typing" a particular set of keystrokes—usually commands or keystrokes designed to perform illicit activity on the target system.

    ../      (8).png" alt=""><figcaption><p>Source: www.sciencedirect.com</p></figcaption></figure>

***

## Practical

### Analyzing .bin file

A bin file in a USB Rubber Ducky is the binary equivalent of the DuckyScript source code. The compiler and encoder generate the bin file, which is made up of byte code that the USB Rubber Ducky interprets. The bin file is the payload that runs when the device is plugged into a computer.

### Decoding the .bin file

#### Duck-Decoder

```
python2 DuckDecoder.py <display | decode> /path/to/inject.bin
```

    ../      (9).png" alt=""><figcaption><p>Decoded outout of bin file</p></figcaption></figure>

#### Ducktoolkit

```
# Install
sudo pip install --upgrade ducktoolkit

# Decode
ducktools.py -d -l gb /path/to/inject.bin /path/to/output.txt
```

#### Extra Knowledge

**NOTE:** To create a bin file, you can write a text file in DuckyScript, which is a scripting language. Then, DuckEncode, a cross-platform executable JAR file, compiles the text file into the inject.bin. You can place the inject.bin in the same directory as the DuckEncode,jar file. Next, you can drop any DuckyScript file onto the batch file, and it will emit inject.bin from the script. You can then move the inject.bin onto the device.\
\
You can encode Ducky Script using the Java command line encoder, or the JS Ducky Encoder. There are also online encoders that can convert your ducky script to an inject.bin without installing any software.

***

## REFERENCES

* 
* 
* 
* 
* 
* 
