# AWS Cloud Practitioner Notes
## Exam Date: August 12 2026
## Goal: Pass CLF-C02

---
Day 1 (00:00 - 40:00)
---------------------
Cloud Computing?
the practice of using a network of remote servers to store, manage and process data, rather than using a local server or personal computer.

On-Premise:
You own the servers, You own/rent the real estate, you hire the IT people, you take all the risk

Cloud Providers:
They own the servers, they own/rent the real estate, they hire the IT people, You are responsible for configuring cloud services and code, and they take care of the rest. 
----------------
The Evolution of Cloud Hosting?

Dedicated Server:
One physical machine used by a single business, to run a single web app/site (very expensive, high maintenence, high security)

Virtual Private Server (VPS):
One physical machine dedicated to a single business. The physical machine is virtualized into sub-machines, used to run multiple web apps/sites. (Better Utilization and Isolation of Resources)

Shared Hosting:
One physical Machine shared by hundreds of businesses, Relies on most tenants under-utilizing their resources. (Very Cheap, poor isolation, Limited functionality)

Cloud Hosting:
Multiple Physical Machines that act as one system.
the system is abstracted into cloud services.
(Flexible, Scalable, Secure, Cost Efficient, High Configurability)
----------------
What is Amazon Web Services (AWS)?

Simple Queue Service (SQS) was the first AWS service launched for public use. Imagine if 10,000 people press 'Buy Now' at the exact same second. SQS holds the 10,000 purchase requets safely in a queue so your payment processing system can handle them smoothly without dropping a single order.

Simple Storage Service (S3) a massive, highly secure bucket to dump files into and retrieve them whenever you want

Elastic Compute Cloud (EC2) Your virtual computer in the cloud. You can choose the exact specs you want your virtual computer to have and can be upgraded whenever neeeded 
----------------
What is a Cloud Service Provider (CSP)?
A CSP is a massive tech utility company that rents out hundreds of digital services that seamlessly connect togehter under a single managment system (instead of buying physical components to build the infrastructure which will be very costly and need real estate to house the components a company can simply rent out exactly what they need and only pay for the exact seconds or hours they use it for).

Metered Billing/Pay-as-you-go: Paying only for what you consumed (per second/per hour)

Unified API: A single standard language/interface used to control all digitial services

Chained Together: Services are designed to connect into one another like building blocks.

Cloud Platform vs CSP: If a company offers digital services but lack things like a unified API, metered billing, or an IaaS offering (virtual machine rentals), its considered just a Cloud Platform, Not a full CSP
-------------
Landscapes of CSP?

Public Cloud: Services that are offered to the general public over the public internet by third party providers such as (AWS, Microsoft Azure, Google Cloud Platform).

Private Cloud: Cloud infrastructure operated soley for a single organization, typically hosted in their own on-premises data centers.

Hybrid Cloud: Combining an on-premises private data center with public cloud resources (e.g. running legacy apps on physcial hardware while running new apps on AWS)

Multi-Cloud: Using multiple public cloud providers at the same time (e.g. using AWS for compute and Google Cloud for machine learning) to avoid vender lock in.
---------------
Day 2 (40:00 - 1:35:00)
---------------
Common Cloud Services (the 4 core)?

AWS groups its 200+ services into logical categories, but almost everything rests on the 4 core building blocks of basic physical infrastructure: Compute, Storage, Networking and Databases. 

Compute: Virtual Processing power to run code and apps. (AWS Example: EC2 - Virtual Machines)

EC2 - is a AWS service which allows clients to rent a virtual machine. Like my ubuntu laptop but running in amazon's data center instead of my desk

Storage: Virtual hard drives to save flat files, objects, or volume blocks (AWS Example: EBS - Virtual Hard Drives)

EBS - is a virtual hard drive that is attached to a single virtual machine

S3 - is object storage accessible through the internet to store files, images, backups etc. 

Networking: Digital wires, routers, and firewalls to isolate or connect resources. (AWS Example: VPC - Private Cloud Network)

Databases: Structured systems built specifically for rapid data querying, reporting, or web app storage. (AWS Example: RDS - SQL Databases)

"Cloud Computing": The exam is expecting you to know this term refers to the entire ecosystem of categories combined, rather than just the "Compute" piece.
----------------
The Evolution of Computing?

Dedicated On-Premises Server:
A dedicated server is a physical machine inside a traditional data center that is completely restricted to one single company.

Cons of Dedicated On-Premises Server:

Guessing Capacity: You must guess how much traffic your apps will get ahead of time and buy physical hardware to match it.

Underutilized Server/Wasted Space: Buying a massive machine for your busiest day of the year means it sits mostly idle (wastes space) on normal days.

Manual Migration: Upgrading or scaling a dedicated server requires manual work. As well as the migration downtime will also underutilize the server.

