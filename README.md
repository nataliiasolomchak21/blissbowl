# BlissBowl Website

The BlissBowl Website represents a comprehensive full-stack application skillfully developed with a blend of HTML, CSS, JavaScript, Python, Django, Stripe, and Bootstrap technologies. This dynamic platform is designed to function as a delivery service, showcasing an extensive array of food bowls categorized to cater to diverse culinary preferences. Users can explore a wide range of delectable options, each thoughtfully curated and presented through an intuitive and user-friendly interface. 

View the live project [here](https://moviegeek-booking-1c00719de368.herokuapp.com/)

![Am I Responsive](documentation/readme_files/am-i-responsive.png)

## Table of Contents

- [UX](#ux)
    - [Target Audience](#target-audience)
    - [Key Project Goals](#key-project-goals)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
- [UI](#ui)
    - [Initial Design](#initial-design)
    - [Colour Palette](#colour-palette)
    - [Typography](#typography)
- [ERD (Entity-Relationship Diagram)](#erd-entity-relationship-diagram)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Ecommerce Business Model](#ecommerce-business-model)
- [Search Engine Optimization (SEO) & Social Media Marketing](#search-engine-optimization-seo--social-media-marketing)
    - [Keywords](#keywords)
    - [Sitemap](#sitemap)
    - [Robots](#robots)
    - [Social Media Marketing](#social-media-marketing)
    - [Newsletter Marketing](#newsletter-marketing)
- [Deployment](#deployment)
    - [Database (ElephangSQL)](#database-elephangsql)
    - [Django secret key](#django-secret-key)
    - [AWS](#aws)
    - [Stripe API](#stripe-api)
    - [Gmail API](#gmail-api)
    - [Heroku](#heroku)
    - [Final Deployment](#final-deployment)
    - [How to Fork the Github Repository](#how-to-fork-the-github-repository)
    - [How to Clone the Github Repository](#how-to-clone-the-github-repository)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
- [Acknowledgements](#acknowledgements)

## UX

### Target Audience

- Busy professionals who want easy and tasty meals.
- Students looking for quick and diverse dining options.
- Families seeking hassle-free and nutritious meal choices.
- Health-conscious individuals interested in balanced and customizable food bowls.

### Key Project Goals

1. **User-Friendly Interface:**
   - Develop an intuitive and visually appealing interface for seamless navigation.

2. **Diverse Food Bowl Menu:**
   - Curate an extensive menu with varied options, including vegetarian and protein-rich choices.

3. **Secure Online Transactions:**
   - Implement a secure payment processing system using the Stripe platform for reliable and safe online transactions.

4. **Responsive Design:**
   - Ensure a responsive design that adapts to various devices for enhanced accessibility.

5. **Feedback and Reviews:**
   - Implement a feedback and review system to gather user opinions and improve overall service.


### User Stories

#### Site-visitor

> *"As a visitor, I can sign up for an account so that I can access personalized features"*
>
> *"As a visitor I can navigate easily through the website using a header and footer so that I can have a seamless browsing experience"*
>
> *"As a user I can see a home page with featured products, categories, comments and newsletter so that I can discover new and exciting items"*
>

#### Site-user

> *"As a registered user, I can log in to my account so that I can access my profile"*
>
> *"As a logged-in user I can log out of my account so that I can end my session."*
>
> *"As a user I can reset my password in case I forget it so that I can regain access to my account"*
>
> *"As a registered user I can have a profile page with sections for personal information, order history, and a favorites list so that I can manage my account effectively"*
>
> *"As a registered user I can update my personal information on my profile so that my account details are always accurate"*
>
> *"As a registered user I can maintain a list of favorite products so that I can easily access and track items I'm interested in"*
>
> *"As a registered user I can view my order history so that I can track and review my past purchases"*
>
> *"As a user I can fill out the contact form and send a message so that I can communicate with the site administrators"*
>
> *"As a user I can subscribe to the newsletter so that I can receive updates and promotions"*
>
> *"As a user I can leave comments under a certain product so that I can share my thoughts about a particular products"*
>
> *"As a user I can access and review the privacy policy of the website so that I can understand how my personal information is handled"*
>

#### Site-shopper

> *"As a shopper I can search for a product by name or description easily so that I can find specific items quickly"*
>
> *"As a shopper I can view a list of products and product details so that I can make a purchase"*
>
> *"As a shopper I can view product categories so that I can explore items based on my preferences"*
>
> *"As a shopper I can easily select the quantity of a product when purchasing it so that I can control my order details"*
>
> *"As a shopper, I can add items to cart, view items in my cart and adjust the quantity before checkout so that I can review and modify my order"*
>
> *"As a shopper I can see the total price for the items and enter payment information securely during checkout so that I can make a purchase"*
>
> *"As a shopper I can view an order confirmation after completing the checkout process so that I can have a summary of my purchase"*
>
> *"As a shopper I can receive an email confirmation after checking out so that I have a record of my purchase"*
>

#### Site-admin

> *"As a site admin I can add products to the catalog so that I can expand and update the product offerings"*
>
> *"As a site admin I can edit/update existing products on the webiste so that I can keep product information accurate"*
>
> *"As a site admin I can delete products from the catalog so that I can manage the product offerings effectively"*
>
> *"As a site admin I can make the website SEO-optimized so that it ranks higher in search engine results"*
>
> *"As a site admin I can implement Facebook marketing strategies so that the website gains visibility and attracts more users"*
>

### Agile Methodology

#### Kanban Board

#### Iterations

#### Issues

#### Labels, Issues and MoSCoW prioritization

#### Story Points

#### Won't Have For This Deployment

## UI

### Initial Design

### Colour Palette

### Typography

## ERD (Entity-Relationship Diagram)

## Features

### Existing Features

### Features Left to Implement

## Technologies Used

## Ecommerce Business Model

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

### Sitemap

### Robots

### Social Media Marketing

### Newsletter Marketing

## Testing

All the information on testing is in [TESTING.md](TESTING.md)

## Deployment

### Database (ElephangSQL)

1. Navitate to [ElephantSQL website](https://www.elephantsql.com/), log in to your account
2. Click “Create New Instance”.
3. Enter database name, leave plan field as it is. You can leave the Tags field blank.
4. Select region, click on "Review".
5. Check that your details are correct. Then click “Create instance”
6. Return to the ElephantSQL dashboard and click on the database instance name for this project.
7. Copy your ElephantSQL database URL using the Copy.
8. Paste this URL into env.py file as DATABASE_URL value and save the file.

```
os.environ["DATABASE_URL"] = "postgres://yourdatabaseURL"
```

### Django secret key

You need to include you Django secret key that you can generate using any of the Django secret keys generators online.
In order to protect django app secret key it was set as an enviroment variable and stored in env.py.

```
os.environ["SECRET_KEY"] = "yourSecretKey"
```

### AWS

### Stripe API

### Gmail API 

### Heroku

1. Log in to Heroku or create an account.
2. Navigate to your Heroku dashboard, click "New" and select "Create new app".
3. Enter a name for your app (can be a name of your project) and choose the region that suits best to your location.
4. Select "Settings" from the tabs.
5. Click "Reveal Config Vars".
6. These are:
```
CLOUDINARY_API_KEY - Get from Cloudinary.
DATABASE_URL - Get from your SQL provider.
DISABLE_COLLECTSTATIC - Set to '1' (without '')
SECRET_KEY - This is your Django project secret key, generated by your Django project. You can generate a new key that is different from your localhost version. You can also add any other Config Vars you need.
```
* Heroku needs two additional files in order to deploy properly.
    * requirements.txt
    * Procfile
7. Select "Deploy" from the tabs.
8. Select "GitHub - Connect to GitHub" from deployment methods.
9. Click "Connect to GitHub" in the created section.
10. Search for the GitHub repository by name.
11. Click to 'Connect' to the relevant repo.
12. Either click ‘Enable Automatic Deploys’ for automatic deploys or ‘Deploy Branch’ to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
13. Click 'View' to view the deployed site.


### Final Deployment

### How to Fork the Github Repository

### How to Clone the Github Repository

## Credits

### Content

### Media

### Code

## Acknowledgements

