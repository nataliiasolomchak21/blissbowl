# BlissBowl Website

Back to [README](README.md)

## Testing Overview

## Table of Contents

- [User Story Tests](#user-story-tests)
- [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JS](#javascript)
    - [Python](#python)
- [Unit Testing](#unit-testing)
    - [Coverage](#coverage)
- [Error Handling](#error-handling)
- [Manual Testing](#manual-testing)
- [Lighthouse](#lighthouse)
- [Responsiveness](#responsiveness)
- [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
    - [Solved](#solved)
    - [Unsolved](#unsolved)

## User Story Tests

| User Story | Screenshot |
| --- | --- |
| *"As a visitor, I can sign up for an account so that I can access personalized features"*|![Design](documentation/readme_files/signup-feature.png)|
| *"As a visitor I can navigate easily through the website using a header and footer so that I can have a seamless browsing experience"*|![Design](documentation/readme_files/header-feature.png)|
| *"As a visitor I can navigate easily through the website using a header and footer so that I can have a seamless browsing experience"*|![User Story](documentation/readme_files/footer-feature.png)|
| *"As a user I can see a home page with featured products, categories, comments and newsletter so that I can discover new and exciting items"*|![User Story](documentation/testing_files/homepage-userstory.png)|
| *"As a registered user, I can log in to my account so that I can access my profile"*|![User Story](documentation/readme_files/login-feature.png)|
| *"As a logged-in user I can log out of my account so that I can end my session."*|![User Story](documentation/readme_files/logout-feature.png)|
| *"As a registered user I can have a profile page with sections for personal information, order history, and a favorites list so that I can manage my account effectively"*|![User Story](documentation/readme_files/profile-info-feature.png)|
| *"As a registered user I can view my order history so that I can track and review my past purchases"*|![User Story](documentation/readme_files/profile-order-history-feature.png)|
| *"As a registered user I can maintain a list of favorite products so that I can easily access and track items I'm interested in"*|![User Story](documentation/readme_files/profile-favourites-feature.png)|
| *"As a registered user I can update my personal information on my profile so that my account details are always accurate"*|![User Story](documentation/readme_files/profile-info-feature.png)|
| *"As a user I can fill out the contact form and send a message so that I can communicate with the site administrators"*|![User Story](documentation/readme_files/contact-feature.png)|
| *"As a user I can subscribe to the newsletter so that I can receive updates and promotions"*|![User Story](documentation/readme_files/footer-feature.png)|
| *"As a user I can leave comments under a certain product so that I can share my thoughts about a particular products"*|![User Story](documentation/readme_files/comments-feature.png)|
| *"As a user I can access and review the privacy policy of the website so that I can understand how my personal information is handled"*|![User Story](documentation/testing_files/privacy-policy-userstory.png)|
| *"As a shopper I can search for a product by name or description easily so that I can find specific items quickly"*|![User Story](documentation/readme_files/search-feature.png)|
| *"As a shopper I can view a list of products and product details so that I can make a purchase"*|![User Story](documentation/readme_files/products-feature.png)|
| *"As a shopper I can view a list of products and product details so that I can make a purchase"*|![User Story](documentation/readme_files/product-detail-feature.png)|
| *"As a shopper I can view product categories so that I can explore items based on my preferences"*|![User Story](documentation/readme_files/categories-feature.png)|
| *"As a shopper I can easily select the quantity of a product when purchasing it so that I can control my order details"*|![User Story](documentation/testing_files/quantity-userstory.png)|
| *"As a shopper, I can add items to cart, view items in my cart and adjust the quantity before checkout so that I can review and modify my order"*|![User Story](documentation/readme_files/shopping-cart-feature.png)|
| *"As a shopper I can see the total price for the items and enter payment information securely during checkout so that I can make a purchase"*|![User Story](documentation/readme_files/checkout-feature.png)|
| *"As a shopper I can view an order confirmation after completing the checkout process so that I can have a summary of my purchase"*|![User Story](documentation/readme_files/order-confirmation-feature.png)|
| *"As a shopper I can receive an email confirmation after checking out so that I have a record of my purchase"*|![User Story](documentation/readme_files/order-confirmation-email-feature.png)|
| *"As a site admin I can add products to the catalog so that I can expand and update the product offerings"*|![User Story](documentation/readme_files/add-product-feature.png)|
| *"As a site admin I can edit/update existing products on the webiste so that I can keep product information accurate"*|![User Story](documentation/readme_files/edit-product-feature.png)|
| *"As a site admin I can delete products from the catalog so that I can manage the product offerings effectively"*|![User Story](documentation/readme_files/prod-man-edit-delete-btns-feature.png)|
| *"As a site admin I can make the website SEO-optimized so that it ranks higher in search engine results"*|![User Story](documentation/testing_files/metatags.png)|
| *"As a site admin I can make the website SEO-optimized so that it ranks higher in search engine results"*|![User Story](documentation/testing_files/robots.png)|
| *"As a site admin I can make the website SEO-optimized so that it ranks higher in search engine results"*|![User Story](documentation/testing_files/sitemap.png)|
| *"As a site admin I can implement Facebook marketing strategies so that the website gains visibility and attracts more users"*|![User Story](documentation/readme_files/facebook-page-one.png)|

## Validator Testing

### HTML

[W3C validation](https://validator.w3.org/) was used to check the markup validity of html file.

<details><summary><b>base (index).html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>404.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>products.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>product_detail.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>add_product.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>edit_product.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>cart.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>checkout.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>checkout_success.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>contact.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

<details><summary><b>profile.html</b></summary>

![HTML](documentation/readme_files/header-feature.png)
</details>

### CSS

[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the validity of css file.

<details><summary><b>base.css</b></summary>

![CSS](documentation/testing_files/base-css.png)
</details>

<details><summary><b>checkout.html</b></summary>

![CSS](documentation/testing_files/checkout-css.png)
</details>

<details><summary><b>profile.css</b></summary>

![CSS](documentation/testing_files/profile-css.png)
</details>

### JavaScript

[JSHint](https://jshint.com/) was used for validation.

<details><summary><b>stripe_elements.js</b></summary>

![JS](documentation/testing_files/stripe-elements-js.png)
</details>

<details><summary><b>quantity_input_script</b></summary>

![JS](documentation/testing_files/quantity-input.png)
</details>

<details><summary><b>Other js code in html</b></summary>

![JS](documentation/testing_files/otherjs-code.png)
</details>

### Python

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.

## Unit Testing

### Coverage

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

####  app

## Error Handling

### Error Pages Testing

## Manual Testing

### Lighthouse

Note to the assessors: The accessibility is low because of some of the Bootstrap elements.

##### Mobile

| Page | Screenshot |
| ---  | --- |
| Home |![screenshot](documentation/testing_files/home-lighthouse-mobile.png) |
| Products |![screenshot](documentation/testing_files/products-lighthouse-mobile.png) |
| Product Detail |![screenshot](documentation/testing_files/product-detail-lighthouse-mobile.png) |
| Cart |![screenshot](documentation/testing_files/home-lighthouse-mobile.png) |
| Checkout |![screenshot](documentation/testing_files/checkout-lighthouse-mobile.png) |
| Checkout Success |![screenshot](documentation/testing_files/checkout-success-lighthouse-mobile.png) |
| Profile |![screenshot](documentation/testing_files/profile-lighthouse-mobile.png) |
| Contact |![screenshot](documentation/testing_files/contact-lighthouse-mobile.png) |
| Add Product |![screenshot](documentation/testing_files/add-product-lighthouse-mobile.png) |
| Edit Product |![screenshot](documentation/testing_files/edit-product-lighthouse-mobile.png) |
| Sign Up |![screenshot](documentation/testing_files/signup-lighthouse-mobile.png) |
| Sign In |![screenshot](documentation/testing_files/signin-lighthouse-mobile.png) |
| Log Out |![screenshot](documentation/testing_files/logout-lighthouse-mobile.png) |

##### Desktop

| Page | Screenshot |
| ---  | --- |
| Home |![screenshot](documentation/testing_files/home-lighthouse-desktop.png) |
| Products |![screenshot](documentation/testing_files/products-lighthouse-desktop.png) |
| Product Detail |![screenshot](documentation/testing_files/product-detail-lighthouse-desktop.png) |
| Cart |![screenshot](documentation/testing_files/cart-lighthouse-desktop.png) |
| Checkout |![screenshot](documentation/testing_files/checkout-lighthouse-desktop.png) |
| Checkout Success |![screenshot](documentation/testing_files/checkout-success-lighthouse-desktop.png) |
| Profile |![screenshot](documentation/testing_files/profile-lighthouse-desktop.png) |
| Contact |![screenshot](documentation/testing_files/contact-lighthouse-desktop.png) |
| Add Product |![screenshot](documentation/testing_files/add-product-lighthouse-desktop.png) |
| Edit Product |![screenshot](documentation/testing_files/edit-product-lighthouse-desktop.png) |
| Sign Up |![screenshot](documentation/testing_files/signup-lighthouse-desktop.png) |
| Sign In |![screenshot](documentation/testing_files/signin-lighthouse-desktop.png) |
| Log Out |![screenshot](documentation/testing_files/logout-lighthouse-desktop.png) |

### Responsiveness

### Browser compatibility

| Browser | Fail/Pass | Screenshot |
| ---  | ---  | --- |
| Chrome | Pass | ![screenshot](documentation/testing_files/homepage-userstory.png) |
| Edge | Pass | ![screenshot](documentation/testing_files/edge.png) |
| Opera | Pass | ![screenshot](documentation/testing_files/opera.png) |
| Firefox | Pass | ![screenshot](documentation/testing_files/firefox.png) |

## Bugs

### Solved

### Unsolved

