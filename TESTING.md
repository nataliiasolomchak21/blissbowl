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
    - [SEO](#seo)
    - [Accessibility](#accessibility)
        - [Lighthouse](#lighthouse)
        - [Responsiveness](#responsiveness)
        - [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
    - [Solved](#solved)
    - [Unsolved](#unsolved)

## User Story Tests

| User Story | Screenshot |
| --- | --- |

## Validator Testing

### HTML

[W3C validation](https://validator.w3.org/) was used to check the markup validity of html file.

### CSS

[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the validity of css file.

### JavaScript

[JSHint](https://jshint.com/) was used for validation.

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

### Accessibility

### Lighthouse

##### Mobile

| Page | Size | Screenshot |
| ---  | ---  | --- |

##### Desktop

| Page | Size | Screenshot |
| ---  | ---  | --- |

### Responsiveness

### Browser compatibility

| Browser | Fail/Pass | Screenshot |
| ---  | ---  | --- |

## Bugs

### Solved

### Unsolved

