---
title: a06-2021-vulnerable-and-outdated-components
tags: [owasp-top-10, web, type/reference]
---

# A06:2021 – Vulnerable and Outdated Components

## Vulnerable and Outdated Components

Using vulnerable and outdated components can introduce significant security risks to your application. It's crucial to actively manage and update all components, including libraries, frameworks, and dependencies, to mitigate these risks effectively.

## Characteristics of Vulnerable and Outdated Components

1.  **Lack of Version Awareness**

    * **Description**: Not knowing the versions of all components used in the application, including nested dependencies.
    * **Example**: Using third-party libraries without tracking their versions.
    * **Impact**: Vulnerabilities in outdated components remain unaddressed, posing a security risk to the application.

2.  **Use of Vulnerable or Unsupported Software**

    * **Description**: Using software that is vulnerable, unsupported, or out of date, including the OS, web/application server, database management system (DBMS), and libraries.
    * **Example**: Running a web server with an outdated version known to have security vulnerabilities.
    * **Impact**: Attackers can exploit known vulnerabilities to compromise the application or its underlying infrastructure.

3.  **Lack of Vulnerability Scanning and Security Bulletin Subscriptions**

    * **Description**: Failing to regularly scan for vulnerabilities and subscribe to security bulletins related to the components used.
    * **Example**: Neglecting to monitor for security updates and patches for third-party libraries.
    * **Impact**: New vulnerabilities may go undetected, leaving the application exposed to potential exploits.

4.  **Delay in Patching and Upgrading**

    * **Description**: Not promptly fixing or upgrading the underlying platform, frameworks, and dependencies in response to security advisories.
    * **Example**: Delaying patching of known vulnerabilities due to infrequent patching schedules.
    * **Impact**: Prolonged exposure to known vulnerabilities increases the risk of exploitation and compromise.

5.  **Lack of Compatibility Testing**

    * **Description**: Failing to test the compatibility of updated, upgraded, or patched libraries with the application.
    * **Example**: Updating a library without verifying its compatibility with existing code.
    * **Impact**: Compatibility issues may arise, leading to application downtime or unexpected behavior.

6. **Inadequate Component Configuration Security**
   * **Description**: Not securing the configurations of components used in the application.
   * **Example**: Using default configurations for third-party libraries without customizing them.
   * **Impact**: Default configurations may expose the application to unnecessary risks or vulnerabilities.

## Prevention Strategies

*   **Implement Patch Management Process**

    * Establish a patch management process to remove unused dependencies, features, components, files, and documentation.

*   **Continuous Version Inventory**

    * Utilize tools like OWASP Dependency Check and retire.js to continuously inventory versions of client-side and server-side components and their dependencies.
    * Monitor sources such as Common Vulnerabilities and Exposures (CVE) and National Vulnerability Database (NVD) for vulnerabilities.
    * Automate version monitoring using software composition analysis tools.
    * Subscribe to email alerts for security vulnerabilities related to used components.

*   **Obtain Components from Official Sources**

    * Obtain components only from official sources via secure links.
    * Prefer signed packages to mitigate the risk of including modified or malicious components.

* **Monitor for Unmaintained Components**
  * Monitor for libraries and components that are unmaintained or do not provide security patches for older versions.
  * Consider deploying virtual patches to monitor, detect, or protect against discovered issues when patching is not feasible.

***

## REFERENCES

* OWASP Application Security Verification Standard: V1 Architecture, design and threat modelling
* OWASP Dependency Check (for Java and .NET libraries)
* OWASP Testing Guide - Map Application Architecture (OTG-INFO-010)
* OWASP Virtual Patching Best Practices
* The Unfortunate Reality of Insecure Libraries
* MITRE Common Vulnerabilities and Exposures (CVE) search
* National Vulnerability Database (NVD)
* Retire.js for detecting known vulnerable JavaScript libraries
* GitHub Advisory Database
* Ruby Libraries Security Advisory Database and Tools
* [SAFECode Software Integrity Controls \[PDF\]](
* 

## Mapped CWEs

*   **CWE-937: OWASP Top Ten 2017 Category A9 - Using Components with Known Vulnerabilities**

    * **Description**: The application uses components with known vulnerabilities.
    * **Link**: 

*   **CWE-494: Download of Code Without Integrity Check**

    * **Description**: The application downloads code from an external source without verifying its integrity.
    * **Link**: 

*   **CWE-840: Business Logic Errors**

    * **Description**: Errors in the application's business logic can lead to security vulnerabilities.
    * **Link**: 

* **CWE-829: Inclusion of Functionality from Untrusted Control Sphere**
  * **Description**: The application includes functionality from an untrusted control sphere.
  * **Link**: 
