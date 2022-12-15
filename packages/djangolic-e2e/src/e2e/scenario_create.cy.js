const fischerTaste = "Avec sa robe dorée et ses délicats arômes sucrés, La Belle Mira met tout le monde d'accord.";


describe('A user i searching for a Kwak beer', () => {
    // reset database to reload fixtures

    before(() => {
        Cypress.Cookies.preserveOnce('csrftoken')
        cy.clearCookies()
        cy.exec("npx nx run djangolic:db-init")
        })

 

    it('successfully loads', () => {
      cy.visit('/')
    })


    it('fills form', () => {
        cy.visit('/create')

        cy.get('input[name*="name"]').type('Fischer La Belle Mira').should('have.value', 'Fischer La Belle Mira')
        cy.get('input[name*="abv"]').type('5.8').should('have.value', '5.8')
        cy.get('input[name*="taste"]').type(fischerTaste).should('have.value', fischerTaste)
        cy.get('input[name*="ibu"]').type('20').should('have.value', '20')
        cy.get('input[name*="image"]').type('https://www.biere-discount.com/img/p/5/1/5/515-thickbox_default.jpg')
        cy.get('select#id_brewery').select('Brasserie Fischer (brasserie du Pécheur)')
        cy.get('select#id_countries_sold_in').select(['France'])
        cy.get('select#id_style').select('Generic')
        cy.get('select#id_type').select('Spéciale')
        cy.get('select#id_glass').select('Goblet')


    })

    it('submits the form', () => {
        cy.get('button[type*="submit"]').click()

    })




})
    