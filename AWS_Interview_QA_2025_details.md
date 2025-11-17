
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

<details>
  <summary><strong>Q122) instance stop and start. What is the reason for that and explain solution?</strong></summary>
  <p>AWSassignedPublicIPautomaticallybutitschangedynathatcaseweneedtoassignElasticIPforthatinstance , onceassi automatically.</p>
</details>

<details>
  <summary><strong>Q123) What is Elastic Beanstalk?</strong></summary>
  <p>AWS Elastic Beanstalk is the fastest and simplest way to get an application up and running on AWS.Developers can simply upload their code and the service automatically handle all the details such as resource provisioning, load balancing, Auto scaling and Monitoring.</p>
</details>

<details>
  <summary><strong>Q124) What is Amazon Lightsail?</strong></summary>
  <p>Lightsail designed to be the easiest way to launch and manage a virtual private server with AWS.Lightsail plans include everything you need to jumpstart your project a virtual machine, ssd based storage, data transfer, DNS Management and a static ip.</p>
</details>

<details>
  <summary><strong>Q125) What is EBS?</strong></summary>
  <p>Amazon EBS Provides persistent block level storage volumes for use with Amazon EC2 instances. Amazon EBS volume is automatically replicated with its availability zone to protect component failure offering high availability and durability. Amazon EBS volumes are available in a variety of types that differ in performance characteristics and Price.</p>
</details>

<details>
  <summary><strong>Q126) How to compare EBS Volumes?</strong></summary>
  <p>Magnetic Volume: Magnetic volumes have the lowest performance characteristics of all Amazon EBS volume types. EBS Volume size: 1 GB to 1 TB Average IOPS: 100 IOPS Maximum throughput: 40-90 MB General-Purpose SSD: General purpose SSD volumes offers cost-effective storage that is ideal for a broad range of workloads. General purpose SSD volumes are billed based on the amount of data space provisioned regardless of how much of data you actually store on the volume. EBS Volume size: 1 GB to 16 TB Maximum IOPS: upto 10000 IOPS Maximum throughput: 160 MB Provisioned IOPS SSD: Provisioned IOPS SSD volumes are designed to meet the needs of I/O intensive workloads, particularly database workloads that are sensitive to storage performance and consistency in random access I/O throughput. Provisioned IOPS SSD Volumes provide predictable, High performance. EBS Volume size: 4 GB to 16 TB Maximum IOPS: upto 20000 IOPS Maximum throughput: 320 MB</p>
</details>

<details>
  <summary><strong>Q127) What is cold HDD and Throughput-optimized HDD?</strong></summary>
  <p>Cold HDD: Cold HDD volumes are designed for less frequently accessed workloads. These volumes are significantly less expensive than throughput-optimized HDD volumes. EBS Volume size: 500 GB to 16 TB Maximum IOPS: 200 IOPS Maximum throughput: 250 MB Throughput-Optimized HDD: Throughput-optimized HDD volumes are low cost HDD volumes designed for frequent access, throughput-intensive workloads such as big data, data warehouse. EBS Volume size: 500 GB to 16 TB Maximum IOPS: 500 IOPS Maximum throughput: 500 MB</p>
</details>

<details>
  <summary><strong>Q128) What is Amazon EBS-Optimized instances?</strong></summary>
  <p>Amazon EBS optimized instances to ensure that the Amazon EC2 instance is prepared to take advantage of the I/O of the Amazon EBS Volume. An amazon EBS-optimized instance uses an optimized configuration stack and provide additional dedicated capacity for Amazon EBS I/When you select Amazon EBS-optimized for an instance you pay an additional hourly charge for that instance.</p>
</details>

<details>
  <summary><strong>Q129) What is EBS Snapshot?</strong></summary>
  <p>It can back up the data on the EBS Volume. Snapshots are incremental backups. If this is your first snapshot it may take some time to create. Snapshots are point in time copies of volumes.</p>
</details>

<details>
  <summary><strong>Q130) How to connect EBS volume to multiple instance?</strong></summary>
  <p>WecantabletoconnectEBSvolumetomultipleinstance multiple EBS Volume to single instance.</p>
</details>

<details>
  <summary><strong>Q131) What are the virtualization types available in AWS?</strong></summary>
  <p>Hardware assisted Virtualization: HVM instances are presented with a fully virtualized set of hardware and they executing boot by executing master boot record of the root block device of the image. It is default Virtualization. Para virtualization: This AMI boot with a special boot loader called PV-GRUB. The ability of the guest kernel to communicate directly with the hypervisor results in greater performance levels than other virtualization approaches but they cannot take advantage of hardware extensions such as networking, GPU etc. Its customized Virtualization image. Virtualization image can be used only for particular service.</p>
