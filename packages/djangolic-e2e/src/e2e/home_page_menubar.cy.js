describe('The Home Page', () => {
    it('successfully loads', () => {
      
      cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
      cy.get('header').contains('Index').click()
      cy.url().should('include', 'http://127.0.0.1:8000/index')

      cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
      cy.get('header').contains('Search').click()
      cy.url().should('include', 'http://127.0.0.1:8000/search')

      cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
      cy.get('header').contains('Create').click()
      cy.url().should('include', 'http://127.0.0.1:8000/create')

      cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
      cy.get('header').contains('Delete').click()
      cy.url().should('include', 'http://127.0.0.1:8000/delete')

      cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
      cy.get('header').contains('Update').click()
      cy.url().should('include', 'http://127.0.0.1:8000/update')

      cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
      cy.get('header').contains('About').click()
      cy.url().should('include', 'http://127.0.0.1:8000/about')
    })
  })