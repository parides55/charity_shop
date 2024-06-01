[**Charity Treasures**](https://charity-shop-pp4-2870c2ac8971.herokuapp.com/)

<details>
<summary>Table of Contents</summary>

- [Introduction](#introduction)
- [User stories](#user-stories)
- [UX](#ux)
  - [Typography](#typography)
  - [Wireframes](#wireframes)
- [Accessibility](#accessibility)
- [Database Design](#database-design)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness](#responsiveness)
  - [Performance Testing](#performance-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [User Story Testing](#user-story-testing)
  - [Code Validation](#code-validation)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

</details>

## Introduction

This projects is a charity website where mostly second hands items are sold in order to raise money and donate to various charity organizations.

It's main features are a product list where users can view items and add them to their basket in order to buy. Also, charity events are advertised in order to inform the website's users and visitors.

The project was built keeping the Agile management principles in mind, and I utilized many of GitHub's features such as Issue and Projects to complete the website. A [Kanban board](https://github.com/users/parides55/projects/3) was used as well to implement the users stories and to keep track of the features left to do.

I used GitHub issues for the product backlog containing the user stories and the labels feature in GitHub Issues for prioritizing features based on the MoSCoW method, and categorizing the user stories.

<details>
<summary>Issues on GitHub with labels</summary>

![Issues on GitHub with labels](Readme_docs/issues_with_MoSCoW.png)

</details>

## User stories

User stories were prepared using GitHub Issues and assigned acceptance criteria for each story, which were used for the manual testing.

User Stories can been seen below under [User Story Testing](#user-story-testing), and in the GitHub Issues for full details including screenshots and acceptance criteria.

## UX

### Typography

- [Roboto google fonts](https://fonts.google.com/specimen/Roboto?query=roboto) were used for the headings.
- [Montserrat google fonts](https://fonts.google.com/specimen/Montserrat?query=montse) were user for all other text.

### Wireframes

## Accessibility

## Database Design

## Features

## Technologies used

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/) for installing Python packages.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for storing the repository online during development.
- GitHub Projects was invaluable throughout the project and helped me keep track of things to do and bugs to fix - you can see [the project's board here](https://github.com/users/parides55/projects/3).
- Visual Studio Code as an IDE.
- [Balsamiq](https://balsamiq.com/wireframes/) for wireframing.
- [Bootstrap 5](https://getbootstrap.com/) as a front end framework.
- [diagrams.net](https://www.diagrams.net/) for drawing database diagrams.
- [favicon.io](https://favicon.io/favicon-generator/) to make a favicon for site.
- [Device Frames](https://deviceframes.com/) for the device mockups in this README.
- [Meta Tags](https://metatags.io/) to prepare the Meta tags for social media share previews.
- [ColorSpace](https://mycolor.space/?hex=%23CCE0C5&sub=1) to choose the color palettes.
- [Design.com](https://www.design.com/) to design, generate and edit the logo.
- [Am I responsive](https://ui.dev/amiresponsive) to generate the mock ups.
- [Stripe](https://stripe.com/gb) as an external provider to handle payments
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/), [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/), [Microsoft Edge](https://www.microsoft.com/en-us/edge) for testing on Windows 11.
- [Safari](https://www.apple.com/safari/) on iOS and iPadOS 15.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/) on Android 12.

## Testing

### Browser Compatibility

### Responsiveness

### Performance Testing

### Accessibility Testing

### User Story Testing

<details>
<summary>As a first-time visitor I want to have a clear explanation of the website so that I know what is it about.</summary>

AC1 : If I visit the homepage I am greeted with a eye catching slogan/hero image

AC2 : I should be able to tell the purpose of the site easily

Result: Pass ✅
</details>

<details>
<summary>As a visitor to the site I want to read the Privacy policy before I sign up so that I can know how my data will be used.</summary>

AC1: By clicking on a link to be directed to a page about the privacy policy

Result: Pass ✅
</details>

<details>
<summary>As a visitor I can signup to the site so that I can buy products, donate, and leave a review.</summary>

AC1 : By filling the signup form be able to register an account

AC2 : Be able to Log In

AC3: After logging in the user is able to buy products, donate and leave a review

Result: Pass ✅
</details>

<details>
<summary>As a user I can view all the products so that I can select one to view to buy it.</summary>

AC1 : When the user clicks on a link a full list of products is displayed.

AC2 : When a user clicks on a product it can see all the information about it.

Result: Pass ✅
</details>

<details>
<summary>As a user I can add products to my favorites so that I can review them later.</summary>

AC1 : By clicking on a button the product is added in user's favorites list.

AC2 : The item can also be removed from the list

Result: Pass ✅
</details>

<details>
<summary>As a user I can add products to my basket so that I can review them again before I buy them.</summary>

AC1 : By clicking a button the product is added to user's basket

AC2 : In the user's basket all the selected products are displayed with the total price.

AC3 : By clicking a button the user in taken to a page to insert payment details and once payment is received the items are deleted from the database.

AC4 : The user can remove items from the basket.

Result: Pass ✅
</details>

<details>
<summary>As a user I can leave a review on each event so that I can communicate my thoughts.</summary>

AC1 : An authorized user can leave a review on each event

AC2 : All reviews are displayed after admin's approval

AC3 : An authorized user can edit and delete their reviews.

Result: Pass ✅
</details>

<details>
<summary>As a user I can view all the events available so that I know what they are about and attend them.</summary>

AC1 : By clicking on a link the user can see a full list of the events

AC2 : By clicking on an event the user can see all the information about the event

Result: Pass ✅
</details>

<details>
<summary>As user/visitor I can read the story of the site so that I can decide if I want to become a member.</summary>

AC1 : By clicking on a link the user/visitor can see the information about the website.

Result: Pass ✅
</details>

<details>
<summary>A user/visitor I can contact the admin of the site by filling out the contact us form so that I can communicate with the admin.</summary>

AC1 : When the user/visitor clicks on a link is taken to the Contact Us form.

AC2 : By filling out the form a message is send to the admin and confirmation message is shown to the user/visitor.

Result: Pass ✅
</details>

<details>
<summary>As an admin I can add products and events so that I can raise money for the charities.</summary>

AC1 : Provide is a logged in user they can add/remove/edit products and events

Result: Pass ✅
</details>

<details>
<summary>As an admin I can read and approve the user’s reviews so that I can filter out objectionable reviews.</summary>

AC1 : Provided a logged in user they can approve/disapprove users reviews

AC2 : Provided a logged in user they can add or delete reviews.

Result: Pass ✅
</details>

<details>
<summary>As an admin I can create draft events so that I can finish writing the content later.</summary>

AC1 : Provided a logged in user I can add events and save them as drafts.

Result: Pass ✅
</details>

<details>
<summary>As an admin I can create or update the about page content so that it is available on the site.</summary>

AC1 : Provided a logged in user they can add and update the content in the about page.

Result: Pass ✅
</details>

<details>
<summary>As an admin I can view the orders made by users so that I can manage them.</summary>

AC1 : Provided a logged in user they can view the orders of the users.
Result: Pass ✅
</details>

### Code Validation

## Deployment

Charity Treasures is deployed to Heroku, using an ElephantSQL Postgres database and Cloudinary for media storage.
To deploy to Heroku, follow these steps:

- Fork or clone this repository in GitHub.
- You will need a Cloudinary account to host user images and static files.
- Login to Cloudinary.
- Select the 'dashboard' option.
- Copy the value of the 'API Environment variable' from the part starting `cloudinary://` to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
- Log in to Heroku.
- Select 'Create new app' from the 'New' menu at the top right.
- Enter a name for the app and select the appropriate region.
- Select 'Create app'.
- Select 'Settings' from the menu at the top.
- Login to ElephantSQL.
- Click 'Create new instance' on the dashboard.
- Name the 'plan' and select the 'Tiny Turtle (free)' plan.
- Select 'select region'.
- Choose the nearest data centre to your location.
- Click 'Review'.
- Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
- Copy the ElephantSQL database URL to your clipboard (this starts with `postgres://`).
- Return to the Heroku dashboard.
- Select the 'settings' tab.
- Locate the 'reveal config vars' link and select.
- Enter the following config var names and values:
    - `CLOUDINARY_URL`: *your cloudinary URL as obtained above*
    - `DATABASE_URL`: *your ElephantSQL postgres database URL as obtained above*
    - `SECRET_KEY`: *your secret key*
- Select the 'Deploy' tab at the top.
- Select 'GitHub' and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
- Find the 'Connect to GitHub' section and use the search box to locate your repo.
- Select 'Connect' when found.
- Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed site to be automatically redeployed every time you push changes to GitHub.
- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
- Your site will shortly be deployed and you will be given a link to the deployed site when the process is complete.

## Credits

### Content

### Media

### Acknowledgements
