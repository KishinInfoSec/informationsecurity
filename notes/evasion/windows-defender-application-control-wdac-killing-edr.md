---
title: windows-defender-application-control-wdac-killing-edr
tags: [evasion, type/walkthrough, phase/evasion, platform/windows]
---

# Windows Defender Application Control (WDAC): Killing EDR

## Windows Evasion

Theory

Windows Defender Application Control (WDAC) was introduced with Windows 10 and allows organizations to control which drivers and applications are allowed to run on their Windows clients. It was designed as a security feature under the servicing criteria, defined by the Microsoft Security Response Center (MSRC).

**EDR drivers or binaries can therefore be blocked using a WDAC policy.**

In order to bypass EDR products using the following method, a reboot is required, which is a bad OPSEC operation.

### Practice <a href="#practice" id="practice"></a>

{% hint style="success" %}
In order to set up a Windows Defender Application Control (WDAC) policy that can tamper with a targeted EDR, follow this guide:
   
## Locally

#### 1. Setup Your Environement <a href="#id-1.-setup-your-environement" id="id-1.-setup-your-environement"></a>

On a fresh installed Windows Virtual machine, we will install:

* Dotnet 8 SDK
* WDAC Wizzard
* The targetted EDR Agent

#### 2. Create a WDAC Policy <a href="#id-2.-create-a-wdac-policy" id="id-2.-create-a-wdac-policy"></a>

When all setup, we can start creating an EDR-Blocking WDAC Policy using the WDAC Wizzard utility:

1. Select "Policy Editor"

     alt=""><figcaption></figcaption></figure>

1. Select the "AllowAll" template from `C:\Windows\Schemas\CodeIntgrity\ExamplePolicies\AllowAll.xml` and click "Next"

     alt=""><figcaption></figcaption></figure>

1. Ensure that "Audit Mode" is Unchecked, click "Next"

     alt=""><figcaption></figcaption></figure>

1. Click "Add Custom"

     alt=""><figcaption></figcaption></figure>

1. Specify conditions on the targeted EDR Publisher, executable/drivers hashes, Product Name, or even Paths.

For this technique to be effective in tampering with EDR functions, it is essential to identify and select both user-land processes (e.g., PE/exe files) and drivers (e.g., sys files) that are necessary for the EDR's to properly work.

However, avoid blocking entire EDR related drivers and processes, as this may lead to system crashes or blue screens. Instead, **focus on blocking the minimal components, necessary to interfere with the essential functions of the EDR.**

     alt=""><figcaption></figcaption></figure>

1. When done, wait for the WDAC Policy to build. It will create an XML and PolicyBinary file.

     alt=""><figcaption></figcaption></figure>

#### 3. Apply the WDAC Policy <a href="#id-3.-apply-the-wdac-policy" id="id-3.-apply-the-wdac-policy"></a>

We can now upload the previously build PolicyBinary file to a target host, and apply it using below command lines:

Copy

```powershell
# Windows 11 22H2 and above
CiTool --update-policy C:\Path\To\{Policy}.cip

# Windows 11, Windows 10 version 1903 and above, 
# And Windows Server 2022 and above
$PolicyBinary = "C:\Path\To\{Policy}.cip"
$DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
$RefreshPolicyTool = "<Path where RefreshPolicy.exe can be found from managed endpoints>"
Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
& $RefreshPolicyTool

# All other versions of Windows and Windows Server
$PolicyBinary = "C:\Path\To\{Policy}.cip"
$DestinationBinary = $env:windir+"\System32\CodeIntegrity\SiPolicy.p7b"
Copy-Item  -Path $PolicyBinary -Destination $DestinationBinary -Force
Invoke-CimMethod -Namespace root\Microsoft\Windows\CI -ClassName PS_UpdateAndCompareCIPolicy -MethodName Update -Arguments @{FilePath = $DestinationBinary}
```

     alt=""><figcaption></figcaption></figure>

#### 4. Reboot <a href="#id-4.-reboot" id="id-4.-reboot"></a>

After reboot, (and maybe several tests to identify which process/driver to block) the EDR should be now disabled.

***

## REFERENCES

* 
* 
