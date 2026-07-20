# AWS Cloud Practitioner Notes
## Exam Date: August 12 2026
## Goal: Pass CLF-C02

---
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

Kondratiev waves: is the technology lifecycle like phenomany which irreversible changes the society on a global scale, a common patter of a wave is the change of supply an demand. 

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




















