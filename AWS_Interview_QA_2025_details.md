
<details>
  <summary><strong>Q1) What is AWS?</strong></summary>
  <p>AWS stands for Amazon Web Services. AWS is a platform that provides on-demand resources for hosting web services, storage, networking, databases and other resources over the internet with a pay-as-you-go pricing.</p>
</details>

<details>
  <summary><strong>Q2) What are the components of AWS?</strong></summary>
  <p>EC 2  ElasticComputeCloud, S3  SimpleStorageService, Store, Cloudwatch, Key-Paris are few of the components of AWS.</p>
</details>

<details>
  <summary><strong>Q3) What are key-pairs?</strong></summary>
  <p>Key-pairs are secure login information for your instances/virtual machines. To connect to the instances we use key-pairs that contain a public-key and private-key.</p>
</details>

<details>
  <summary><strong>Q4) What is S3?</strong></summary>
  <p>S3 stands for Simple Storage Service. It is a storage service that provides an interface that you can use to store any amount of data, at any time, from anywhere in the world. With S3 you pay only for what you use and the payment model is pay-as-you-go.</p>
</details>

<details>
  <summary><strong>Q5) What are the pricing models for EC2instances?</strong></summary>
  <p>The different pricing model for EC2 instances are as below, On-demand Reserved Spot Scheduled Dedicated</p>
</details>

<details>
  <summary><strong>Q6) What are the types of volumes for EC2 instances?</strong></summary>
  <p>There are two types of volumes, Instance store volumes EBS  ElasticBlockStores</p>
</details>

<details>
  <summary><strong>Q7) What are EBS volumes?</strong></summary>
  <p>EBS stands for Elastic Block Stores. They are persistent volumes that you can attach to the instances. With EBS volumes, your data will be preserved even when you stop your instances, unlike your instance store volumes where the data is deleted when you stop the instances.</p>
</details>

<details>
  <summary><strong>Q8) What are the types of volumes in EBS?</strong></summary>
  <p>Following are the types of volumes in EBS, General purpose Provisioned IOPS Magnetic Cold HDD Throughput optimized</p>
</details>

<details>
  <summary><strong>Q9) What are the different types of instances?</strong></summary>
  <p>Following are the types of instances, General purpose Computer Optimized Storage Optimized Memory Optimized Accelerated Computing</p>
</details>

<details>
  <summary><strong>Q10) What is an auto-scaling and what are the components?</strong></summary>
  <p>Auto scaling allows you to automatically scale-up and scale-down the number of instances depending on the CPU utilization or memory utilization. There are 2 components in Auto scaling, they are Auto-scaling groups and Launch Configuration. Get AWS Online Training</p>
</details>

<details>
  <summary><strong>Q11) What are reserved instances?</strong></summary>
  <p>Reserved instances are the instance that you can reserve a fixed capacity of EC2 instances. In reserved instances you will have to get into a contract of 1 year or 3 years.</p>
</details>

<details>
  <summary><strong>Q12) What is an AMI?</strong></summary>
  <p>AMI stands for Amazon Machine Image. AMI is a template that contains the software configurations, launch permission and a block device mapping that specifies the volume to attach to the instance when it is launched.</p>
</details>

<details>
  <summary><strong>Q13) What is an EIP?</strong></summary>
  <p>EIP stands for Elastic IP address. It is designed for dynamic cloud computing. When you want to have a static IP address for your instances when you stop and restart your instances, you will be using EIP address.</p>
</details>

<details>
  <summary><strong>Q14) What is Cloudwatch?</strong></summary>
  <p>Cloudwatch is a monitoring tool that you can use to monitor your various AWS resources. Like health check, network, Application, etc.</p>
</details>

<details>
  <summary><strong>Q15) What are the types in cloudwatch?</strong></summary>
  <p>There are 2 types in cloudwatch. Basic monitoring and detailed monitoring. Basic monitoring is free and detailed monitoring is chargeable.</p>
</details>

<details>
  <summary><strong>Q16) What are the cloudwatch metrics that are available for EC2 instances?</strong></summary>
  <p>Diskreads, Diskwrites, CPU utilization, networkpacketsIn, networkpacketsOut, networkIn, networkOut, CPUCreditUsage, CPUCreditBalance.</p>
</details>