AWS Equivalent: For companies moving to the cloud who still require dedicated physical hardware due to strict legal rules. AWS offers EC2 Dedicated Hosts and Dedicated Instances.
---
Virtual Machines (VMs) & Containers:

This phase of computing solved the "Wasted Space" problem by using a piece of software called a 'Hypervisor' to slice one physical server into multiple isolated virtual computers (VMs), which can then run tightly packaged micro-apps called Containers. 

Hypervisor: the core software layer which creates, runs and manages Virtual Machines on top of physical hardware

Virtual Machines: Is an Amazon EC2. its a full complete virtual computer with its own Operating System. (windows or linux)

Guest OS: The operating system running inside a specific VM (you can have a Linux Guest OS and a Windows Guest OS running on the exact same physical machine) 

Containers/Docker: These are even smaller and faster than Virtual Machines. They are very lightweight and hold he bare minimum code to run an app which can be run in milliseconds. On AWS you run these on Amazon ECS.

Docker Daemon: this is the background software that packs, launches and runs containers. it is the engine that makes containers run.
---
Serverless Computer/Functions: AWS handles the hassle of configuring, packing and managing the virtual servers and Operating Systems for you. it handles the whole infrastructure automatically. (AWS Lambda)

AWS Lambda: This is the absolute ultimate textbook example of a Serverless "Function" service.  

Pay-for-use Pricing: With serverless (Lambda), you only pay for the milliseconds that someone uses your app, so if no one runs your app you pay 0$.

Cold Starts: The Serverless system automatically shuts down when not in use to save you money. So when someone randomly requests to use your app after a long break, it may take a second or 2 to wake up and load, this is called a "Cold Start"

-----------------------
Types of Cloud Computing (The Big 3)?

IaaS (Infrastructure as a Service): You rent the raw building blocks - like the virtual computers, hard drives, and networking. You have total control, but you have to manage the operating system and install everything. (e.g. Amazon EC2, Amazon VPC, Amazon EBS)

PaaS (Platform as a Service): For developers. AWS handles the operating system, hardware, and server setups automatically. You only care about writing and uploading your application code. (e.g. AWS Elasic Beanstalk)

SaaS (Software as a Service): A completely finished, ready-to-use product made for everyday customers. You don't manage code, servers, or systems. It just works. (e.g. Gmail, Office 365, Salesforce)

----------------------
Different Cloud Deployment Models?

Public Cloud: Everything is built on a CSP (Cloud Service Provider) like AWS. You have zero physical hardware on your own, This is also called "Cloud-Native" or "Cloud First"

Private Cloud: Everything is built inside your own company-owned data center. It is completely locked down just for your business. This is also known as "On-Premise". A common software tool that is used to build a private cloud is OpenStack. 

Hybrid Cloud: You use a mix of both your own On-Premise data center and a Public Cloud provider (like AWS). They are usually connected together securely using something like a VPN.

Cross-Cloud (Multi-Cloud): You use multiple different public cloud providers at the same time (e.g., using AWS and Google Cloud and Microsoft Azure Together)

----------------------
IAM (Identity and Access Management) is used to assign certain groups permissions on the cloud.

AWS Region Selector: is crucial when using AWS becuase sometimes certain services on AWS require you to set a specific region to grant you permission for you to use it.

AWS budgets: is used to set a monthly or daily budget on specific services or total cost to prevent you from over spending.

AWS Free Tier: is a feature AWS posesses which notifies users if a specific service they want to use is on a Free Trail to use before you start paying or any AWS service that AWS service publishes to give the user the freedom of usage before purchase.

Billing Alarms: is amn alert sent to you email to notify you if a certain service or total spending is more than the set amount or over the norm boundary. To allow you to investigate and stop certain services without alarming you suddenly. (CloudWatch).

MFA (Multi-Factor Authentication): Usually Recommended to set on root users when using AWS for an extra layer of protection and security. A main example is Authy, A mobile application that scans a qr code displayed, for an extra layer of confirmation before granting access to the log in page.
----------------------
Innovation waves

Kondratiev waves: is the technology lifecycle like phenomany which irreversible changes the society on a global scale, a common pattern of a wave is the change of supply an demand. 

when theres an increase of the kondratiev wave it suggets an expansion, if it reaches to the top and flattens out it means that was the boom, if starts dropping it suggests a recession, and if the drop flattens out it suggests a depression.
----------------------
Burning Platform? 

Burning platform is a term used when a company abandons old technology to new technology with the common drive for uncertain success and can also be influenced by fear. The future of an organization is risked on its digital transformation.
----------------------
Evolution of Computing Power?

General Computing (CPU): on AWS you access this by using the standard Amazon EC2 instances.

