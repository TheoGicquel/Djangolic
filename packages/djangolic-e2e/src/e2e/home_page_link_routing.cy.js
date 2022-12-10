beforeEach(() => cy.visit('/'));

describe('Buttons routing in index page body should navigate to :', () => {

  it('goes to a random beer page', () => {
    cy.get("a").contains('I\'m feeling lucky').click()
    cy.url().should('include', '/random')
  })
  it('goes to the index page', () => {
    cy.get("a").get("div").contains('Index').click()
    cy.url().should('include', '/index')
  })
  it('goes to search form', () => {
    cy.get("a").get("div").contains('Search').click()
    cy.url().should('include', '/search')
  })
  it('goes to the beer create form', () => {
    cy.get("a").get("div").contains('Create').click()
    cy.url().should('include', '/create')
  })
    it('goes to the about page', () => {
    cy.get("a").get("div").contains('About').click()
    cy.url().should('include', '/about')
  })
})

describe('Buttons routing in index page navbar should navigate to :', () => {
    it('goes to index page', () => {
      
      cy.get('header').contains('Index').click()
      cy.url().should('eq', Cypress.config().baseUrl + '/index')
    })
    it('goes to search form', () => {

      cy.get('header').contains('Search').click()
      cy.url().should('eq', 'http://127.0.0.1:8000/search')
    })
      it('goes to create form', () => {

      cy.get('header').contains('Create').click()
      cy.url().should('eq', Cypress.config().baseUrl+'/create')
    })
      it('goes to about page', () => {
      cy.get('header').contains('About').click()
      cy.url().should('include', Cypress.config().baseUrl+'/about')
    })
  })