</details>

<details>
  <summary><strong>Q132) Differentiate Block storage and File storage?</strong></summary>
  <p>Block Storage: Block storage operates at lower level, raw storage device level and manages data as a set of numbered, fixed size blocks. File Storage: File storage operates at a higher level, the operating system level and manage data as a named hierarchy of files and folders.</p>
</details>

<details>
  <summary><strong>Q133) What are the advantage and disadvantage of EFS? Advantages:</strong></summary>
  <p>Fully managed service File system grows and shrinks automatically to petabytes Can support thousands of concurrent connections Multi AZ replication Throughput scales automatically to ensure consistent low latency Disadvantages: Not available in all region Cross region capability not available More complicated to provision compared to S3 and EBS</p>
</details>

<details>
  <summary><strong>Q134) what are the things we need to remember while creating s3 bucket?</strong></summary>
  <p>Amazon S3 and Bucket names are This means bucket names must be unique across all AWS Bucket names can contain upto 63 lowercase letters, numbers, hyphens and You can create and use multiple buckets You can have upto 100 per account by</p>
</details>

<details>
  <summary><strong>Q135) What are the storage class available in Amazon s3?</strong></summary>
  <p>Amazon S3 Standard Amazon S3 Standard-Infrequent Access Amazon S3 Reduced Redundancy Storage Amazon Glacier Get AWS Online Training</p>
</details>

<details>
  <summary><strong>Q136) Explain Amazon s3 lifecycle rules?</strong></summary>
  <p>Amazon S3 lifecycle configuration rules, you can significantly reduce your storage costs by automatically transitioning data from one storage class to another or even automatically delete data after a period of time. Store backup data initially in Amazon S3 Standard After 30 days, transition to Amazon Standard IA After 90 days, transition to Amazon Glacier After 3 years, delete</p>
</details>

<details>
  <summary><strong>Q137) What is the relation between Amazon S3 and AWS KMS?</strong></summary>
  <p>To encrypt Amazon S3 data at rest, you can use several variations of Server-Side Encryption. Amazon S3 encrypts your data at the object level as it writes it to disks in its data centersanddecryptitforyouwhenyouaccessitllSSEperformed Management Service (AWS KMS) uses the 256-bit Advanced Encryption Standard (AES).</p>
</details>

<details>
  <summary><strong>Q138) What is the function of cross region replication in Amazon S3?</strong></summary>
  <p>Cross region replication is a feature allows you asynchronously replicate all new objects in the source bucket in one AWS region to a target bucket in another region. To enable cross-region replication, versioning must be turned on for both source and destination buckets. Cross region replication is commonly used to reduce the latency required to access objects in Amazon S3</p>
</details>

<details>
  <summary><strong>Q139) How to create Encrypted EBS volume?</strong></summary>
  <p>You need to select Encrypt this volume option in Volume creation page. While creation a new master key will be created unless you select a master key that you created separately in the service. Amazon uses the AWS key management service (KMS) to handle key management.</p>
</details>

<details>
  <summary><strong>Q140) Explain stateful and Stateless firewall.</strong></summary>
  <p>Stateful Firewall: A Security group is a virtual stateful firewall that controls inbound and outbound network traffic to AWS resources and Amazon EC2 instances. Operates at the instance level. It supports allow rules only. Return traffic is automatically allowed, regardless of any rules. Stateless Firewall: A Network access control List (ACL) is a virtual stateless firewall on a subnet level. Supports allow rules and deny rules. Return traffic must be explicitly allowed by rules.</p>
</details>

<details>
  <summary><strong>Q141) What is NAT Instance and NAT Gateway?</strong></summary>
  <p>NAT instance: A network address translation (NAT) instance is an Amazon Linux machine Image (AMI) that is designed to accept traffic from instances within a private subnet, translate the source IP address to the Public IP address of the NAT instance and forward the traffic to IWG. NAT Gateway: A NAT gateway is an Amazon managed resources that is designed to operate just like a NAT instance but it is simpler to manage and highly available within an availability Zone. To allow instance within a private subnet to access internet resources through the IGW via a NAT gateway.</p>
</details>

<details>
  <summary><strong>Q142) What is VPC Peering?</strong></summary>
  <p>AmazonVPCpeeringconnectionisanetworkingconnectio that enables instances in either Amazon VPC to communicate with each other as if they are within the same network. You can create amazon VPC peering connection between your own Amazon</p>
