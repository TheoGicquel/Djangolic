describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="bg-gray-50"]').get("a").contains('Search').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="bg-gray-50"]').get("a").contains('I\'m feeling lucky').click()
    cy.url().should('include', 'http://127.0.0.1:8000/random')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="flex  flex-row flex-wrap max-w-4xl   mx-auto space-x-2"]').get("a").get("div").contains('Index').click()
    cy.url().should('include', 'http://127.0.0.1:8000/index')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="flex  flex-row flex-wrap max-w-4xl   mx-auto space-x-2"]').get("a").get("div").contains('Search').click()
    cy.url().should('include', 'http://127.0.0.1:8000/search')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="flex  flex-row flex-wrap max-w-4xl   mx-auto space-x-2"]').get("a").get("div").contains('Create').click()
    cy.url().should('include', 'http://127.0.0.1:8000/create')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="flex  flex-row flex-wrap max-w-4xl   mx-auto space-x-2"]').get("a").get("div").contains('Delete').click()
    cy.url().should('include', 'http://127.0.0.1:8000/delete')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="flex  flex-row flex-wrap max-w-4xl   mx-auto space-x-2"]').get("a").get("div").contains('Update').click()
    cy.url().should('include', 'http://127.0.0.1:8000/update')

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.get('section[class*="flex  flex-row flex-wrap max-w-4xl   mx-auto space-x-2"]').get("a").get("div").contains('About').click()
    cy.url().should('include', 'http://127.0.0.1:8000/about')
  })
})

