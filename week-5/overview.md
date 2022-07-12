
# Infrastructure as Code (IaC)

Building infrastructure manually is tedious and error-prone. As developers, we should strive to simplify and modularize
the environments that we deploy. The same way we develop our software to be modular, so too should our systems.

## Why care?

Developers are commonly asked:

- Build a range
- Deploy a test host
- Perform load tests
- Scale X application

We should be able to answer these asks in a simple way - with code.

Also, dramatically simplifies your life.

## Nuts and bolts

There are countless software suites for maintain IaC deployments, some common ones are:

- Terraform
- Ansible
- Vagrant
- AWS CloudFormation
- Puppet
- Chef

## Examples

We will do a simple single host deployment on an existing VPC and subnet, using an existing Key Pair.

## Complicated Examples

Paved Roads for Prelude systems deployments:

- https://github.com/preludeorg/systems/tree/master/paved-roads

## References

- Paved Road security at Netflix (https://medium.com/@NetflixTechBlog/scaling-appsec-at-netflix-6a13d7ab6043)
- Example CloudFormation template doc (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)