</details>

<details>
  <summary><strong>Q143) VPCsorAmazonVPCinanotherAWSaccountwithinasingleregio Q147) What is MFA in AWS?</strong></summary>
  <p>Multi factor Authentication can add an extra layer of security to your infrastructure by adding a second method of authentication beyond just password or access key.</p>
</details>

<details>
  <summary><strong>Q144) What are the Authentication in AWS?</strong></summary>
  <p>User Name/Password Access Key Access Key/ Session Token</p>
</details>

<details>
  <summary><strong>Q145) What is mean by Multi-AZ in RDS?</strong></summary>
  <p>Multi AZ allows you to place a secondary copy of your database in another availability zone for disaster recovery purpose. Multi AZ deployments are available for all types of Amazon RDS Database engines. When you create s Multi-AZ DB instance a primary instance is created in one Availability Zone and a secondary instance is created by another Availability zone.</p>
</details>

<details>
  <summary><strong>Q146) What is Amazon Dynamo DB?</strong></summary>
  <p>Amazon Dynamo DB is fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. Dynamo DB makes it simple and Cost effective to store and retrieve any amount of data.</p>
</details>

<details>
  <summary><strong>Q147) What is cloud formation?</strong></summary>
  <p>Cloud formation is a service which creates the AWS infrastructure using code. It helps to reduce time to manage resources. We can able to create our resources Quickly and faster.</p>
</details>

<details>
  <summary><strong>Q148) How to plan Auto scaling?</strong></summary>
  <p>Manual Scaling Scheduled Scaling Dynamic Scaling</p>
</details>

<details>
  <summary><strong>Q149) What is Auto Scaling group?</strong></summary>
  <p>Auto Scaling group is a collection of Amazon EC2 instances managed by the Auto scaling service. Each auto scaling group contains configuration options that control when auto scaling should launch new instance or terminate existing instance.</p>
</details>

<details>
  <summary><strong>Q150) Differentiate Basic and Detailed monitoring in cloud watch?</strong></summary>
  <p>Basic Monitoring: Basic monitoring sends data points to Amazon cloud watch every five minutes for a limited number of preselected metrics at no charge. Detailed Monitoring: Detailed monitoring sends data points to amazon CloudWatch every minute and allows data aggregation for an additional charge.</p>
</details>

<details>
  <summary><strong>Q151) What is the relationship between Route53 and Cloud front?</strong></summary>
  <p>In Cloud front we will deliver content to edge location wise so here we can use Route 53 for Content Delivery Network. Additionally, if you are using Amazon CloudFront you can configure Route 53 to route Internet traffic to those resources.</p>
</details>

<details>
  <summary><strong>Q152) What are the routing policies available in Amazon Route53?</strong></summary>
  <p>Simple Weighted Latency Based Failover Geolocation</p>
</details>

<details>
  <summary><strong>Q153) What is Amazon ElastiCache?</strong></summary>
  <p>Amazon ElastiCache is a web services that simplifies the setup and management of distributed in memory caching environment. Cost Effective High Performance Scalable Caching Environment Using Memcached or Redis Cache Engine</p>
</details>

<details>
  <summary><strong>Q154) What is SES, SQS and SNS?</strong></summary>
  <p>SES (Simple Email Service): SES is SMTP server provided by Amazon which is designed to send bulk mails to customers in a quick and cost-effective manner.SES does not allows to configure mail server. SQS (Simple Queue Service): SQS is a fast, reliable and scalable, fully managedmessagequeuingservice . AmazonSQSmakesitsimplean temporary repository for messages to waiting for processing and acts as a buffer between the component producer and the consumer. SNS (Simple Notification Service): SNS is a web service that coordinates and manages the delivery or sending of messages to recipients.</p>
</details>

<details>
  <summary><strong>Q155) How To Use Amazon Sqs? What Is Aws?</strong></summary>
  <p>Amazon Web Services is a secure cloud services stage, offering compute power, database storage, content delivery and other functionality to help industries scale and grow.</p>
</details>

<details>
  <summary><strong>Q156) What is the importance of buffer in AWS?</strong></summary>
  <p>lowpriceConsumeonlytheamountofcalculating , storag needed. No long-term assignation, minimum spend or up-front expenditure is required. Elastic andScalableQuicklyRiseanddecreaseresourcestoapplication and control costs. Avoid provisioning maintenance up-front for plans with variable consumption speeds or low lifetimes.</p>
</details>