<details>
  <summary><strong>Q17) What is the minimum and maximum size of individual objects that you can store in S3</strong></summary>
  <p>The minimum size of individual objects that you can store in S3 is 0 bytes and the maximum bytes that you can store for individual objects is 5TB.</p>
</details>

<details>
  <summary><strong>Q18) What are the different storage classes in S3?</strong></summary>
  <p>Following are the types of storage classes in S3, Standard frequently accessed Standard infrequently accessed One-zone infrequently accessed. Glacier RRS  reducedredundancystorage</p>
</details>

<details>
  <summary><strong>Q19) What is the default storage class in S3?</strong></summary>
  <p>The default storage class in S3 in Standard frequently accessed. Became an AWS Expert with Certification in 25hours</p>
</details>

<details>
  <summary><strong>Q20) What is glacier?</strong></summary>
  <p>Glacier is the back up or archival tool that you use to back up your data in S3.</p>
</details>

<details>
  <summary><strong>Q21) How can you secure the access to your S3 bucket?</strong></summary>
  <p>There are two ways that you can control the access to your S3 buckets, ACL  Access ControlList Bucket polices</p>
</details>

<details>
  <summary><strong>Q22) How can you encrypt data in S3?</strong></summary>
  <p>You can encrypt the data by using the below methods, ServerSideEncryptionS3 ( AES256encryption ) ServerSideEncryptionKMS ( KeymanagementService ) ServerSideEncryptionC ( ClientSide )</p>
</details>

<details>
  <summary><strong>Q23) What are the parameters for S3 pricing?</strong></summary>
  <p>The pricing model for S3 is as below, Storage used Number of requests you make Storage management Data transfer Transfer acceleration</p>
</details>

<details>
  <summary><strong>Q24) What is the pre-requisite to work with Cross region replication in S3?</strong></summary>
  <p>You need to enable versioning on both source bucket and destination to work with cross region replication. Also both the source and destination bucket should be in different region.</p>
</details>

<details>
  <summary><strong>Q25) What are roles?</strong></summary>
  <p>Roles are used to provide permissions to entities that you trust within your AWS account. Roles are users in another account. Roles are similar to users but with roles you do not need to create any username and password to work with the resources.</p>
</details>

<details>
  <summary><strong>Q26) What are policies and what are the types of policies?</strong></summary>
  <p>Policies are permissions that you can attach to the users that you create. These policies will contain that access that you have provided to the users that you have created. There are 2 types of policies. Managed policies Inline policies</p>
</details>

<details>
  <summary><strong>Q27) What is cloudfront?</strong></summary>
  <p>Cloudfront is an AWS web service that provided businesses and application developers an easy and efficient way to distribute their content with low latency and high data transfer speeds. Cloudfront is content delivery network of AWS.</p>
</details>

<details>
  <summary><strong>Q28) What are edge locations?</strong></summary>
  <p>Edge location is the place where the contents will be cached. When a user tries to access some content, the content will be searched in the edge location. If it is not available then the content will be made available from the origin location and a copy will be stored in the edge location.</p>
</details>

<details>
  <summary><strong>Q29) What is the maximum individual archive that you can store in glacier?</strong></summary>
  <p>You can store a maximum individual archive of upto 40 TB. Get AWS 100% Practical Training</p>
</details>

<details>
  <summary><strong>Q30) What is VPC?</strong></summary>
  <p>VPC stands for Virtual Private Cloud. VPC allows you to easily customize your networking configuration. VPC is a network that is logically isolated from other network in the cloud. It allows you to have your own IP address range, subnets, internet gateways, NAT gateways and security groups.</p>
</details>

<details>
  <summary><strong>Q31) What is VPC peering connection?</strong></summary>
  <p>VPC peering connection allows you to connect 1 VPC with another VPC. Instances in these VPC behave as if they are in the same network.</p>
</details>

<details>
  <summary><strong>Q32) What are NAT gateways?</strong></summary>
  <p>NAT stands for Network Address Translation. NAT gateways enables instances in a private subnet to connect to the internet but prevent the internet from initiating a connection with those instances.</p>
</details>

<details>
  <summary><strong>Q33) How can you control the security to your VPC?</strong></summary>
  <p>You can use security groups and NACL (Network Access Control List) to control the security to your VPC.</p>
</details>

