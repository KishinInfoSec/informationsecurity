---
title: bhis-active-defense-offensive-countermeasures-and-cyber-deception
tags: [security-operations, active-defense, type/reference, phase/detection, source/bhis]
description: "John Strand 2-day course Active Defense, Offensive Countermeasures, and Cyber Deception: modules, deception techniques, tools and labs."
source_pdf: ACM_2DayJune_2026.pdf
---

# Active Defense, Offensive Countermeasures, and Cyber Deception (2-Day Course Notes)

Course-level map of John Strand's deck (with Bryce Galbraith and Paul Asadoorian), 218 slides, version 25_01, copyright 2026.
The vault splits the same deck into part 1 [[security-operations/active-defense/bhis-active-defense-foundations-and-threat-emulation]] (concepts, threat emulation), part 2 [[security-operations/active-defense/bhis-active-defense-annoyance-and-honeypots]] (honeypots, honeyports, tarpits) and part 3 [[security-operations/active-defense/bhis-active-defense-attribution-and-cyber-deception]] (legal issues, honeytokens, web bugs); this note is the whole-course outline with the speaker's framing kept where it is memorable.

## Course structure and lab VM guidance

- The course is deliberately different: "Most of the labs are not in the slides (because we like you :-))".
- Every VM-based lab lives inside the course VM within github, so you do not have to dig through hundreds of pages after class to figure out how something works.
- Prerecorded video walkthroughs of each lab are on the USB and embedded in Discord. "You're welcome! Enjoy! ;-)"
- It opens with AI: there is a misconception that AI will replace basic skills — "Context matters. Basics build context", and core fundamentals make using AI "cheaper".
- AI is in everything the course does now, but "it requires a system".
- Section flow as presented: introductions and standards → AI and deception → annoyance (tarpits, evil web servers, honeypots, honeyports, Portspoof, Cowrie) → attribution (legal issues, TOR, honeytokens, web bugs) → cyber deception on the cheap → attack extras → summary and capstone challenges.
- Opening lab, "Bad Guy Defenses": brainstorm what OSes attackers use and why, obfuscation techniques, persistence mechanisms, C2, and exfiltration. Framing: "Layers are not always awesome."
- Labs called out on slides (all instructions inside the class VM / ADHD VM):
  - Bad Guy Defenses; n8n
  - Advanced backdoors (~25 min): decode C2 from a Skillbit packet capture, then re-hunt with RITA / AC Hunter
  - HoneyUser; honeyport AutoDrop from the CLI (~60 min, solutions at the end — "But what is the fun in that?")
  - SpiderTrap (~15-20 min); Portspoof (~20 min); Cowrie (~20 min)
  - Web honeypot; Beelzebub; Canarytokens; HoneyShare

## Core definitions used throughout

- **Active defense:** "the employment of limited offensive action and counterattacks to deny a contested area or position to the enemy"; proactive, anticipatory and reactionary — "The adversaries are already inside your gates."
- **Passive defense:** measures taken to reduce the probability and minimize damage "without the intention of taking the initiative" — traditional static defenses ("hope for the best").
- **Prevent | Detect | Respond:** "Prevention is ideal, but detection is a must, and detection without response is of little value."
- **Offensive countermeasures:** offensive techniques employed as aggressors attack, but with a defensive posture.
- Aikido analogy: redirect and block opponents' attacks while taking considerable care not to harm them; "Aikido practitioners respond to attacks; they do not initiate attacks."
- **Poison, not venom:** poison is taken then consumed, venom is injected — "Lay traps inside your systems, but don't attack theirs."
- **Cyber deception:** the deliberate and calculated process of deceiving attackers to wage a better defense — "Slow them down, confuse them, deceive them … make them work harder."
- Goal: Detection time + Reaction time < Attack time (`Dt + Rt < At`); deception does not replace other layers, it complements and feeds them. "Militaries have employed deception strategies since the beginning of time. Why don't we?"
- **MITRE Engage** is the adversary-engagement framework the course maps to; disrupting the OODA loop is the strategic goal.

## Why deception: adversary reality and failing strategies

