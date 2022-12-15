
describe('A user i searching for a Kwak beer', () => {

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

        //cy.get("[data-cy=page-title]").should("contain", "results",{ matchCase: false })
    })

    it('finds the card associated to the Kwak beer', () => {
        //cy.get("[data-cy=beer-article]")
        //.should("contain", "Kwak",{ matchCase: false })
        cy.get('[data-cy="beer-article"]').should("contain", "Kwak")
        .contains('[data-cy="view-button"]', 'Kwak').click()

    })


})
    