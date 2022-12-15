
describe('Title tags', () => {
  

  it('Index page correctly named', () => {
    cy.visit('/')
    cy.get("[data-cy=page-title]").should("contain", "index")
  })

  it('About page correctly named', () => {
    cy.visit('/about')
    cy.get("[data-cy=page-title]").should("contain", "About")
  })

  it('Search page correctly named', () => {
    cy.visit('/search')
    cy.get("[data-cy=page-title]").should("contain", "Search")
  })


  it('Create page correctly named', () => {
    cy.visit('/create')
    cy.get("[data-cy=page-title]").should("contain", "Create")
  })


  it('Beer page correctly named', () => {
    cy.visit('/beer/1/view')
    cy.get("[data-cy=page-title]").should("contain", "View")
  })

})


