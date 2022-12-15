


describe('A user i searching for a Kwak beer', () => {
    // reset database to reload fixtures

    before(() => {
        cy.exec("npx nx run djangolic:db-init")
        })

    /**
     * We assume the user does not remember the spelling of kwak, searches by country instead
     */

    it('successfully loads', () => {
      cy.visit('/')
    })

    it('goes to the search page', () => {
        cy.get("[data-cy=search-button]").click()
        cy.url().should('include', '/search')
        cy.get("[data-cy=page-title]").should("contain", "Search",{ matchCase: false })
    })

    it('selects belgium', () => {
        cy.get('select#id_countries_sold_in').select(['Belgium'])
    })

    it('submits the form', () => {
        cy.get('button[type*="submit"]').click()

    })

    it('finds the card associated to the Kwak beer', () => {
        cy.get("[data-cy=beer-article] h3").should("contain", "Kwak")

        cy.get('[data-cy=edit-button]').should('exist').closest('[data-cy=beer-article]')
        .should('have.attr', 'data-cy', 'beer-article').and('contain', 'Kwak')

        cy.get('[data-cy=beer-card-view-link]').should('exist').closest('[data-cy=beer-article]')
        .should('have.attr', 'data-cy', 'beer-article').and('contain', 'Kwak')

    })  

        it('goes to kwak page', () => {

        cy.get("h3").contains("Kwak").click()
    })


    it('changes Taste value', () => {
        cy.url().should('include', '/beer/3')
        cy.get("a").contains("Edit").click()
        cy.get("input[name='taste']").clear().type("lorem ipsum dolor sit amet")
        cy.get("button").contains("Search").click()
        cy.url().should('include', '/beer/3')
        cy.get("p").contains("lorem ipsum dolor sit amet")

    })


})
    