<img src="https://zebrands.mx/wp-content/uploads/2021/07/WEB-ZEB-05-1-1024x291.png" width="300">

# Data Engineering Technical Test

Hello there! Thank you for showing interest in applying to Zebrands. As part of our recruitment process, we would like to invite you to take on this challenge, which will allow you to showcase your skills and knowledge.

## Context

At Zebrands, we distribute our products through a variety of channels, both online and offline. One of these channels includes sales on popular marketplace platforms such as Amazon, Mercadolibre, Walmart, Linio, and others. To ensure our products are accurately represented and up-to-date on these platforms, we have an internal operations team responsible for managing the catalog. This team continuously monitors product availability, price, description, and other attributes to ensure everything is accurate and up-to-date.

## Problem

Considering the large number of products we sell (think of ~500 different SKUs) and the number of marketplaces we sell on (more than 10 platforms), ensuring that our products are correctly cataloged on all platforms at all times becomes a complex task.
To have better control, we want to have a general dashboard where we can visualize the price and availability of each product on each marketplace on any date in the past.

## What we need from you

1. Propose a data architecture that supports the collection, processing, and visualization of price and availability data for _N_ of our products across _M_ different marketplace platforms. Please take the following points into consideration:
   - We need to obtain price and availability data at least once a day and store the historical data indefinitely.
   - The architecture must be able to handle the addition and removal of products from our catalog.
   - Not all marketplaces sell all our products.
   - The data sources can vary and depend on the marketplace, such as internally implemented web scrapers, connections to marketplace APIs, batch files sent by partners, or manual CSV uploads.

   **Expected deliverable**: An architecture diagram along with an explanation and justification of your proposal.

2. As a proof of concept, implement a web scraper that can automatically gather the price and availability information of every version of the "Colchón Luuna Original" on a marketplace of your choice. The scraper should be scheduled to run once a day and store the data in a structured format on a platform of your choice. 

   Please pay special attention to the details while implementing the web scraper, focusing on aspects such as code quality, versioning, modularity, and maintainability, along with other essential software engineering principles. Although this project serves as a proof of concept in terms of scope, we anticipate a solution that meets production-quality standards.
   
   For your convienence, we have provided links to the product on some marketplaces below (we only require that you implement the web scraper on one platform):
    - Amazon: https://www.amazon.com.mx/Luuna-Colch%C3%B3n-Memory-L%C3%A1tex-Matrimonial/dp/B019YBYBSC
    - Mercadolibre: https://www.mercadolibre.com.mx/colchon-1-plaza-de-espuma-luuna-original-100cm-x-190cm-x-24cm/p/MLM15569488
    - Liverpool: https://www.liverpool.com.mx/tienda/pdp/colch%C3%B3n-luuna-confort-medio/1062274906

   **Expected deliverable**: A repository link, containing the code of the web scraper.
   
3. Create a dashboard using any platform and technology you prefer. The dashboard should utilize the data collected by the web scraper to display the price history of the "Colchón Luuna Original" in its different versions (individual, matrimonial, etc.) over time. If you need to perform any pre-processing tasks before building the dashboard, you are welcome to do so and share your code with us.

   **Expected deliverable**: A link to the functional dashboard.

## What we will evaluate

The challenge may seem ambiguous or broad in some points. This is intentional as we expect you to make reasonable assumptions and decisions.

Your challenge will be evaluated on the following dimensions:

* Relevance of the solution: We are looking for your proposed architecture to meet the requirements and be scalable over time.
* Code quality: We take writing clean, readable, and maintainable code seriously.
* Creativity: Don't limit yourself to the instructions; if you have a good idea, go for it!
* Communication: In this position, your technical ability is equally important as your ability to communicate, so make sure your explanations and documentation are clear and concise.
