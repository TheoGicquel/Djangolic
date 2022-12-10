# Djangolic

A Django + Tailwind CRUD app to search and organize beers.

## Features

- Search for beers using different criterias
- Add / Delete / Modifiy beers
- Responsive design

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Tech Stack

**Client:** Jinja + Tailwind CSS + Fontawesome Icons

**Server:** Django

**Testing/Build:** Nx (Nrwl) + Cypress

## Installation

Install all required dependencies and populate database

```bash
./install.sh
```

## Running Project

To build and deploy this project run :

```bash
  npx nx djangolic:build
  npx nx djangolic:serve
```

## Environment Variables

The following environment variables can be found in `/packages/djangolic/djangolic/.env`

- `NPM_BIN_PATH_WINDOWS`
- `SECRET_KEY`

## Running Tests

To run tests in a terminal, run the following command

```bash
    npx nx djangolic-e2e:e2e
```

If you wish to run tests in the interactive GUI provided by cypress, launch the following script :

```bash
    ./cypress.sh
```
