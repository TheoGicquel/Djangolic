describe('The Search Function', () => {

  beforeEach(() => {
    cy.visit('/search')
  })

  it('successfully navigates', () => {
    cy.url().should('include', '/search')
  })
  it('fills the form', () => {
    cy.get('input[name*="name"]').type('Guiness')
  })


  it('fills the form and search for a Guinnes', () => {
    cy.get('input[name*="name"]').type('Guiness')
    cy.get('button[type*="submit"]').click()
    cy.get('h3').contains('Guiness')
  })

})