GPU Computing : Originally built for gaming, and they are 50x faster than traditional CPUs. It powers the AI, ML and deep learning models. AWS has custom hardware options for this such as, AWS inferentia (lnf1) chips.

Quantum Computing: 100 million times faster than standard computers. On AWS, the dedicated service for this is called Amazon Braket (Bracket with a 'k')
----------------------
The Benefits of Cloud (7)

Cost-efficient: You pay for what you consume, no upfront cost. The Pay-as-you-go with thousands of users share the cost of the resources.

Gobal: You can use it any where in the world, Just choose a region.

Secure: Cloud providers take care of the security work. Cloud services are also secure by default.

Reliable: Data backups, disaster recovery, data replication, and fault tolerance

Scalable: Increase or decrease resources or services on demand. 

Elastic: Automate scaling during spikes and drop on demand (it scales by itself if it sees the demand increases and scales down if it sees the demand decreasing)

Current: The hardware and software is patched, managed, upgraded and replaced by the cloud providers without interupting you.
-------------------
AWS Global Infrastructure

What is the AWS Global Infrastructure?
is globally distributed hardware and data centers that are physically networked together to act as one large resource for the end customer.

Regions in AWS Global Infrastructure?
Regions are geographically distinct locations.
Every region is physically isolated and independent from every other region in terms of location, power and water supply.

New services on AWS become available first on US-EAST

All billing info appears in US-EAST-1

the cost of AWS Services very per region.

Questions before you select a region:

What Regulatory Compliance does this region meet? (Laws)

What is the COST of Servies in this region?(Cost)

What AWS Services are available in this region?(Availability)

What is the distance or latency to my end-user?(Time)
--------------------
Regional vs Global Services?

Regional Services: 
The AWS Management Console limits the user to a specific region when using certain AWS Services, and when a user switches their region certain resources may disappear, because you are now looking at a different data center zone.

Global Services:
These services are allowed across all physical regions. When you open a console page it will automatically locks the display as the region 'Global' which means that it is accessible in any region.

The Big 4 GLOBAL Services to Memorize:

IAM (Identity and Access Management): Managing users, passwords, and permissions across the whole account. Global

Amazon Route 53: AWS's global DNS service that routes web traffic worldwide.

Amazon CloudFront: A global Content Delivery Network (CDN) that caches data closer to users using a group of regions. (help with latency)

Amazon S3 (Simple Storage Service): S3 is global as a service but when creating a single storage container it turns to a S3 Bucket which causes you to explicitly select a single region for where that data physically sits.

-------------------------
Day 3 (1:35:00 - 1:55:00)
-------------------------
AWS Global infrastructure - Availability Zones (AZs)

Availability Zone? An availability zone is a physical locaiton made up of one or more data centers inside an AWS Region.

How many AZs Per Region? A region generally contains 3 AZs. US-EAST-1 has the most (6 AZs)

Physical Isolation and Connection? AZs are meant to be physically isolated so if there were to be a flood or power outage, other AZs in that region wont be afftected taking down the whol region. They are also located 100km of one and other.

They are connected with ultra-fast, high-bandwidth, low-latency (<10ms) metro fibre optic cables while also habing all traffic being encrypted.

High Availabilty: Standard practive to deploy workloads accross atleast 3 AZs so your application stays even if one or two data centers fail completely.

When launching a EC2 (virtual machine) you dont pick the availabilty zones rather you pick a subnet which is directly mapped to a specific availabilty zone.
------------------------
Fault Tolerance and Failure Zones

A fault domain (or failure zone) is a ring0fenced boundrary designed if something were to break inside it, it wont have a cascade affect outside that domain. AWS adopts this concept at every layer so if a fire or a power outage were to happen in one spot it wont bring down your whole app.

Fault domain: A section of a network that is vulnrable to damage if a system fails. Its used to create a ring-fenced boundery to protect every layer from spilling over. 

An Availabilty Zone acts as an individual Fault Domain (or Failure Zone)

An AWS Region acts as a Fault Level (a collection of multiple fault domains).

-------------------------
AWS Global Network and Points of Presence (PoP)

The AWS Global network is the fibre-optic expressway connecting data centers around the world, using Points of Presence (Edge Locations) as on/off ramps so traffic bypasses the slow public internet.

The main goal of AWS Global Network is for efficiency of speed, security and staying away from public internet congestion.

Point of Presence(PoP): the goal of it is to find a physical location (data center/hardware owned by AWS) closest to the end user for content delivery.

Edge Locations: Small data centers that hold cached copies of popular files(images, web pages, videos) near users.

-------------------------
PoP Routing, Direct Connect, & Local Zones
---
AWS Direct Connect

what is it? A dedicated, private physical network between your on-premise data center and AWS.

