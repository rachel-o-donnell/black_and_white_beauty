# **BLACK & WHITE BEAUTY**

![amiresponsive mock-ups of Black & White Beauty](./documentation/responsiveness/)

### LIVE WEBSITE: **[Link to the Deployed Site](https://black-and-white-beauty.herokuapp.com/)**

__![GitHub last commit](https://img.shields.io/github/last-commit/rachel-o-donnell/black_and_white_beauty?color=fuschia&style=for-the-badge)__
__![GitHub contributors](https://img.shields.io/github/contributors/rachel-o-donnell/black_and_white_beauty?color=purple&style=for-the-badge)__
__![GitHub language count](https://img.shields.io/github/languages/count/rachel-o-donnell/black_and_white_beauty?color=blue&style=for-the-badge)__
__![GitHub top language](https://img.shields.io/github/languages/top/rachel-o-donnell/black_and_white_beauty?color=yellow&style=for-the-badge)__

*** A NOTE ON THE 2nd contributor:
Neil McEwwn (Code Institute) who had to change my files to adapt to a crossover from Gitpod to CodeAnywhere - I had originally done the change myself and he confirmed I had everything in place and did it correctly but it wasn't working. He redid the process requested a pull request and I accepted the change. In the end I reverted all these changes as CodeAnywhere was rife with issues and I had lost too much time already so went back to Gitpod. 

# Project Overview

Black & White Beauty is a fictitious e-commerce full stack project built using Django, Python, JavaScript and Bootstrap 4. The site is deployed to Heroku, uses Amazon S3 for cloud storage and Stripe for payment processing. Black & White Beauty is a business to consumer online retailer of black and white illustrations.

<br/>

---

**TABLE OF CONTENTS**


- [Introduction](#introduction)
- [UX](#ux)
  - [Strategy](#strategy)
  - [Marketing Strategy](#marketing-strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Agile](#agile)
  - [Epics](#epics)
  - [Sprints](#sprints)
- [Features](#features)
  - [Header](#header)
  - [Footer](#footer)
  - [Homepage](#homepage)
  - [Items](#Items)
  - [Item Details](#item-details)
  - [Commissions](#Commissions)
  - [Commission Details](#Commission-details)
  - [Cart](#cart)
  - [Checkout](#checkout)
  - [Order Confirmation / history](#order-confirmation--history)
  - [User Profiles](#user-profiles)
  - [Store Management](#Store-management)
  - [Reviews](#review-management)
  - [FAQ Management](#FAQ-management)
  - [Error Pages](#error-pages)
- [Marketing Strategy Implementation](#marketing-strategy-implementation)
  - [Branding](#branding)
  - [SEO](#seo)
  - [Keywords](#keywords)
  - [Newsletter](#newsletter)
  - [Social media](#social-media)
* [Future Development, Iteration and Implementation](#future-development-iteration-and-implementation)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks Used](#frameworks-used)
    * [Databases Used](#databases-used)
    * [Libraries and Packages Used](#libraries-and-packages-used)
    * [Programmes and Applications Used](#programmes-and-applications-used)
    * [Payment Processing Platform Used](#payment-processing-platform-used)
    * [Cloud Application Platforms Used](#cloud-platforms-used)
    * [Cloud Storage Services Used](#cloud-storage-services-used)
* [Testing](#testing)
* [Bugs, Issues and Solutions](#bugs-issues-and-solutions)
* [Deployment and Local Development](#deployment-and-local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [How to Fork](#how-to-fork)
        * [How to Clone](#how-to-clone)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

---

# **Future Development, Iteration and Implementation**
| **FOR FUTURE IMPLEMENTATION** |   |
| --- | --- |

---
# **TECHNOLOGIES USED**
## **Languages Used**
* [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
* [Python](https://www.python.org/) was used for the back end programming of the site.
## Frameworks Used
* [DJANGO - v3.2 ](https://docs.djangoproject.com/en/4.1/releases/3.2/) Django is a free and open-source, Python-based web  framework that follows the model–template–views architectural pattern.
* [Bootstrap4 - v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) was used as the frontend framework.
## Databases Used
* [DB.SQLITE3](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) was the database used for the project (development).
* [ElephantSQL](https://www.elephantsql.com/) ElephantSQL's Postgres as a Service was used to host the the database for the project (production).
## **Libraries and Packages Used**
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication.
* [JQuery - v3.5.1](https://jquery.com/) is a fast, small, and feature-rich JavaScript library.
* [Font Awesome Kit](https://fontawesome.com/v5/docs/web/setup/use-kit) is used for its icon toolkit.
* [django-countries, v7.2.1](https://pypi.org/project/django-countries/7.2.1/) was the Django application used to provide country choices for use with forms, and a country field for models.
* [django-crispy-forms, v1.14.0](https://pypi.org/project/django-crispy-forms/) was used to build programmatic reusable layouts out of form components.
* [gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server that allows us to run any Python application concurrently by running multiple processes within a single dyno
* [pillow](https://pypi.org/project/Pillow/) - a required Python imaging library used to enable handling of images.
* [psycopg2](https://pypi.org/project/psycopg2/) - a postgresql database adapter for python and used to connect with our postgres database
* [boto3==1.26.27](https://pypi.org/project/boto3/), [botocore==1.29.27] is an Amazon Web Services (AWS) software development kit (SDK) used to connect to the S3 bucket
* [pip](https://pip.pypa.io/en/stable/) is the package installer for Python, allowing us to install the packages we need for this site.
* [django storages](https://django-storages.readthedocs.io/en/latest/) - collection of custom storage backends for Django

## **Programmes and Applications Used**
* [Lucid Chart](https://www.lucidchart.com/pages/) was used to draw and build the Entity Relationship Diagram. It was also used to draw the User Flow Diagram.
* [favicon.io](https://favicon.io/) used to create the site's favicon
* [Git](https://git-scm.com/) used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.
* [GitHub](https://github.com/) is the project's git repository
* [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) used to track and integrate issues for Agile Development
* [Chrome DevTools](https://www.google.com/intl/en_uk/chrome/) - used for debugging, validation (Lighthouse) and taking fullscreen screenshots of the site
* [ezgif](https://ezgif.com/)


## **Payment Processing Platform Used**
* [Stripe](https://stripe.com/gb) was used to test and implement the payment processing for the site.

Stripe how to test cards interactively:
| **CARD NUMBER** | **MM &amp; YY**  | **CVC** | **SIMULATED PAYMENT RESULT** |
| --- | --- | --- | --- |
| 4242 4242 4242 4242 | use any valid future month and year | use any three digit CVC | successful payment |
| 4000 0000 0000 0002 | use any valid future month and year | use any three digit CVC | generic decline |

## **Cloud Application Platforms Used**
* [Heroku](https://devcenter.heroku.com/) was used for hosting and deployment of the live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

## **Cloud Storage Services Used**
* [AWS S3](https://aws.amazon.com/) was used to store the images and static files.
---

# **TESTING**
Please refer to [TESTING.md](./TESTING.md) file for:
* Manual Testing and Results
* Validation of all languages
* Lighthouse scores

<br/>

---
# **BUGS, ISSUES AND SOLUTIONS**
Please also refer to [TESTING.md](./TESTING.md) file for:
* Solutions to bugs found during testing and development phase
* Known bugs
<br/>

---
# **DEPLOYMENT**
Please refer to [DEPLOYMENT.md](./DEPLOYMENT.md) file for:
* Creating the database to be used in production
    * Instructions to common question: *"What if you didn't use fixtures in your project?"*
* Deploying to Heroku
* Setting up AmazonS3 for hosting our static and media files
---

# **CREDITS**
## **Code** 

https://github.com/rachel-o-donnell/booutique-ado : The project very much got its start from Code Institutes walkthrough project

PROJECTS I looked through for inspiration and problem solving
https://github.com/rachel-o-donnell/rising-women
https://github.com/AliOKeeffe/PP5-Fresh-Nest
https://github.com/davidcalikes/sensical.ie
https://github.com/lucywoodman/the-chocolate-factory
https://github.com/JoyZadan/shop-kbeauty
https://github.com/Iris-Smok/JoyfulBookstore-PP5
https://github.com/rachel-o-donnell/the-witchs-cauldron

README structure and deployment steps are from
https://github.com/JoyZadan/shop-kbeauty

editing commit messages
https://linuxhint.com/remove-committed-file-after-push-in-git/#:~:text=Display%20the%20existing%20content%20of,file%20from%20the%20local%20repository.
https://stackabuse.com/git-revert-to-a-previous-commit/

10 minute mail
https://10minutemail.com/

https://iwt.ie/


## **Content**


The policies were generated from:
* [Privacy Policy Generator ](https://www.privacypolicygenerator.info/download.php?lang=en&token=2YTFAh7Aa8GDO5knKT5gJ2WAr7mS9EG2)


## **Media**
* All images used in the site are my own drawings

## **Other Resources**
These other resources were used for research and/or for finding solutions when I got stuck.
1. [Stack Overflow](https://stackoverflow.com/)

---

# **ACKNOWLEDGEMENTS**