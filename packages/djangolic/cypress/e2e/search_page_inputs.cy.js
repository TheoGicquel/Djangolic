describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('http://127.0.0.1:8000/search') // change URL to match your dev URL


    cy.get('#name').type('Guiness').should('have.value', 'Guiness')
    cy.get('#brewery').type('Taverne').should('have.value', 'Taverne')
    cy.get('#country').type('France').should('have.value', 'France')

    cy.get('#abv').type('-1').should('have.value', '-1')
    cy.get('button[type*="submit"]').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search')
    cy.get('#abv').clear()

    cy.get('#abv').type('101').should('have.value', '101')
    cy.get('button[type*="submit"]').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search')
    cy.get('#abv').clear()

    cy.get('#ibu').type('-1').should('have.value', '-1')
    cy.get('button[type*="submit"]').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search')
    cy.get('#ibu').clear()

    cy.get('#ibu').type('201').should('have.value', '201')
    cy.get('button[type*="submit"]').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search')
    cy.get('#ibu').clear()

    cy.get('#abv').type('20').should('have.value', '20')
    cy.get('#ibu').type('120').should('have.value', '120')
    cy.get('button[type*="submit"]').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search/result/')
  })
})