why does it exist? To bypass the public internet for consistent network performance, lower bandwidth costs, and high throughput.

Security relevance: Traffic stays entirely off the public internet, offering a private, secure pathway for sensitive data.

Exam keyword: Dedicated private connection, by pass public internet, consistent network performance.
---
AWS Local Zones

what is it? AWS infrastructure that places compute and storage services closer to large population centers.

why does it exist? TO deliver single-digit millisecond latency (e.g., 7ms) for highly demanding, time-sensitive applications.

Security relevance: Enables companies with local data residency compliance needs to run workloads locally in specific cities.

Exam keyword: Single-digit millisecond latency, Opt-in, metroplitan areas.

Background
PoPs live at network intersections and connect AZs to Tier-1 transit providers to optimize global data traffic.

------------------
Day 4 (1:55:00 - 2:18:00)
------------------

AWS Wavelength

what is it? AWS infrastructure embedded directly inside telecom 5G networks.

why does it exist? To give mobile applications ultra-low latency by processing data right next to 5G cell towers.

Security relevance: minimize network hops across the open internet by handling data directly within carrier 5G boundaries 

Exam keyword: 5G networks, Ultra-low latency, Telecom partners (verizon, vodafone).

---
AWS Outposts

what is it? A physical rack of AWS hardware delivered and installed inside your own-on premise data center.

why does it exist? to meet strict data residency laws or run ultra-low latency workloads locally using standard AWS APIs.

security relevance: keeps data physically inside you rown building to satisfy local data sovereignty and compliance requirements.

Exam keywords: Physical rack of servers, On-Premise data center, Hybrid cloud, Strict data residency.

---
AWS GovCloud (US)

what is it? Isolated AWS regions designed specifically for US government agencies and vetted public sector organizations.

why does it exist? To host sensitive Controlled Unclassified Information (CUI) and meet strict US government compliance standards (FedRAMP High, ITAR, CJIS)

Security relevance: Managed excusively by US citizens on US soil with strict identity vetting for root account access.

Exam keyword: US Government, FedRAMP, ITAR, US Citizens on US soil, Public Sector.

Background
Data residency regulations mandate where physical data resides, leading to specialized isolated environments like AWS China (amazonaws.cn), which requires a local business license and operates separately from standart global regions.

---
AWS Ground Station

what is it? A fully managed service that allows you to control satellite communications and process satellite data.

Why does it exist? Eliminates the need to build and manage your own expensive physical ground antenna infrastructure to talk to satellites.

Security relevance: Security ingests satellite data directly into AWS services (like Amazon S3) for encrypted storage and processing.

Exam keyword: Satellite communications, Uplink/Downlink data, Satellite imagery, Weather forecasting.
---
AWS Outposts (Deep Dive*)

what it is? Fully managed physical hardware (racks or servers) extending AWS infrastructure directly into on-premise facilities.

Why does it exist? Delivers a consistent hybrid cloud experience by running local AWS compute and storage with single-digit millisecond latency on-site.

Security relevence: Keeps sensitive workloads locked within physical enterprise data center boundaries to meet strict compliance laws.

Exam keyword: Physical rack, On-premises facility, Hybrid experience, 42U/1U/2U form factors.

Background
AWS co-founded The Climate Pledge aiming for Net-zero Carbon by 2040, utilizing 100% renewable energy goals, evaporative water cooling, and energy-efficient data center designs.

------------------
Day 5 (2:18:00 - 3:39:00)
------------------
Cloud Architecture Terminologies

High Availability (HA): Elastic Load Balancer (ELB)

what is it? Designing systems so applications remain operational with zero downtime by eliminating single points of failure.

why does it exist? Automatically shifts traffic away from unhealthy servers/AZs to healthy ones so users experience no service interruption.

Security relevance: Prevents Denial of Service (DoS) conditions caused by single server crashes.

Exam keyword: No single point of failure, Elastic Load Balancer, Remain available.
---
High Scalability & Elasticity: Auto Scaling Groups (ASG)

What is it? Scalability is the capacity to grow; Elasticity is the automated, dynamic expanding (scaling out) and shrinking (scaling in) based on real-time demand

why does it exist? Prevents system crashes during traffic spikes while saving money by removing unused servers when traffic drops.

Exam keyword: Scale Out/ Scale In, Automated capacity, Dynamic demand, Vertical vs Horizontal.

Fault Tolerance & Disaster Recovery (Durability): Amazon RDS Multi-AZ & CloudEndure Disaster Recovery

Exam keyword: Failover, Standby database, Multi-AZ, Prevent data loss, Disaster Recovery (DR).


Background:
Cloud Architects balance Security, Cost, Availability, Scalability, Elasticity, Fault Tolerance, and Disaster Recovery when designing AWS technical solutions.
---
Disaster Recovery Strategy & RPO/RTO