<details>
  <summary><strong>Q34) What are the different types of storage gateway?</strong></summary>
  <p>Following are the types of storage gateway. File gateway Volume gateway Tape gateway</p>
</details>

<details>
  <summary><strong>Q35) What is a snowball?</strong></summary>
  <p>Snowball is a data transport solution that used source appliances to transfer large amounts of data into and out of AWS. Using snowball, you can move huge amount of data from one place to another which reduces your network costs, long transfer times and also provides better security.</p>
</details>

<details>
  <summary><strong>Q36) What are the database types in RDS?</strong></summary>
  <p>Following are the types of databases in RDS, Aurora Oracle MYSQL server Postgresql MariaDB SQL server</p>
</details>

<details>
  <summary><strong>Q37) What is a redshift?</strong></summary>
  <p>Amazon redshift is a data warehouse product. It is a fast and powerful, fully managed, petabyte scale data warehouse service in the cloud.</p>
</details>

<details>
  <summary><strong>Q38) What is SNS?</strong></summary>
  <p>SNS stands for Simple Notification Service. SNS is a web service that makes it easy to notifications from the cloud. You can set up SNS to receive email notification or message notification.</p>
</details>

<details>
  <summary><strong>Q39) What are the types of routing polices in route53?</strong></summary>
  <p>Following are the types of routing policies in route53, Simple routing Latency routing Failover routing Geolocation routing Weighted routing Multivalue answer</p>
</details>

<details>
  <summary><strong>Q40) What is the maximum size of messages in SQS?</strong></summary>
  <p>The maximum size of messages in SQS is 256 KB.</p>
</details>

<details>
  <summary><strong>Q41) What are the types of queues in SQS?</strong></summary>
  <p>There are 2 types of queues in SQS. Standard queue FIFO (First In First Out)</p>
</details>

<details>
  <summary><strong>Q42) What is multi-AZ RDS?</strong></summary>
  <p>Multi-AZ (Availability Zone) RDS allows you to have a replica of your production database in another availability zone. Multi-AZ (Availability Zone) database is used for disaster recovery. You will have an exact copy of your database. So when your primary database goes down, your application will automatically failover to the standby database.</p>
</details>

<details>
  <summary><strong>Q43) What are the types of backups in RDS database?</strong></summary>
  <p>There are 2 types of backups in RDS database. Automated backups Manual backups which are known as snapshots.</p>
</details>

<details>
  <summary><strong>Q44) list?</strong></summary>
  <p>Security Groups Network access control list Can control the access at the instance level Can control access at the subnet level Can add rules for "allow" only Can add rules for both "allow" and "deny" Evaluates all rules before allowing the traffic Rules are processed in order number when allowing traffic. Can assign unlimited number of security groups Can assign upto 5 security groups. Statefull filtering Stateless filtering</p>
</details>

<details>
  <summary><strong>Q45) What are the types of load balancers in EC2?</strong></summary>
  <p>There are 3 types of load balancers, Application load balancer Network load balancer Classic load balancer Become an AWS Certified Expert in 25Hours</p>
</details>

<details>
  <summary><strong>Q46) What is and ELB?</strong></summary>
  <p>ELB stands for Elastic Load balancing. ELB automatically distributes the incoming application traffic or network traffic across multiple targets like EC2, containers, IP addresses.</p>
</details>

<details>
  <summary><strong>Q47) creating users?</strong></summary>
  <p>Following are the two types of access that you can create. Programmatic access Console access</p>
</details>

<details>
  <summary><strong>Q48) What are the benefits of auto scaling?</strong></summary>
  <p>Following are the benefits of auto scaling Better fault tolerance Better availability Better cost management</p>
</details>

<details>
  <summary><strong>Q49) What are security groups?</strong></summary>
  <p>Security groups acts as a firewall that contains the traffic for one or more instances. You can associate one or more security groups to your instances when you launch then. You can add rules to each security group that allow traffic to and from its associated instances. You can modify the rules of a security group at any time, the new rules are automatically and immediately applied to all the instances that are associated with the security group Get AWS Online Training</p>
</details>

<details>
  <summary><strong>Q50) WhataresharedAMIs ?</strong></summary>
  <p>SharedAMIsaretheAMIthatarecreatedbyotherdevelo other developed to use.</p>
</details>