- "Make no mistake, APTs hunt administrators without mercy." Post-exploitation is adroitly executed under valid user context using normal OS features; entire teams are dedicated to attacking your organization.
- Adversary capabilities: 0-days, undisclosed exploits, advanced malware, backdoors, supply-chain infiltration, spies, coercion, lawfare; telecommunications infrastructure turned into a surveillance and attack platform; detection is bypassed before deployment.
- Nation-states have virtually unlimited resources (via taxpayers), direct access to your electrons, never-ending exploits, elaborate anonymization and C2, and practical immunity from prosecution.
- Good testing firms (BHIS, Layered Security, TrustedSec, SecureIdeas) are not thwarted by traditional defenses — they bypass them as a course of business; nation-states "run circles around most defenses".
- "Same things with Next-Gen AI in front" — the advice has been patch, strong passwords, anti-malware and firewalls for years; a next-gen AI firewall and next-gen AI anti-malware are still "reactionary by nature". "Do you see a pattern?"
- "You will be exploited" — expect it; anything less is denial. Zero-days, phishing/SE, advanced malware, supply-chain infiltration and government backdoors defeat most current security technologies.
- Getting compromised is acceptable because it is going to happen; unacceptable is an attacker persisting for months or pivoting from one system to the rest of the network in minutes.
- Recommendations: segment internal networks down to the desktop level and between subnets; consider an "infected" VLAN.
- Treat the internal network as hostile ("set your internal system firewalls at the same level they would be at a coffee shop"); block inbound with alerts, exceptions for admin networks; segment business units/OUs; private VLANs help; even the built-in Windows firewall works "if you are sadistic and desperate".
- Pass-the-Hash has worked since 1997; Pass-the-Ticket and Security Access Token (SAT) impersonation have worked for years — SAT impersonation, keyloggers and Mimikatz/Kiwi over normal domain protocols usually will not trip IDS alerts.
- Insiders: "If you cannot detect an insider, your network is not secure" (Snowden; attackers using valid credentials). Can you detect a user accessing 1000s of files or 100s of systems? Future attacks use far less malware; Word web bugs help get attribution.
- Threat emulation: think post-exploitation, not just missing patches — what happens after an attacker gains access. Free tools automate parts of it; the collected data is invaluable.
- Named emulation tools: Caldera, Atomic Red Team, Sigma-based detection, BloodHound, plus commercial offerings.
- Warning: "One of the traps of the MITRE framework" is training systems to detect specific attacks; most Atomic Red Team and MITRE entries are classes of attacks and vendors simply detect those — "A few modifications and you can easily bypass detection."
- Mindset shift: from "Can we be hacked?" to "What can we detect?" — "Start by finding gaps. Fill them. Move on. Start with the framework. This is ACTIVE."
- Advanced C2 lab conclusion: an IDS vendor could signature one Base64 string, but encryption and randomization bypass that; internet whitelisting is stronger but often not politically feasible. "This lab highlights just how hard it is to detect attackers when they are already in your network."

## AI, workflows, and orchestration

- Offensive AI is "fundamentally changing the game": attacks are not just faster, they are far more in-depth; API endpoints identified and fuzzed with scary accuracy.
- Internal post-exploitation is getting far faster — evolution through BloodHound and PingCastle; lateral movement "in just moments". Hence the need for deception.
- n8n example: automate alert enrichment pulling from Canarytokens, honeyports and full honeypots.
- Also with n8n: correlate data across multiple sources (doing this manually was time intensive), automate threat-hunting workflows, set thresholds and generate alerts.
- Use AI to assist analysts; pull all data to one point for a human; generate actionable reporting and response actions; tie it all together with ticketing systems.
- Think in workflows and cost, not "AI good/bad": can basic analysis run first and then be fed to AI? A feedback loop of refinement? Example: "have an agent run nmap, or have it code and build a port scanner".
- Core deception tools to parse data quickly and effectively: honeyports, Beelzebub, SpiderTrap, web honeypots; tie it all together with MCP servers and services like n8n.
- MCP vs orchestration: MCP servers expose capabilities, orchestration tools execute workflows; MCP is reactive, orchestration proactive; "They work best together, not instead of each other."
- Key difference is agency: MCP is a collection of tools at an AI agent's disposal; n8n-style orchestration interconnects tools as inputs and outputs.
- "Solving the problem AI on AI": more tools use AI to generate honey data dynamically, bypassing the whole honeypot-fingerprinting problem — "Only place where hallucinations are not just OK... They are fun!" Beelzebub is the named example for SSH, HTTP, Telnet and MCP servers.

