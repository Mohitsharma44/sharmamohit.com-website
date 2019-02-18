# sharmamohit.com-website

personal website hosted using AWS S3 at https://sharmamohit.com

###### Status:
![Website Status](https://img.shields.io/website-up-down-green-red/https/sharmamohit.com.svg?style=flat)
![Website Uptime](https://img.shields.io/uptimerobot/ratio/m781993530-436682a6e42e6d3bc06223b8.svg?label=Uptime&logo=clockify&style=flat)
![Travis Status](https://img.shields.io/travis/Mohitsharma44/sharmamohit.com-website.svg?label=TravisCI&logo=travis&style=flat)

### Structure

The landing page on my website is a single index page in [`resume/index.html`](./resume)

The `/work/` slug is a portfolio website created using gohugo and Academic theme.

### Building

The website is built and deployed automatically by TravisCI to AWS S3 bucket when a commit is pushed to the master branch. The script for travis primarily consists
of building the hugo website to `public` directory, then copying the contents from `resume` to public and finally
pushing the public directory to S3 bucket.

### Cloudfront Invalidation

After the above deployment (upload to s3 bucket) travis will also initiate forced cloufront invalidation.

> Sure I don't need to invalidate all objects but hey, its so cheap..