<details>
  <summary><strong>Q51) load balancer?</strong></summary>
  <p>Dynamic port mapping, multiple port multiple listeners is used in Application Load Balancer, One port one listener is achieved via Classic Load Balancer</p>
</details>

<details>
  <summary><strong>Q52) By default how many Ip address does aws reserve in a subnet?</strong></summary>
  <p>5</p>
</details>

<details>
  <summary><strong>Q53) What is meant by subnet?</strong></summary>
  <p>A large section of IP Address divided in to chunks are known as subnets</p>
</details>

<details>
  <summary><strong>Q54) How can you convert a public subnet to private subnet?</strong></summary>
  <p>Remove IGW & add NAT Gateway, Associate subnet in Private route table</p>
</details>

<details>
  <summary><strong>Q55) Answer: noitsnotpossible , wecanincreaseitbutnotreducethe Q56) What is the use of elastic ip are they charged by AWS?</strong></summary>
  <p>These are ipv4 address which are used to connect the instance from internet, they are charged if the instances are not attached to it</p>
</details>

<details>
  <summary><strong>Q56) way?</strong></summary>
  <p>If versioning is enabled we can easily restore them</p>
</details>

<details>
  <summary><strong>Q57) to fix the issue?</strong></summary>
  <p>By default AWS offer service limit of 20 running instances per region, to fix the issue we need to contact AWS support to increase the limit based on the requirement</p>
</details>

<details>
  <summary><strong>Q58) I need to modify the ebs volumes in Linux and windows is it possible</strong></summary>
  <p>yes its possible from console use modify volumes in section give the size u need then for windows go to disk management for Linux mount it to achieve the modification Get AWS Online Training</p>
</details>

<details>
  <summary><strong>Q59) Answer: Yesitspossibletostoprds . Instancewhicharenon - prod Q61) What is meant by parameter groups in rds. And what is the use of it?</strong></summary>
  <p>Since RDS is a managed service AWS offers a wide set of parameter in RDS as parameter group which is modified as per requirement</p>
</details>

<details>
  <summary><strong>Q60) What is the use of tags and how they are useful?</strong></summary>
  <p>Tags are used for identification and grouping AWS Resources</p>
</details>

<details>
  <summary><strong>Q61) an IAM Error how can I rectify it?</strong></summary>
  <p>AsAWSuserIdonthaveaccesstouseit , IneedtohaveQ64 ) IdontwantmyAWSAccountidtobeexposedto Answer: In IAM console there is option as sign in url where I can rename my own account name with AWS account</p>
</details>

<details>
  <summary><strong>Q62) By default how many Elastic Ip address does AWS Offer?</strong></summary>
  <p>5 elastic ip per region</p>
</details>

<details>
  <summary><strong>Q63) instance?</strong></summary>
  <p>Binds the user session with a specific instance</p>
</details>

<details>
  <summary><strong>Q64) Which type of load balancer makes routing decisions at either the transport layer or the Application layer and supports either EC2 or VPC.</strong></summary>
  <p>Classic Load Balancer</p>
</details>

<details>
  <summary><strong>Q65) VPC?</strong></summary>
  <p>Elastic Network Interface</p>
</details>

<details>
  <summary><strong>Q66) Have selected SSH, HTTP, HTTPS protocol. Why do we need to select SSH?</strong></summary>
  <p>To verify that there is a rule that allows traffic from EC2 Instance to your computer</p>
</details>

<details>
  <summary><strong>Q67) Security group. How will these changes be effective?</strong></summary>
  <p>Changes are automatically applied to windows instances</p>
</details>

<details>
  <summary><strong>Q68) Load Balancer and DNS service comes under which type of cloud service?</strong></summary>
  <p>IAAS-Storage</p>
</details>

<details>
  <summary><strong>Q69) can achieve this?</strong></summary>
  <p>Create a snapshot of the unencrypted volume (applying encryption parameters), copy the. Snapshot and create a volume from the copied snapshot</p>
</details>

<details>
  <summary><strong>Q70) auto scaling Commands?</strong></summary>
  <p>Auto scaling Launch Config</p>
</details>

<details>
  <summary><strong>Q71) Which are the types of AMI provided by AWS?</strong></summary>
  <p>Instance Store backed, EBS Backed</p>
</details>