Service: Business Continuity Plan (BCP) & DR Strategies

What is it? RPO (Recovery Point Objective) is acceptable data loss (time back to last backup); RTO (Recovery Time Objective) is acceptable downtime (time until service is restored).

Why does it exist? Balances recovery cost against business loss across Disaster Recovery models: Backup & restore (cheap, hours), Pilot Light (core Database synced, ~10 mins), and Multi-site Active/Active (zero downtime, real-time, expensive).

Security relevance: Guarantees data integrity and operational resilience following severe security breaches or outage events.

Exam keyword: RPO (data loss), RTO (downtime), Pilot Light, Warm Standby, Multi-site Active/Active

---
AWS APIs & Interacting Tools: AWS Application Programming Interface (API)

Service: AWS API

what it is? HTTPS REST endpoints that every AWS service exposes to receive management commands.

Why does it exist? Standardizes how human users, scripts, and software applications make signed requests to control AWS resources.

Security relevance: All API calls require HTTPS authentication via AWS Signatures and IAM permissions 

Exam Keyword: HTTPS Requests, Signed Request, AWS SDK, Management Console, Service Endpoints.

Background:
Disaster Recovery involves trading off cost vs recovery speed, while all AWS developer tools (Console, CLI, SDK) simply act as interfaces that send HTTP/S requests to underlying AWS API service endpoints.
---
AWS Management Console & ClickOps
Service: AWS Management Console

What is it? A web-based graphical interface used to manage and monitor AWS resources via point-and-click actions ("ClickOps")

Why does it exist? Allows users with limited programming knowledge to deploy and configure services easily.

Security relevance: Authenticates via root or IAM user credentials, supporting Multi-Factor Authentication (MFA) and Session Timeouts.

Exam keyword: Web-based unified console, ClickOps, Limited programming knowledge.
---
AWS Account ID & Amazon Resource Names (ARNs)
Service: AWS Account ID & ARNs

What is it? Account ID is a unique 12-digit number identifying an AWS account; ARN is a formatted string that uniquely identifies any specific resource accross all of AWS.

why does it exist? ARNs are strictly required in IAM policies to grant or deny granular permissions to exact resources.

Security relevance: Used for cross-account roles, access control policies, and support cases.

Exam keyword: 12-digit number, Uniquely identify AWS resources.
---
AWS Tools for PowerShell
Service: AWS Tools for PowerShell

what is it? A set of PowerShell Cmdlets (verb-noun commands) that interact with AWS APIs from Windows/Linux PowerShell environments.

Why does it exist? Enables sysadmins comfortable with PowerShell to automate AWS management using .NET objects

Security relevance: Uses AWS credentials/access keys to execute administrative script to manage cloud servers instead of clicking through a web page.

Exam keyword:Powershell Cmdlets, verb and noun (e.g., New-S3Bucket), .NET objects.

Background
The AWS Management Console acts as an umbrella hub containing customized service consoles (e.g., EC2, VPC, Systems Manager) accessible via console.aws.amazon.com.
---
AWS CLI & AWS CloudShell
Service: AWS Command Line Interface (CLI) & AWS CloudShell

What is it? AWS CLI is an executable tool to control AWS services via text commands; AWS CloudShelll is a free, browser-based shell built directly into the Management Console pre-loaded with AWS CLI.

Why does it exist? Enables rapid, programmatic management and automation of cloud resources without cicking through a web UI.

Sercurity relevance: Uses Access Keys (Access Key ID + Secret Access Key) or temporarily assumed console roles for authorization.

Exam keyword: Programmatically interact, Single or multi-line commands, Browser-based shell, 1GB free storage per region.
---
AWS Software Development Kit (SDK)
Service: AWS Software Development Kit (SDK)

What is it? A collection of stoware development tools and libraries enabling deveolpers to interact with AWS services natively within application code.

Why does it exist? Allows custom applications written in popular languages (Python, Java, Nodejs, C++, etc) to create, modify, and delete AWS resources programmatically.

Security relevance: Handles authentication, automatic retries, and request signing behind the scenes using IAM permissions

Exam keyword: Collection of software development tools, Programming languages (python, java, node.js), Embed in application code.
---
Ifrastructure as Code (IaC): CloudFormation & CDK
Service: AWS CloudFormation & AWS Cloud Development Kit (CDK)

What is it? Tools that automate creating, updating, or deleting cloud infrastructure using code blueprint. CloudFormation is declarative (JSON/YAML); CDK is imperative (Python, TypeScript, Java) and synthesizes into CloudFormation templates.

Why does it exist? Replaces manual resource creation with repeatable, version-controlled, and consistent environment deployments.

Security relevance: Eliminates human configuration errors and ensures security policies are consistently applied to new infrastructure stacks.

