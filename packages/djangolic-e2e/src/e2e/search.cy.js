describe('The Search form', () => {

  beforeEach(() => {
    cy.visit('/search')
  })

  it('successfully navigates', () => {
    cy.url().should('include', '/search')
  })
  it('fills the form', () => {
    cy.get('input[name*="name"]').type('Guiness')
  })


  it('selects a single country from the `countries_sold_in` select ', () => {
  
    cy.get('select#id_countries_sold_in').select('France')
  })


  it('selects multiple countries from the `countries_sold_in` select ', () => {
  
    cy.get('select#id_countries_sold_in').select(['France','Belgium'])
  })

})

  describe('The Search results', () => {

    beforeEach(() => {
      cy.visit('/search')
    })

  it('fills the form and finds a Guinnes by name', () => {
    cy.get('input[name*="name"]').type('Guiness')
    cy.get('button[type*="submit"]').click()
    cy.get('h3').contains('Guiness')
  })

  it('does not find a beer that should not exist', () => {
    cy.get('input[name*="name"]').type('@#$%^&*()aaaaadzdsdqsdazdazdsqdqsdzq') // this is silly but it works
    cy.get('button[type*="submit"]').click()
    cy.get('h3').should('not.exist')
  })

  it('finds a beer sold BOTH in france and belgium', () => {
  
    cy.get('select#id_countries_sold_in').select(['France','Belgium'])
    cy.get('button[type*="submit"]').click()
    cy.get('h3').contains('Dremwel').should('not.exist')

  })


  it('finds a beer sold ONLY in belgium', () => {
  
    cy.get('select#id_countries_sold_in').select(['Belgium'])
    cy.get('button[type*="submit"]').click()
    cy.get('h3').contains('Dremwel').should('not.exist')

  })

})