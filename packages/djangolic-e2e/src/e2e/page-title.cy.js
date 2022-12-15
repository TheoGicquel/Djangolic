
describe('Title tags', () => {
  

  it('Index page correctly named', () => {
    cy.visit('/')
    cy.get("[data-cy=page-title]").should("contain", "index",{ matchCase: false })
  })

  it('About page correctly named', () => {
    cy.visit('/about')
    cy.get("[data-cy=page-title]").should("contain", "About",{ matchCase: false })
  })

  it('Search page correctly named', () => {
    cy.visit('/search')
    cy.get("[data-cy=page-title]").should("contain", "Search",{ matchCase: false })
  })


  it('Create page correctly named', () => {
    cy.visit('/create')
    cy.get("[data-cy=page-title]").should("contain", "create",{ matchCase: false })
  })


  it('Beer page correctly named', () => {
    cy.visit('/beer/1/view')
    cy.get("[data-cy=page-title]").should("contain", "view",{ matchCase: false })
  })

})