## Annoyance: tarpits, evil web servers, scanner confusion

- PHPIDS plus a PHP tarpit rule can make attacking a website "interesting": first install PHPIDS, then create a rule that serves Mr. Clippy to detected attackers. "Is it a good idea to taunt attackers??" — the deck debates it.
- Time Machine: make your website look like something else by changing web server identity headers.
- **HoneyDNS:** what if your DNS server pointed to a large number of non-existent systems? Most attackers start by pulling records (zone transfer if possible); fill the zone with records pointing at unused IP address space, then log, alert, and possibly drop sources that request those systems.
- **Evil web servers:** testers and attackers use automated crawling to find pages and insertion points — maybe attack the tools back, possibly setting up a DoS condition on the automated scanner, or just set up rules that alert you.
- Caveat: "This is not something you want to do on an external webserver that you want to have crawled by Google. Configure robots.txt appropriately."
- **SpiderTrap:** infinitely recursive directory loops to stop web crawling activity; configure link-count and link-length ranges and the listen port; can be seeded with a DirBuster directory list to look more realistic.
- "Many testers use the Ron Popeil testing methodology — 'Set it and forget it!'": a `wget -m` mirror against the trap would lead to "a fun surprise when the testers come back".
- **Weblabyrinth:** Ben Jackson took SpiderTrap and extended it into a PHP script loadable in your web infrastructure; "gently tells Googlebot to go away".
- Weblabyrinth extras: random HTTP errors (404, 403, and 402 "Included just for the WTF Factor") to keep it "real", and a configured text string that triggers IDS alerts. "It is David Bowie approved."
- **Portspoof:** white noise and chaff in addition to tripwires — random responses to service identification requests; "the ports that get scanned never come back the same", so a simple service identification scan can take hours.

## Honeypots, honey users, honeyports, Cowrie

- A honeypot is "an object that is intended to be interacted with by an attacker, not legitimate users". "Honey all the things!" — honeytoken, honeyrecord, honeytable, honeypot, honeynet, honeycred, honeyport, honeydoc.
- Ideally it resembles something valuable to you or your organization; "Any interaction with the honeything is considered malicious and should be responded to immediately."
- Two views: research honeypots (a learning tool "much like having a hacker ant farm", but a time sink management often does not value) vs **production** honeypots — identifying malicious internal systems and users, attacks AV and IDS miss, and feeding incident-handling procedures.
- Honeypots answer "Detect and clear?" vs "Detect and learn?": they reveal attacker skill and motivation (dropping warez versus hunting "TOP SECRET" or credit card numbers) and what else they could reach.
- Why production: "Security through obscurity is this: No security at all" — clarified as the `Dt + Rt < At` goal; other technologies miss most post-exploitation activity and trusted insiders.
- **OpenCanary:** a great collection of Python scripts emulating many honey services (FTP, HTTP, SMB, SSH, Telnet, etc.); alerting via email, syslog and SMS is one of the more interesting aspects.
- **Honey users:** fake Domain Admin accounts, service accounts, plus emails for those accounts — "LinkedIn? Facebook? Yes!" Write SIEM rules so use of these accounts alerts. Lab: HoneyUser.
- **Honeyports:** ports that trigger an action when they are connected to — blacklist, alert, "Fire up Mr. Coffee". Done wrong they can blacklist legitimate systems, so "understand how connections work before you start implementing technical solutions."
- **Fail2Ban:** monitors authentication failures in `/var/log/auth.log` and blocks the offending IP past a threshold; covers anything that logs to auth.log (SSH, web services, Telnet) — "So easy to use, it should be installed on everything."
- CLI honeyport lab goal: build auto-drop scripts for Linux and Windows yourself, because "you might not have access/permission to use some of the tools we cover".
- Building blocks: iptables (`iptables -A INPUT -p tcp -s 172.16.30.42 -j DROP`; `-F` clears rules; `-L` lists them), bash loops/variables, netcat listener (`nc -nvl 8080`), `grep`, pipes, shell redirects (0 stdin, 1 stdout, 2 stderr), `/dev/null`, `awk`. "Standard Error (2) is very important." "Feel free to use AI... Just know what it is doing."
- Trigger behaviour: a plain SYN scan reports the honeyport open; a full connect scan (`nmap -sT`) completes the handshake, triggers the trap, and the DROP rule appears in `iptables -L`. A Windows variant chains netcat with a netsh advfirewall block rule ("Just... Don't do this."); there is also a PowerShell-Honeyport script.
- What honeyports buy you: visibility where IDS/IPS fail (attackers communicating over SMB, SSH, HTTP, HTTPS; effectively blind to 0-days), flexibility (CLI, Python, PowerShell, Ruby), and effectiveness for air-gapped/high-security networks.
- Enterprise caveats: may interfere with VA scanning (create exceptions, use authenticated scanning); an attacker blocking legit systems would need DoS, TCP sequence prediction and a full established connection — "Very hard to do with a live system." Simple, low interaction, little production impact.
- **Cowrie** (Kippo is the older ADHD3 version): "an outstanding SSH honeypot" letting the attacker interact with a fake SSH service, capturing logins, activity and "the passwords an attacker has, or at least what he thinks he has"; usable for both annoyance and attribution.
- Cowrie enterprise value: collected commands show intent — simple backdoor setup, specific files (targeted attack), or DDoS booter/spammer. Do they have valid user IDs and passwords? Users register work email on third-party sites (Io9, Adobe, LinkedIn, RockYou); if that site is compromised and passwords are synced, reaction changes.
- Cowrie lab: attack a partner's SSH honeypot, watch the logs, then reverse roles; you can change the default password.
- **Artillery** (TrustedSec, Dave Kennedy): honeyport plus file monitoring in one tool; automatically opens honeyports for widely used services (135/445 RPC/SMB, 1433 MSSQL, 5900 VNC) and can email alerts; the default port set is "very predictable" but modifiable, and setup across many servers is "a bit cumbersome".
- **Application-specific honeypots** mimic specific applications to blend in with existing servers in uniform environments (think SCADA), on the inside or outside the network — useful for proving to management that attacks happen.
- **Fingerprinting problem:** many honeypots are identified by predictable signatures that Nessus and Shodan pick up — "The trap may be set, but the attacker will go away." Change Conpot defaults (serial number, system name, system description) for greater OPSEC, per Darren Martyn's honeypot OPSEC research.
- **AI on AI:** LLM-generated honey responses sidestep fingerprinting entirely (Beelzebub); lab in the VM.