Exam keywords: Infrastructure as Code (IaC), Blueprint, Declarative (JSON/YAML), CloudFormation Stacks, CDK imperative programming.

Background
AWS CLI relies on Python under the hood and operates across Windows, Mac, and Linux environments.
-----------------------
Day 6 (3:39:00 - 5:00:00)
-----------------------
AWS Access Keys
service: IAM Access Keys

what is it? A two-part credential pair (Access Key ID and Secret Access Key) used for programmatic access to AWS services.

why does it exist? It allows tools like AWS CLI, SDKs, and other devellopment environments to securely interact with the AWS API without a username and password.

Security relevance: Never share them or hardcode them into a codebase. They care the exact same permissions as the IAM user they belong to, and they should be stored securely locally (e.g., in ~/.aws/credentials or as environment variables).

Exam keyword: Programmatic access, Access Key ID and Secret Access Key, Never share or commit to codebase.
---
AWS Shared Responsibility Model
Service: Security Framework

what is it? A cloud security framework dividing security obligations between the Customer and AWS.

why does it exist? To explicitly define who fixes what if something breaks or gets hacked.

security relevance: AWS is responsible for security OF the cloud (hardware, global infrastructure, physical security of data centers). Customers are responsible for security IN the cloud (customer data, IAM permissions, OS patching, encryption, network firewall rules).

Exam keyword: Security IN the cloud (Customer), Security OF the cloud (AWS), Customer Data (Customer), Physical Infrastructure (AWS).

Backgroud
AWS Toolkit for VSCode is an open-source plugin that allows developers to create, debug, and deploy serverless applications and CDK stakcs directly from their code editor.
---
Cloud Service Models (IaaS vs PaaS vs SaaS)
Service: Cloud Deliviery Models

What is it? IaaS give you a maximum control (virtual servers, OS, networking); PaaS manages OS/runtime so you just upload application code; SaaS is fully managed software ready to use.

Why does it exist? Allows organizations to balance operational control against mainenance overhead based on business needs.

Security relevance: The higher up the stack you go (IaaS -> PaaS -> SaaS) the more security responsibility shifts directly onto AWS.

Exam keyword: IaaS (EC2 - OS control), PaaS (Elastic Beanstalk - Upload code) 

IaaS (The Root User): Builds the server foundation and sets the developer permissions.

PaaS (The Developer): Uses that foundation to code, build, and deploy a web application.

SaaS (The End-User): Pays a subscription to log in and use that finished application over the internet.
---
Shared Responsibility Across Compute and Serverless
Service: Compute Spectrum (EC2, Containers, Lambda, Elastic Beanstalk)

What is it? Responsibility varies by compute type: EC2 requires OS patching/firewalls; Containers (ECS/EKS/Fargate) reduce host OS tasks; Lambda (Serverless) leaves only application code and data to the customer.

Why does it exist? Serverless offloads runtime, OS, and server scaling security directly to AWS so developers focus purely on logic.

Security relevance: Serverless minimizes the customer's attack surface by eliminating host OS vulnerability management.

Exam keyword: EC2 (Customer patches Guest OS), Lambda / Fargate (less customer responsibility), Elastic Beanstalk (PaaS)

Background:
Rule of thumb: "If you can configure or store it, you are responsible for it; if you cannot configure it, AWS is responsible for it."
---
Core Computer Service and Containers
Service: Amazon EC2, Lightsail, ECS, ECR, EKS, Fargate, Lambda.

What is it? EC2 (Elastic Compute Cloud) is an advanced, pay-as-you-go, full control and elastic virtual computer usually used by big companies that have random high demand and low demand days that needs to be adjusted which will save them more money in the long run using elasticity. Amazon Lightsail is also a virtual computer is a simple, fixed price, pre-built virtual machine usually used by small blogs, simple websites and beginner projects which wont need any advanced VMs becuase it'll confuse the owner. ECS (Elastic Container Service) is a tool by Amazon that helps you run computer programs safely inside containers (small boxes with everything an app needs to run). ECR is like a Docker Hub meaning it stores the container images securely and privately. EKS is a an (Elastic Kubernetes Service) "smart robot helper that takes care of the hard computer setup work so your website or app stays running." Kubernetes: The manager robot that watches all the containers, turns more on when it gets busy, and fixes them if they break (more complex and costly than ECS). Fargate runs containers serverlessly. AWS Fargate is a tool that manages, creates and runs containers without needing to directly configure a server and manage it. 

why does it exist? Gives flexibility ranging from full virtual server customizatin down to automated, zero-infrastructure container or function execution.

Security relevance: EC2 requires guest OS patching, while Fargate and Lambda transfer host OS and runtime patch responsibilities directly to AWS.

