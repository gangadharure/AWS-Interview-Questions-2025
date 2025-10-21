
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

