---
title: fuzzing-chrome-v8-engine
tags: [reconnaissance, active-recon, fuzzing, type/tool]
---

# Fuzzing Chrome V8 Engine

## Introduction to Fuzzilli

A (coverage-)guided fuzzer for dynamic language interpreters based on a custom intermediate language ("FuzzIL") which can be mutated and translated to JavaScript.

## Usage

1. Download the source code for one of the supported JavaScript engines. See the Targets/ directory for the list of supported JavaScript engines.
2. Apply the corresponding patches from the target's directory. Also see the README.md in that directory.
3. Compile the engine with coverage instrumentation (requires clang >= 4.0) as described in the README.
4. Compile the fuzzer: `swift build [-c release]`.
5. Run the fuzzer: `swift run [-c release] FuzzilliCli --profile=<profile> [other cli options] /path/to/jsshell`. See also `swift run FuzzilliCli --help`.

## Read More Here

## Other Fuzzer

* FreeDom: 

***

## REFERENCES

* 
* 
* 
* 
* 
* 
* 
* 
