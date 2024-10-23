---
# An instance of the Experience widget.
# Documentation: https://sourcethemes.com/academic/docs/page-builder/
widget: experience

# Activate this widget? true/false
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 40

title: Experience
subtitle:

# Date format
#   Refer to https://sourcethemes.com/academic/docs/customization/#date-format
date_format: Jan 2006

# Experiences.
#   Add/remove as many `experience` blocks below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   You can begin a multiline `description` using YAML's `|-`.
experience:
- company: Angi
  company_url: "https://angi.com"
  date_end: ""
  date_start: "2023-09-11"
  description: |-
    * Angi One
      <br/><br/>
      * Collaborated with cross-functional teams to build key components of the Angi One platform using Kubernetes controllers, Flux, and ArgoCD, enabling single-manifest deployments for applications and cloud services, reducing developer overhead and cutting production time by 50%.
      * Led efforts to automate documentation workflows based on CRDs, ensuring up-to-date documentation with every release, reducing manual effort and support inquiries.
      * Partnering with development and observability teams to enhance and automate component generation in the Backstage catalog, streamlining the onboarding process and improving system visibility.
  location: Remote
  title: |-
    * Senior Infrastructure Engineer
- company: Workday
  company_url: "https://workday.com"
  date_end: "2023-09-08"
  date_start: "2019-05-20"
  description: |-
    * Development and Operations
      <br/><br/>
      * Implemented policy-based infrastructure management using OPA and Atlantis improving developer experience while providing them more control over their resources and helping them shift security best practices to the left.
      * Mentored developers and junior engineers as they grow into their role.
      * Created an automated AWS deployment pipeline to deploy microservice application cross account and cross region;
      reducing operations toil by 4 hours every week.
      * Actively manage, improve, and monitor infrastructure resources in DC and on AWS including but not limited to
        EC2, ECS, Route53, S3, RDS, Lambda, ES etc. using tools like terraform, wavefront, ELK stack and slack.
      * Introduced team to using policies (OPA) for managing infrastructure giving developers more control over their cloud resources.
      * Writing ansible roles to help manage the hosts and perform application deployment.
      * Writing Jenkinsfiles and improving shared libraries for automated build and deployment of several applications and services using Jenkins.
      * Migrating application services to an in-house flavor of Kubernetes platform.
    * Knowledge Share
      <br/><br/>
      * Spearheaded an initiative between Ops and multiple dev teams to empower the developers with the knowledge
    they would need to take ownership of their services.
    * Scrum Master
      <br/><br/>
      * Helped team self organize and self manage by incorporating servant leadership principles.
  location: Victoria, BC, Canada
  title: |- 
    * Senior Software Development Engineer, DevOps
    * Software Development Engineer III, DevOps
    * Software Development Engineer II, DevOps
- company: NYU CUSP
  company_url: "https://cusp.nyu.edu"
  date_end: "2019-05-14"
  date_start: "2014-06-01"
  description: |-
    * Developed a scalable and secure container scheduling and monitoring infrastructure (PAAS)
    * Architected the NYU/CUSP Urban Observatory’s multi-site physical infrastructure (Distributed Systems, Networking)
    * Developed a secure machine critical IoT platform and implemented a CI/CD framework for deploying and
      maintaining over 100 urban noise monitoring sensors in NYC (CI/CD, IoT)
  location: New York City, NY, USA
  title: |-
    * Associate Research Scientist
    * Assistant Research Scientist
---