<details>
  <summary><strong>Q157) What is the way to secure data for resounding in the cloud?</strong></summary>
  <p>Avoidstoragesensitivematerialinthecloud . & ReadtheusercontracttofindouthowyourcloudservicestorinBeseriousaboutpasswords . & Encrypt . & Use an encrypted cloud service.</p>
</details>

<details>
  <summary><strong>Q158) Name The Several Layers Of Cloud Computing?</strong></summary>
  <p>Cloud computing can be damaged up into three main services: Software-as-a-Service (SaaS), Infrastructure-as-a-Service (IaaS) and Platform-as-a-Service (PaaS). PaaS in the middle, and IaaS on the lowest</p>
</details>

<details>
  <summary><strong>Q159) What Is Lambda edge In Aws?</strong></summary>
  <p>Lambda Edge lets you run Lambda functions to modify satisfied that Cloud Front delivers, executing the functions in AWS locations closer to the viewer. The functions run in response to Cloud Front events, without provisioning or managing server.</p>
</details>

<details>
  <summary><strong>Q160) Distinguish Between Scalability And Flexibility?</strong></summary>
  <p>Cloud computing offers industries flexibility and scalability when it comes to computing needs: Flexibility . Cloudcomputingagreesyourworkerstobemoreflexi the workplace. Workers can access files using web-enabled devices such as smartphones, laptops and notebooks. In this way, cloud computing empowers the use of mobile technology. One of the key assistances of using cloud computing is its scalability. Cloud computing allows your business to easily expensive or downscale your IT requests as and when required. For example, most cloud service workers will allow you to increase your existing resources to accommodate increased business needs or changes. This will allow you to support your commercial growth without exclusive changes to your present IT systems.</p>
</details>

<details>
  <summary><strong>Q161) What is IaaS?</strong></summary>
  <p>IaaSisacloudservicethatrunsservicesonpay - for - what IaaS workers include Amazon Web Services, Microsoft Azure and Google Compute Engine Users: IT Administrators</p>
</details>

<details>
  <summary><strong>Q162) What is PaaS?</strong></summary>
  <p>PaaS runs cloud platforms and runtime environments to develop, test and manage software Users: Software Developers</p>
</details>

<details>
  <summary><strong>Q163) What is SaaS?</strong></summary>
  <p>In SaaS, cloud workers host and manage the software application on a pay-as-you-go pricing model Users: End Customers</p>
</details>

<details>
  <summary><strong>Q164) Which Automation Gears Can Help With Spinup Services?</strong></summary>
  <p>The API tools can be used for spin up services and also for the written scripts. Persons scripts could be coded in Perl, bash or other languages of your preference. There is one more option that is flowery management and stipulating tools such as a dummy or improved descendant. A tool called Scalar can also be used and finally we can go with a controlled explanation like a Right scale. Which automation gears can help with pinup service.</p>
</details>

<details>
  <summary><strong>Q165) What Is an Ami? How Do I Build One?</strong></summary>
  <p>An Amazon Machine Image (AMI) explains the programs and settings that will be applied when you launch an EC2 instance. Once you have finished organizing the data, services, and submissions on your ArcGIS Server instance, you can save your work as a custom AMI stored in Amazon EC2. You can scale out your site by using this institution AMI to launch added instances Use the following process to create your own AMI using the AWS Administration Console: *Configure an EC2 example and its attached EBS volumes in the exact way you want them created in the custom AMI. 1. Log out of your instance, but do not stop or terminate it. 2. Log in to the AWS Management Console, display the EC2 page for your region, then click Instances. 3. Choose the instance from which you want to create a custom AMI. 4. Click Actions and click Create Image. 5. Type a name for Image Name that is easily identifiable to you and, optionally, input text for Image Description. 6. Click Create Image. Read the message box that appears. To view the AMI standing, go to the AMIs page. Here you can see your AMI being created. It can take a though to create the AMI. Plan for at least 20 minutes, or</p>
</details>

<details>
  <summary><strong>Q166) slowerifyouveconnectedalotofadditionalapplicationsordata Q171) What Are The Main Features Of Amazon Cloud Front?</strong></summary>
  <p>Amazon Cloud Front is a web service that speeds up delivery of your static and dynamic web content, such as .html, .css, .js, and image files, to your users.CloudFront delivers your content through a universal network of data centers called edge locations</p>
</details>

<details>
  <summary><strong>Q167) What Are The Features Of The Amazon Ec2 Service?</strong></summary>
  <p>Amazon Elastic Calculate Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud calculating easier fordesigners . AmazonEC2ssimplewebserviceinterfaceallowsyo capacity with minimal friction.</p>
