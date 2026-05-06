---
title: "Job Board"
listing:
  contents: offers
  type: grid
  page-size: 9
  sort: "date desc"
  fields: [title, author, date, description, categories]
  categories: true
  filter-ui: true
  sort-ui: false
  feed:
    title: "Open Models Job Board"
page-layout: full
---

Find here your next jobs to work around open models and digital commons!

::: {.callout-note collapse="true"}
## How to share a job offer?

Anyone can propose a job offer by opening an issue on [GitHub](https://github.com/Open-Models/Base/issues/new).
Accepted offers are published as open data following the [Schema.org JobPosting](https://schema.org/JobPosting)
standard, and are freely reusable by anyone.

##### Contribution guideline
**Required info to generate the JSON**: Job title, organization, description, short resume, publication date, url, categories. Try the following [prompt](jobs.prompt) for
conversion with AI.
:::

<a href="index.xml">
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="#f26522" style="vertical-align:middle; margin-right:4px">
    <circle cx="6.18" cy="17.82" r="2.18"/>
    <path d="M4 4.44v2.83c7.03 0 12.73 5.7 12.73 12.73h2.83c0-8.59-6.97-15.56-15.56-15.56zm0 5.66v2.83c3.9 0 7.07 3.17 7.07 7.07h2.83c0-5.47-4.43-9.9-9.9-9.9z"/>
  </svg>
  Subscribe to the job RSS feed
</a>