<details>
  <summary><strong>Q72) always attached to a Single instance. What setting can you use?</strong></summary>
  <p>Sticky session</p>
</details>

<details>
  <summary><strong>Q73) When do I prefer to Provisioned IOPS over the Standard RDS storage?</strong></summary>
  <p>If you have do batch-oriented is workloads.</p>
</details>

<details>
  <summary><strong>Q74) instance?</strong></summary>
  <p>Primary db instance does not working.</p>
</details>

<details>
  <summary><strong>Q75) e-commerce data for the near by real-time analysis?</strong></summary>
  <p>Good of Amazon DynamoDB.</p>
</details>

<details>
  <summary><strong>Q76) providestothesolutionforcompanysrequirements ?</strong></summary>
  <p>An web application provide on Amazon DynamoDB solution.</p>
</details>

<details>
  <summary><strong>Q77) Which the statement use to cases are suitable for Amazon DynamoDB?</strong></summary>
  <p>The storing metadata for the Amazon S3 objects& The Running of relational joins and complex an updates.</p>
</details>

<details>
  <summary><strong>Q78) you recommend do?</strong></summary>
  <p>Introduce Amazon Elasticache to the cache reads from the Amazon DynamoDB table and to reduce the provisioned read throughput.</p>
</details>

<details>
  <summary><strong>Q79) approaches to the meet these requirements?</strong></summary>
  <p>The Deploy Elasti Cache in-memory cache is running in each availability zone and Then Increase the RDS MySQL Instance size and the Implement provisioned IOPS.</p>
</details>

<details>
  <summary><strong>Q80) analyze it. Which setup of following would you be prefer?</strong></summary>
  <p>The Replace the RDS instance with an 6 node Redshift cluster with take 96TB of storage.</p>
</details>

<details>
  <summary><strong>Q81) your need?</strong></summary>
  <p>Used on Application Load Balancer.</p>
</details>

<details>
  <summary><strong>Q82) change it from areas?</strong></summary>
  <p>Changed to Auto Scaling launch configuration areas.</p>
</details>

<details>
  <summary><strong>Q83) reduce load on the Amazon EC2 instance?</strong></summary>
  <p>Let Create a load balancer, and Give register the Amazon EC2 instance with it.</p>
</details>

<details>
  <summary><strong>Q84) What does the Connection of draining do?</strong></summary>
  <p>The re-routes traffic from the instances which are to be updated (or) failed an health to check.</p>
</details>

<details>
  <summary><strong>Q85) new ones, which of the services does that?</strong></summary>
  <p>The survice make a fault tolerance.</p>
</details>

<details>
  <summary><strong>Q86) What are the life cycle to hooks used for the AutoScaling?</strong></summary>
  <p>They are used to the put an additional taken wait time to the scale in or scale out events. Are You Interested in AWS Course ? Click here</p>
</details>

<details>
  <summary><strong>Q87) be happen to the Auto Scaling in the condition?</strong></summary>
  <p>The auto Scaling will be suspend to the scaling process.</p>
</details>

<details>
  <summary><strong>Q88) instances in the same of Security Group.Such the new rules apply?</strong></summary>
  <p>The Immediately to all the instances in security groups.</p>
</details>

<details>
  <summary><strong>Q89) to be recreated in second region?</strong></summary>
  <p>May be the selected on Route 53 Record Sets.</p>
</details>

<details>
  <summary><strong>Q90) select option should he choose for his application?</strong></summary>
  <p>The condition should be Enable to AWS CloudTrail for the loadbalancers.</p>
</details>

<details>
  <summary><strong>Q91) Which of the services to you would not use to deploy an app?</strong></summary>
  <p>Lambda app not used on deploy.</p>
</details>

<details>
  <summary><strong>Q92) How do the Elastic Beanstalk can apply to updates?</strong></summary>
  <p>By a duplicate ready with a updates prepare before swapping.</p>
</details>

<details>
  <summary><strong>Q93) tried, then key that I just created is not listed.What could be reason&solution?</strong></summary>
  <p>The Key should be working in the same region.</p>
</details>

<details>
  <summary><strong>Q94) AWS services to can accomplish this?</strong></summary>
  <p>The monitoring on Amazon CloudWatch</p>
</details>

