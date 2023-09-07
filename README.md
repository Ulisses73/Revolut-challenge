# Revolut-challenge

## Application usage:

Used with Python3:

Run the application: python3 app.py

By default, it will run on port 5000

To add data for the application:

```curl -X PUT -H "Content-Type: application/json" -d '{"dateOfBirth": "1990-09-16"}' http://localhost:5000/hello/test```

To get the data you can do:

```curl localhost:5000/hello/test ```


## Diagram explanation:

Internet: The external world connects to the application through the internet.

Amazon Route 53: Used to route incoming requests to the appropriate load balancer (if used) or directly to the EC2 instances hosting the Flask application.

Load Balancer: To handle high traffic or ensure high availability, becauseit will  distribute incoming requests across multiple EC2 instances.

Amazon EC2: Virtual machines running the Flask application code. They are hosted within a Virtual Private Cloud (VPC) for network isolation and security.

Amazon RDS: Hosts the database used by the application to store user data.

Amazon CloudWatch: Monitor and log application and server metrics for performance and debugging.

## Scripts for building and no-downtime production:

### Scripts:

setup.sh - set up the necessary environment variables, configurations, and dependencies.

deploy.sh - ensure zero-downtime deployments using blue-green deployment or rolling deployments.

### Other SRE practices

- Set up a CI/CD pipeline using a tool like Jenkins or GitLab CI/CD. It should include the following stages: build, test, deploy to staging, automated test in staging, manual test in staging and Production deployment.
- Backup and restore scripts. Automate regular database backups to a secure location (e.g., Amazon S3), for example using RDS settings, which could then be used to restore the database.
- Monitoring and Alerting: using tools like Prometheus, Grafana, or AWS CloudWatch to track system health and performance. Define alerting thresholds for key metrics.
- High Availability Database: for production, using a managed high-availability database solution like Amazon RDS Multi-AZ.