</details>

<details>
  <summary><strong>Q168) Explain Storage For Amazon Ec2 Instance.?</strong></summary>
  <p>An instance store is a provisional storing type located on disks that are physically attachedtoahostmachine . & Thisarticlewillpresentyoutothe type, compare it to AWS Elastic Block Storage (AWS EBS), and show you how to backup data stored on instance stores to AWS EBS Amazon SQS is a message queue service used by scattered requests to exchange messages through a polling model, and can be used to decouple sending and receiving components</p>
</details>

<details>
  <summary><strong>Q169) connectivity with external networks?</strong></summary>
  <p>Internet Gateway {IGW) Virtual Private Gateway (VGW)</p>
</details>

<details>
  <summary><strong>Q170) Which of the following are characteristics of Amazon VPC subnets?</strong></summary>
  <p>Each subnet maps to a single Availability Zone. By defaulting, all subnets can route between each other, whether they are private or public.</p>
</details>

<details>
  <summary><strong>Q171) How can you send request to Amazon S3?</strong></summary>
  <p>Every communication with Amazon S3 is either genuine or anonymous. Authentication is a process of validating the individuality of the requester trying to access an Amazon Web Services (AWS) product. Genuine requests must include a autograph value that authenticates the requestsender . Theautographvalueis , inpart , createdfromther (access key identification and secret access key).</p>
</details>

<details>
  <summary><strong>Q172) cloud ?</strong></summary>
  <p>Backup Data Locally. A standout amongst the most vital interesting points while overseeing information is to guarantee that you have reinforcements for your information, AvoidStoringSensitiveInformation . & UseCloudServicesthatEncryptData . & EncryptYourData . & InstallAnti - infectionSoftware . & MakePasswordsStronger . & Test the Security Measures in Place.</p>
</details>

<details>
  <summary><strong>Q173) What is AWS Certificate Manager ?</strong></summary>
  <p>AWS Certificate Manager is an administration that lets you effortlessly arrangement, oversee, and send open and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) endorsements for use with AWS administrations and your inward associated assets. SSL/TLS declarations are utilized to anchor arrange interchanges and set up the character of sites over the Internet and additionally assets on private systems. AWS Certificate Manager expels the tedious manual procedure of obtaining, transferring, and reestablishing SSL/TLS endorsements.</p>
</details>

<details>
  <summary><strong>Q174) What is the AWS Key Management Service</strong></summary>
  <p>AWS Key Management Service (AWS KMS) is an overseen benefit that makes it simple foryoutomakeandcontroltheencryptionkeysusedtoscramble is additionally coordinated with AWS CloudTrail to give encryption key use logs to help meet your inspecting, administrative and consistence needs.</p>
</details>

<details>
  <summary><strong>Q175) What is Amazon EMR ?</strong></summary>
  <p>Amazon Elastic MapReduce (EMR) is one such administration that gives completely oversaw facilitated Hadoop system over Amazon Elastic Compute Cloud (EC2).</p>
</details>

<details>
  <summary><strong>Q176) What is Amazon Kinesis Firehose ?</strong></summary>
  <p>Amazon Kinesis Data Firehose is the least demanding approach to dependably stack gushinginformationintoinformationstoresandexaminationdevic overseen benefit that consequently scales to coordinate the throughput of your information and requires no continuous organization</p>
</details>

<details>
  <summary><strong>Q177) What Is Amazon CloudSearch and its highlights ?</strong></summary>
  <p>Amazon CloudSearch is a versatile cloud-based hunt benefit that frames some portion of Amazon Web Services (AWS). CloudSearch is normally used to incorporate tweaked seek abilities into different applications. As indicated by Amazon, engineers can set a pursuit application up and send it completely in under 60 minutes.</p>
</details>

<details>
  <summary><strong>Q178) from a virtual private cloud?</strong></summary>
  <p>Amazon Virtual Private Cloud (Amazon VPC) empowers you to characterize a virtual system in your very own consistently disengaged zone inside the AWS cloud, known as a virtual private cloud (VPC). You can dispatch your Amazon EC2 assets, for example, occasions, into the subnets of your VPC. Your VPC nearly looks like a conventional system that you may work in your very own server farm, with the advantages of utilizing adaptable foundation from AWS. You can design your VPC; you can choose its IP address extend, make subnets, and arrange course tables, organize portals, and security settings. You can interface occurrences in your VPC to the web or to your own server farm</p>
</details>