<details>
  <summary><strong>Q95) both existing company and then acquired company, is billed to the single account?</strong></summary>
  <p>All InvitestakeacquiredthecompanysAWSaccounttojoinexisting by using AWS Organizations.</p>
</details>

<details>
  <summary><strong>Q96) of respect to best practice for the security in this scenario?</strong></summary>
  <p>The user should be attach an IAM roles with the DynamoDB access to EC2 instance.</p>
</details>

<details>
  <summary><strong>Q97) access S3 bucket securely?</strong></summary>
  <p>An Create an IAM role for the EC2 that allows list access to objects in S3 buckets. Launch toinstancewiththisrole , andretrieveanrolescredentialsfrom Q101) You use the Amazon CloudWatch as your primary monitoring system for web application. After a recent to software deployment, your users are to getting Intermittent the 500 Internal Server to the Errors, when you using web application. You want to create the CloudWatch alarm, and notify the on-call engineer let when these occur. How can you accomplish the using the AWS</p>
</details>

<details>
  <summary><strong>Q98) services?</strong></summary>
  <p>An Create a CloudWatch get Logs to group and A define metric filters that assure capture 500 Internal Servers should be Errors. Set a CloudWatch alarm on the metric and By Use of Amazon Simple to create a Notification Service to notify an the on-call engineers when prepare CloudWatch alarm is triggered.</p>
</details>

<details>
  <summary><strong>Q99) most cost effective and Like performance efficient the architecture setup?</strong></summary>
  <p>Assign to multiple ELBs an EC2 instance or group of EC2 take instances running to common component of the web application, one ELB change for each platform type.Take Session will be stickiness and SSL termination are done for the ELBs.</p>
</details>

<details>
  <summary><strong>Q100) scalability and high availability?</strong></summary>
  <p>File a change request to get implement of Proxy Protocol support in the application. Use of ELB with TCP Listener and A Proxy Protocol enabled to distribute the load on two application servers in the different AZs.</p>
</details>

<details>
  <summary><strong>Q101) during the ramp up traffic?</strong></summary>
  <p>Check the service limits in the Trusted Advisors and adjust as necessary, so that forecasted count remains within the limits.</p>
</details>

<details>
  <summary><strong>Q102) you make?</strong></summary>
  <p>Deploy to 3 EC2 instances in one of availability zone and 3 in another availability of zones and to use of Amazon Elastic is Load Balancer.</p>
</details>

<details>
  <summary><strong>Q103) requirements?</strong></summary>
  <p>Use TCP load balancing on load balancer system, SSL termination on Amazon to create EC2 instances, OS-level disk take encryption on Amazon EBS volumes, and The amazon S3 with server-side to encryption and Use the SSL termination on load balancers, an SSL listener on the Amazon to create EC2 instances, Amazon EBS encryption on the EBS volumes containing the PHI, and Amazon S3 with a server-side of encryption.</p>
</details>

<details>
  <summary><strong>Q104) servers?</strong></summary>
  <p>Result of cloud is re-configure the load-testing software to the re-resolve DNS for each web request.</p>
</details>

<details>
  <summary><strong>Q105) c3 . 2xlargeinstanceshavesignificanttocapacitythat option is the most of cost effective and uses EC2 capacity most of effectively?</strong></summary>
  <p>To use a separate ELB for the each instance type and the distribute load to ELBs with a Route 53 weighted round of robin.</p>
</details>

<details>
  <summary><strong>Q106) configurations will support these requirements?</strong></summary>
  <p>The configure to the web application get authenticate end-users against the centralized access on the management system. Have a web application provision trusted to users STS tokens an entitling the download of the approved data directly from a Amazon S3.</p>
</details>

<details>
  <summary><strong>Q107) time-efficient way?</strong></summary>
  <p>By Using a VPC, they could be create an the extension to their data center and to make use of resilient hardware IPSEC on tunnels, they could then have two domain consider to controller instances that are joined to the existing domain and reside within the different subnets in the different availability zones. Get AWS Online Training!</p>
</details>

<details>
  <summary><strong>Q108) What is Cloud Computing?</strong></summary>
  <p>Cloud computing means it provides services to access programs, application, storage, network, server over the internet through browser or client side application on your PC, Laptop, Mobile by the end user without installing, updating and maintaining them. Cloud computing is a cloud platform service that provides you with theon-demand services that can range from compute, databases, storage, networking, applications and so on. Cloud computing follows your pay-as-you-go model where you are going to pay only for what you are using.</p>