## Deployment OPSEC: "Not Getting Shot Is Important"

- You think you have a bad guy system to investigate — "Direct connections are a huge no-no!" and directly connecting can be highly dangerous.
- "Our recommendation is to not connect until you are sure you have what you need from an IR perspective." Do not set it up so it is attributable to you or your company — think drug dealers, mafia, Internet tough guys.
- Set up ADHD-style callbacks in a non-attributable fashion, preferably on a third-party hosting provider; "Do not set this up on your network (ever!)". All callbacks must come to a server/domain not related to your organization.
- Register through a name/e-mail that is not a real person — employees setting this up under personal email and name is "not good at all."
- Use a third-party anonymizing proxy for callbacks, email, domain registration and PayPal: Whonix (VMs) or TailsOS (live system) for TOR; VPN services are another option but may not be as anonymous.
- Non-attributable email: avoid Google/Microsoft; ProtonMail is "ok for privacy and anonymity" (free, zero-knowledge, Switzerland, custom domains). All other accounts register to it; use a very strong/long passphrase never reused anywhere.
- Burner phones confirm account details (some services require SMS activation); buy cheap phones anywhere or use the Burner app — "WARNING: Your phone can still be traced with a warrant."
- Paying for it: never a personal/corporate credit card; buy VISA/AMEX/Mastercard gift cards with cash (preferably in another state), $100-$500 covers a 2-6 month operation, tie them to PayPal. Providers that accept PayPal/pre-paid cards get rarer; be prepared to destroy the instance — "Don't get too emotionally attached to it."
- Architecture: honeydocs, HoneyBadger, Canarytokens, honeyports, SpiderTrap — "All deployed components should call back to your cloud-based hosted orchestration system."

## Attribution, legal issues, honeytokens

