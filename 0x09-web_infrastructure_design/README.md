# 0-Simple web stack

- A server is a computer that provides services or resources to other computers over
the internet.
- The role of the domain name is to make it easier for users to access the website, by using a human-readable name instead of an IP address.
- CNAME
- the role of the web server is to receive requests from browser, and send back responses.
- run the application code.
-  the role of database is to store and retrieve data.
- HTTP
- SPOF (single point of fail): means if a single component fails, the whole system fails.
- Downtime: means that the user will not be able to access the server during that period.
- If the website receives more requests than the server can handle, the performance and the reliability of the website will degrade, and users may experience slow loading, errors, or timeouts.


# 1. Distributed web infrastructure

- The **load balancer** is an additional element that distributes incoming requests among multiple servers, improving the availability and performance of the website.
- The **web server** is an additional element that handles HTTP requests from the load balancer and serves static content, such as images, CSS, and JavaScript files. 
- The **application server** is an additional element that hosts the web application code and processes dynamic requests from the web server.
- The **database** is an additional element that stores and manages the structured data for the web application
-  The **primary node** is the main source of data and handles all write operations, while the **replica node** is a secondary source of data that is kept in sync with the primary node and handles read operations. 
- The difference between the primary node and the replica node in regard to the application is that the application server can only write data to the primary node, but can read data from either node.
- here are several components that are SPOF, such as the load balancer, the application server, and the primary node of the database. If any of these components goes down for any reason, such as hardware failure, power outage, network outage, etc., the website will be unavailable or partially unavailable.
- Security issues: Without a firewall and HTTPS, the infrastructure is vulnerable to various security threats, such as denial-of-service attacks, man-in-the-middle attacks, data breaches, etc.
- No monitoring: There is no monitoring system in this infrastructure, which means that there is no way to collect, analyze, or visualize the data about the performance, availability, or health of the components


# 2. Secured and monitored web infrastructure

- The **three firewalls** are additional elements that provide security for the network by filtering the traffic based on predefined rules or policies.
- The **SSL certificate** is an additional element that provides encryption and authentication for the website.
- The **monitoring client** is an additional element that collects and sends data about the performance, availability, or health of the components to a monitoring service, such as Sumologic or other monitoring services. Monitoring is used to detect and resolve issues, optimize the resource utilization, and ensure the quality of service.
- The monitoring tool is collecting data by using **metrics**, which are numerical measurements that represent the state or behavior of a component.
- The issues with this infrastructure are:
    - **Terminating SSL at the load balancer level** is an issue because it creates a single point of failure and reduces the overall security of the infrastructure. 
    - **Having only one MySQL server capable of accepting writes** is an issue because it creates a single point of failure and limits the scalability of the database.
    - **Having servers with all the same components** (database, web server and application server) is an issue because it reduces the isolation and flexibility of the components.


