![Luuna Logo](https://luuna-bucket.imgix.net/img/header-logo.svg?auto=compress,format)

# Fullstack Technical Test

Hello! Thanks for your interest in applying to ZeBrands.
As a part of the recruiting process, we ask you to complete this task as a way for you to showcase your abilities and knowledge.

# Description of the task

We need to build a very basic website to display a catalog of products. 

On the backend, we need to have a system to manage _products_ (a CRUD approach would be enough). A _product_ should have basic info such as sku, name, price and brand.

As a special requirement, whenever a _product_ creation, update or deletion is made (for example, if a price is adjusted), we need to send a notification to the system admin about the change, either via email or other mechanism (feel free to use any email address for the admin user).

On the frontend, we need at least two views:
    1) The "category view", to list existing _products_
    2) The "product details view" to display _product_ details

Your task is to build this system implementing a REST or GraphQL API using Python (and the frameworks/libraries of your preference) and consuming it from a React or React Native app.

## What we expect
We are going to evaluate all your choices from API design to deployment, so invest enough time in every step, not only coding. The test may feel ambiguous at points because we want you to feel obligated to make design decisions. In real life you will often find this to be the case.

We are going to evaluate these dimensions:
- Code quality: We expect clean code and good practices
- Technology: Use of paradigms, frameworks and libraries. Remember to use the right tool for the right problem
- Creativity: Don't let the previous instructions to limit your choices, be free
- Organization: Project structure, versioning, coding standards
- Documentation: Anyone should be able to run the app and to understand the code (this doesn't mean you need to put comments everywhere :))
- Usability: For frontend we expect you to build a usable application with a mobile first experience

If you want to stand out by going the extra mile, you could do some of the following:
- Add tests for your code
- Containerize your solution
- Deploy the API to a real environment
- Use AWS SES or another 3rd party API to implement the notification system
- Provide API documentation (ideally, auto generated from code)
- Propose an architecture design and give an explanation about how backend and frontend should scale in the future

## Delivering your solution
Please provide us with a link to your personal repository and a link to the running app if you deployed it.