- Why attribution when nation-states are hard to catch: "One, know what they are after. Two, understand what they already have" — better defenses, better allocation. "Active defense provides threat intelligence."
- Indirection is key for attackers (TOR, botnets) — very few penetration testers do this; understand the difference between pentesters and nation-state hackers.
- TOR is not just for browsers: proxychains and SOCKS-5 can push Nmap, Nessus and Metasploit through it. Done right the good guys cannot see the real IP; done wrong "there is a good chance of finding out exactly who is attacking you."
- Packet captures in class contrast `-sP` and `-sS` scan artifacts; the right way through TOR is a full connect scan with no host discovery: `proxychains nmap -Pn -sT -p 80 209.20.73.195`.
- Case law and precedents discussed:
  - **U.S. v. Heckenkamp:** sysadmin counter-hacked a threatening student machine (temp/temp); the student's consent to university network terms justified the sysadmin.
  - **Susan v. Absolute:** a stolen laptop with tracking/spy software took embarrassing photos; Judge Rice: reporting an IP or geolocation "is something entirely different to violate federal wiretapping laws by intercepting the electronic communications". Settled out of court — "Just because they do something bad to you, it does not give you the right to violate their rights."
  - **1999 WTO DDoS:** hosting provider Conxion reflected the E-Hippies attack back through a mod_rewrite rule, disabling the attackers' site; not prosecuted (not the same as legal); logged 10,000 unique IPs.
  - **MSFT court order vs Waledac botnet (2010):** ex parte temporary restraining order suspended the botnet domains; Microsoft took "other technical measures" to degrade it.
- Warning banners carry a lot about permission; access-check technologies (OpenVPN scripts, Windows 2008 Network Access Protection) may double as a means to gather information about an attacker's system.
- Protecting IP is an accepted precedent for callbacks: software updates, license checks (Microsoft Genuine Advantage), phone tracking apps. "We are not necessarily talking about 'hacking' per se; we are talking about getting attribution or stuff we see every day."
- Hallmarks of legality: discuss, document, plan, consult with others, do not hide ("Hiding may be interpreted as what you think you are doing is 'wrong'"), "Don't be evil" — and remember ethics "is not always the same as legal"; "Don't become the people you're defending against."
- Reality check — how this goes wrong: mistakes or unintended consequences, easily accessible malware, full attacks of attacker IPs, crashing systems, persistent long-term access. It is about having options: annoyance, attribution, attack.
- **Canarytokens:** hosted option generates an MD5 string based on attacker/victim information and an iframe directing them to the site; recover results from the site, webhook them to your n8n orchestration server. Self-hosted: implement the APIs on your servers, custom DNS server, results database, embeddable Java and Flash applications.
- Make tokens real: referenced from `robots.txt`, cloned websites, wifi geolocation (`netsh wlan` details), Word docs on shares, compromised systems, websites and spam email. Lab: Canarytokens.
- **Word web bugs (honeydocs):** the feature is built into Core Impact ("kidnapping") — "However, we can do it free." Embed a stylesheet/image reference to your listener in an interesting document; when the doc is opened it pulls the URL — a direct connection with the opener's IP.
- No macros used ("excellent"), far less likely to crash a system, works for penetration testing and tracking intellectual property — "Not all ways of finding attribution need to result in shell access."
- Works in Microsoft Word, Apple TextEdit, LibreOffice Writer, AbiWord; Linux document processors need the ADHD web-bug server; can be extended to full macro scripts, which "would be far cooler for .xlsx files".
- Enterprise framing: "One of the key components of active defense is how psychology is key" — tactics are often 80%-90% thinking about what would entice an attacker. As an IR tactic, an attacker downloading a "sensitive" document gives you their IP for law investigations and threat intelligence, with no long-term persistent access: "From your intellectual property, which they stole."
- **HoneyBadger** (Tim Tomes): simple Java application that records geolocation of attackers — OS calls query nearby wireless access point details, then the Google Maps Geolocation API returns latitude/longitude.
- Three techniques, ranked: wireless access point detection (ideal), asking permission via JavaScript (not ideal), IP-based geolocation (easily spoofed via VPNs/anonymizers/TOR). Accuracy varies: "Sometimes it works flawlessly and is remarkably accurate. Other times? Well, not so much…" Location macros can be generated; "HoneyBadger Don't Care If They're Using TOR!" when wireless detection applies. "The trick is making them believe it is okay."
- Commercial cyber deception named: Javelin Networks, Cymmetria, Illusive Networks, Attivo Networks, TrapX, Acalvio.

## Deception on the cheap: AD honeyadmins, shares, recursion