Exam keyword: Virtual Machine/ Instance, AMI, Lightsail (Simple/WordPress), ECS (Docker), ECR (Image repository), Fargate (Serverless container) , EKS (Kubernetes), Lambda (Serverless function).
---
High Performance Computing (HPC) & Infrastructure 
service: AWS Nitro System, Bare Metal, Battlerocket, AWS ParallelCluster

What is it? The Nitro System offloads hypervisor tasks to dedicated hardware cards for maximum speed and security. Bare Metal by passes hypervisors entirely for raw hardware access. Bottlerocket is a purpose-built Linux OS for containers. AWS ParallelCluster automates deploying HPC compute clusters.

Why does it exist? Delivers supercomputing performance for heavy computational tasks, AI/ML, and low-latency workloads.

Security relevance: Nitro Security Chips isolate physical hardware resources directly on the motherboard.

Exam keyword: Nitro System (Dedicated hardware/lightweight hypervisor), Bare Metal (No Hypervisor), Bottlerocket (Open-source container OS), ParallelCluster (HPC cluster management).

Background
EC2 serves as the backbone of AWS infrastructure because many higher-level managed services run on EC2 instances behind the scenes.
-----------------------
Day 7 (5:00:00 - 6:00:00)
-----------------------
Service: Edge Computing and Hybrid Computing Services (AWS Outposts, AWS Wavelength, AWS Local Zones)

What is it? Infrastructure solutions that extends AWS compute, storage, and networking closer to end users or directly into on-premises data centers.

Why does it exist? To solve strict local data soverignty requirements and provide single-digit millisecond latency, for applications that cannot tolerate long network transit times to main AWS Regions.

Security relevance: Enables companies with regulatory compliance laws to physically store sensitive data inside their own data center boundaries or within carrier boundaries.

Exam Keyword: Physical rack on-premise (Outposts), 5G networks/telecom (Wavelength), Metrapoliran areas outside region (Local Zones).
---
Service: Cost and Capacity Management Services (Compute Optimizer, Auto Scaling, ELB, Elastic Beanstalk)

What is it? A collection of AWS compute services and features designed to optimize costs, automate resource scaling, and balance application traffic.

Why does it exist? To prevent manual server provisioning, eliminate wasted spending on idle capacity, and maintain application availability, during sudden traffic spikes.

Security Relevance: ELBs prevent Denial of Service (DoS) outages by routing traffic away from unhealthy instances, while Auto Scaling prevents resource exhaustion crashes. 

Exam keyword: ML recommendations to reduce cost "helps tell you how to manage your cloud for cost optimizations" (Compute Optimizer), dynmaic capacity scaling "Elasticity" (Auto Scaling Group), health check traffic routing "if a server had an issue it would reroute you to a different server" (Elastic Load Balancer), PaaS deployment "Platform as a Service Deployment of application" (Elastic Beanstalk).
---
Types of Storage Service:
Service/ Concept Name: Storage Types Comparison (EBS vs EFS vs S3)

What is it? The three primary storage architectures offered by AWS: Block (EBS), File (EFS), Object (S3).

Why does it exist? Different application workloads require different storage mechanisms (e.g., operating system boot drives vs shared network drives vs mass file storage). 

Security relevance: EBS and EFS support POSIX access controls and volume-level encryption; S3 uses IAM policies, Bucket policies, and SCLs for web-scale permission management.

Exam Keyword: Single VM attach / block (EBS), Shared file system across multiple VMs / NFS (EFS), Web-accessible object storage with meta data (S3).
---
Service/Concept Name: Amazon Simple Storage Service (S3) Deep Dive

What is it? An object storage system that stores data as "object" inside "buckets" with globally unique names.

Why does it exist? To store unlimited amounts of unstructured data (0 bytes to 5TB per individual object) without managing server hardware.

Security Relevance: S3 buckets are private by default; public access must be explicitly enabled, and buckets can be encrypted at rest using KMS.

Exam Keyword: Globally unique bucket namespace, 0 Bytes to 5 TB object size limit, Key/Value pairs + Metadata.
---
AWS Snow family (Snowcone, Snowball Edge)

What is it? Physical secure edge computing and data transfer appliances used to move large datasets into or out of AWS offline.

Why does it exist? Network transfers of petabyte-scale data over standard internet connections can take months or years; shipping physical hardware is faster and more reliable. 

Security relevance: Devices feature tamper-evident enclosures, hardware encryption, and strict chain-of-custody tracking.

Exam keyword: Offline physical data migration, Petabyte scale (Snowball Edge), Edge computing in remote/disconnected locations. Note on AWS Snowmobile: As of 2024, AWS retired the Snowmobile shipping container truck service. On the CLF-C02 exam, focus on Snowcone and Snowball Edge for physical data transfers.
---
AWS Storage Gateway (and Core Storage Recap)

