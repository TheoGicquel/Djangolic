describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('http://127.0.0.1:8000/search') // change URL to match your dev URL


    cy.get('input[name*="name"]').type('Guiness').should('have.value', 'Guiness')
    cy.get('select[name*="brewery"]').select('Asahi Biiru Kabushiki Gaisha')
    cy.get('select[name*="countries_sold_in"]').select('France')

    cy.get('input[name*="abv"]').type('-1').should('have.value', '-1')
    cy.get('button[type*="submit"]').click()
    cy.url().should('not.include', 'http://127.0.0.1:8000/search/results')
    cy.get('input[name*="abv"]').clear()

    cy.get('input[name*="abv"]').type('101').should('have.value', '101')
    cy.get('button[type*="submit"]').click()
    cy.url().should('not.include', 'http://127.0.0.1:8000/search/results')
    cy.get('input[name*="abv"]').clear()

    cy.get('input[name*="ibu"]').type('-1').should('have.value', '-1')
    cy.get('button[type*="submit"]').click()
    cy.url().should('not.include', 'http://127.0.0.1:8000/search/results')
    cy.get('input[name*="ibu"]').clear()

    cy.get('input[name*="ibu"]').type('201').should('have.value', '201')
    cy.get('button[type*="submit"]').click()
    cy.url().should('not.include', 'http://127.0.0.1:8000/search/results')
    cy.get('input[name*="ibu"]').clear()

    cy.get('input[name*="ibu"]').type('20').should('have.value', '20')
    cy.get('input[name*="ibu"]').type('120').should('have.value', '120')
    cy.get('button[type*="submit"]').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search/results/')
  })
})