- Goal: "Set up a set of cyber deception and attribution components in under half a day"; "Many ways to do the exact same thing"; quick and dirty — "Odd, these quick things usually get picked up the fastest."
- **Active Directory HoneyAdmin:** be obvious; disable logon hours; set up Kiwi as a "cheap SIEM"; test with a password spray; alerts fire on use.
- **HoneyShares and HoneyDocs** on file shares (lab in the VM).
- **Infinitely recursive Windows directories** ("Hasselhoff Recursion", thanks to Mark Baggett): `dir /S` continues forever — "The S is for Sub-Directories"; Meterpreter recursion continues until the victim system reboots, even if the attacker's session is terminated.
- Effect: possibly slow down exfiltration, but "It can also crash some services — possibly backups. Be careful."
- AD deception pointers: Deploy-Deception (github.com/samratashok/Deploy-Deception) and "Lab of a Penetration Tester: Forging Trusts for Deception in Active Directory".

## Attack-side extras

- `exe2vba.rb` (in the tools directory of Metasploit) converts any .exe into VBA so it can be imported into Word and Excel: `./exe2vba.rb notevil.exe notevil.vba` — "Now you can test your standalone .exe files."
- Closing slides: "No... Seriously... Vuln Software is Everywhere", "Just Two Weeks at a Bank", "Taking Over a Botnet", then the summary and Capstone Challenges.

## Key takeaways

- Restated at the end: active vs passive defense; prevention ideal, detection mandatory, response required; poison not venom; "Always ensure solid legal footing — proper authorization, warrant, written approval, etc."
- "It's about changing the game… It's about actively engaging the enemy… It's about disrupting their OODA loop… It's about affecting the (Dt + Rt < At) equation…"
- "It's about getting away from the easy button… It's about getting away from plug-and-play security solutions… It's about embracing the fact that advanced adversaries aren't afraid of consoles and executive dashboards… It's about getting into the fight!"

## Tools mentioned

| Tool / project | Role in the deck |
|---|---|
| MITRE Engage | adversary-engagement framework the course maps to |
| Caldera, Atomic Red Team, Sigma, BloodHound | threat emulation and detection testing (vendor-bypass caveat) |
| RITA / AC Hunter | beaconing detection in the advanced C2 lab |
| n8n, MCP servers | alert enrichment, correlation, workflow orchestration |
| PHPIDS, PHP tarpit | detect attack traffic; serve Mr. Clippy |
| HoneyDNS, evil web servers, SpiderTrap, Weblabyrinth, Portspoof | scanner/crawler confusion and tarpits |
| OpenCanary, Cowrie/Kippo, Artillery, Conpot, Beelzebub | honeypots (emulation, SSH, service, ICS, AI-generated) |
| Fail2Ban | authentication-failure blocking |
| CLI/PowerShell honeyports | connect-triggered alert or blocklist |
| Canarytokens, Word web bugs, HoneyBadger | attribution callbacks and geolocation |
| Deploy-Deception | Active Directory deception, forged trusts |
| Whonix, TailsOS, ProtonMail, burner phones, gift cards | non-attributable operations infrastructure |
| ADHD course VM, Skillbit | lab platforms; most labs live inside the VM |

## Defender/Attacker takeaways

- Defender: assume breach, segment to the desktop, firewall internally like a coffee shop, and shift budget from prevention theatre to measurable detection.
- Defender: instrument deception where attackers must touch it (accounts, documents, shares, ports, DNS), route every callback to one orchestrated place, and alert on any honeything interaction.
- Defender: keep the legal checklist — discuss, document, plan, consult, warrant, banners, do not hide — and run decoy infrastructure non-attributably.
- Attacker view: the deck frames every honeything as poison — something you must take or touch (document, web page, honeyport, honeypot), and a callback from it is a direct connection. Crawlers and service scanners are the tools most exposed to tarpits, recursive link loops and randomized banners.

## Source

BHIS/Antisyphon "Active Defense, Offensive Countermeasures, and Cyber Deception", John Strand with Bryce Galbraith and Paul Asadoorian, `Resources/BHIS/ACM_2DayJune_2026.pdf`, 218-slide deck, version 25_01, copyright 2026.
Whole deck condensed here; the part notes cover slides 1-81, 82-134 and the attribution/legal material in depth.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/attribution]]
- [[reconnaissance/active-recon/stealth-scanning-strategies]]
- [[social-engineering/insider-attack]]