What is it? A hybrid cloud storage service that seamlessly connects an on-premises environment to AWS cloud storage (S3).

Why does it exist? To allow on-premises applications to use cloud storage without replacing existing local infrastructure or software workflows.

Security Relevance: Integrates with AWS KMS for encryption at rest and uses secure SSL/TLS channels for data in transit over the internet or AWS Direct Connect.

Exam Keyword: Hybrid cloud storage, extend on-premises storage to S3, S3 File Gateway / Volume Gateway / Tape Gateway.
---
AWS Backup & Amazon FSx

What is it? AWS Backup provides centralized, automated backup management across AWS services; Amazon FSx offers fully managed, high-performance file systems tailored for Windows (SMB) or high-performance Linux (Lustre) workloads.

Why does it exist? AWS Backup eliminates manual, piecemeal snapshots across different services; FSx provides native Windows file system compatibility and high-performance compute file sharing that native EFS cannot support.

Security Relevance: AWS Backup allows enforcing cross-region/cross-account backup policies and immutable backups (AWS Backup Vault Lock) for ransomware protection.

Exam Keyword: Centralized automated backup policy (AWS Backup), Windows SMB file share / Lustre high-performance compute (Amazon FSx).
------------------
Day 8 (6:00:00 - )
------------------
Databases vs. Data Warehouses:
Service: Database Concepts (Row-oreiented vs. Coloumn-oriented)

What is it? Relational databases store structured, row-oriented data ideal for OLTP (Online Transactional Processing) like e-commerce orders. Data Warehouses store column-oriented data optimized for OLAP (Online Analytical Processing) to aggregate huge datasets for business reports.

Why does it exist? Transactional databases handle high-volume individual reads/writes, while data warehouses run complex analytical queries across millions of rows efficiently.

Security relevance: Access controls and encryption must be configured for both transactional and historical analytical data repositories.

Exam keyword: Relational (Row-oriented / OLTP), Data Warehouse (Column-oriented / Analytics / Aggregation).
---
NoSQL Databases (DynamoDB, DocumentDB, Keyspaces)
Service: Amazon DynamoDB, Amazon DocumentDB, Amazon Keyspaces

What is it? DynamoDB is AWS's flagship serverless NoSQL key-value and document database designed for single-digit millisecond performance at massive scale. DocumentDB is a managed MongoDB-compatible database. Keyspaces is a managed Apache Cassandra-compatible database.

Why does it exist? Provides schemaless, ultra-fast scaling beyond traditional relational database boundaries without operational overhead like sharding.

Security relevance: Fine-grained access control can be tied directly to IAM policies and primary key values.

Exam keyword: DynamoDB (Serverless / Key-Value & Document / Massive scale), DocumentDB (MongoDB), Keyspaces (Apache Cassandra).
---
Relational Databases Services (RDS and Aurora)
service: Amazon RDS, Amazon Aurora, Aurora Serverless, RDS on VMware

What is it? RDS is a managed relational database service supporting 6 SQL engines (MySQL, MariaDB, PostgreSQL, Oracle, SQL Server, Aurora). Amazon Aurora is AWS's cloud-native relational database (up to 5x faster than MySQL and 3x faster than PostgreSQL). Aurora Serverless auto-scales on demand. RDS on VMware runs RDS in on-premises data centers.

Why does it exist? Offloads routine database administrative tasks like provisioning, patching, backup, and recovery for transactional (OLTP) applications.

Security relevance: Automated patching, encryption at rest via KMS, and network isolation within Amazon VPC.

Exam keyword: RDS (Relational / OLTP), Aurora (5x MySQL / 3x Postgres performance), Aurora Serverless (Auto-scaling / On-demand relational), RDS on VMware (On-premises).
---
Specialized Database & Caching Services
Service: Amazon Redshift, ElastiCache, Neptune, Timestream, QLDB, Database Migration Service (DMS)

What is it? Redshift is a petabyte-scale data warehouse (OLAP). ElastiCache provides in-memory caching using Redis or Memcached. Neptune is a graph database (social networks, fraud rings). Timestream tracks time-series data (IoT metrics). QLDB is an immutable, cryptographically verifiable ledger database. DMS migrates databases to AWS (including SQL to NoSQL).

Why does it exist? Matches specific database architectures to specialized data storage and caching requirements.

Security relevance: QLDB provides a cryptographically verifiable log that cannot be altered or deleted.

Exam keyword: Redshift (Data warehouse / OLAP / Analytics), ElastiCache (In-memory caching / Redis / Memcached), Neptune (Graph / Social media / Fraud detection), Timestream (IoT / Time-series), QLDB (Ledger / Immutable / Cryptographic), DMS (Database migration).