</details>

<details>
  <summary><strong>Q109) Why we go for Cloud Computing?</strong></summary>
  <p>Lower computing cost Improved Performance No IT Maintenance Business connectivity Easily upgraded Device Independent</p>
</details>

<details>
  <summary><strong>Q110) What are the deployment models using in Cloud?</strong></summary>
  <p>Private Cloud Public Cloud Hybrid cloud Community cloud 4</p>
</details>

<details>
  <summary><strong>Q111) Explain Cloud Service Models?</strong></summary>
  <p>SAAS (Software as a Service): It is software distribution model in which application are hosted by a vendor over the internet for the end user freeing from complex software and hardware management. (Ex: Google drive, drop box) PAAS (Platform as a Service): It provides platform and environment to allow developers to build applications. It frees developers without going into the complexity of building and maintaining the infrastructure. (Ex: AWS Elastic Beanstalk, Windows Azure) IAAS (Infrastructure as a Service): It provides virtualized computing resources over the internet like cpu, memory, switches, routers, firewall, Dns, Load balancer (Ex: Azure, AWS)</p>
</details>

<details>
  <summary><strong>Q112) What are the advantage of Cloud Computing?</strong></summary>
  <p>Pay per use Scalability Elasticity High Availability Increase speed and Agility Go global in Minutes</p>
</details>

<details>
  <summary><strong>Q113) What is AWS?</strong></summary>
  <p>Amazon web service is a secure cloud services platform offering compute, power, database, storage, content delivery and other functionality to help business scale and grow. AWS is fully on-demand AWS is Flexibility, availability and Scalability AWS is Elasticity: scale up and scale down as needed.</p>
</details>

<details>
  <summary><strong>Q114) What is mean by Region, Availability Zone and Edge Location?</strong></summary>
  <p>Region: An independent collection of AWS resources in a defined geography. A collection of Data centers (Availability zones). All availability zones in a region connected by high bandwidth. Availability Zones: An Availability zone is a simply a data center. Designed as independent failure zone. High speed connectivity, Low latency. Edge Locations: Edge location are the important part of AWS Infrastructure. Edge locations are CDN endpoints for cloud front to deliver content to end user with low latency</p>
</details>

<details>
  <summary><strong>Q115) How to access AWS Platform?</strong></summary>
  <p>AWS Console AWS CLI (Command line interface) AWS SDK (Software Development Kit)</p>
</details>

<details>
  <summary><strong>Q116) What are the pricing models available in AWS EC2?</strong></summary>
  <p>On-Demand Instances Reserved Instances Spot Instances Dedicated Host</p>
</details>

<details>
  <summary><strong>Q117) What are the types using in AWS EC2?</strong></summary>
  <p>General Purpose Compute Optimized Memory optimized Storage Optimized Accelerated Computing (GPU Based)</p>
</details>

<details>
  <summary><strong>Q118) What is AMI? What are the types in AMI?</strong></summary>
  <p>Amazon machine image is a special type of virtual appliance that is used to create a virtual machine within the amazon Elastic compute cloud. AMI defines the initial software that will be in an instance when it is launched. Types of AMI: Published by AWS AWS Marketplace Generated from existing instances Uploaded virtual server</p>
</details>

<details>
  <summary><strong>Q119) How to Addressing AWS EC2 instances?</strong></summary>
  <p>Public Domain name system (DNS) name: When you launch an instance AWS creates a DNS name that can be used to access the Public IP: A launched instance may also have a public ip address This IP address assigned from the address reserved by AWS and cannot be specified. Elastic IP: An Elastic IP Address is an address unique on the internet that you reserve independently and associate with Amazon EC2 instance. This IP Address persists until the customer release it and is not tried to</p>
</details>

<details>
  <summary><strong>Q120) What is Security Group?</strong></summary>
  <p>AWS allows you to control traffic in and out of your instance through virtual firewall called Security groups. Security groups allow you to control traffic based on port, protocol and source/Destination.</p>
</details>

<details>
  <summary><strong>Q121) When your instance show retired state?</strong></summary>
  <p>Retired state only available in Reserved instances. Once the reserved instance reserving time (1 yr/3 yr) ends it shows Retired state.</p>
</details>

