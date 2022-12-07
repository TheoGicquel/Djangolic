describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('http://127.0.0.1:8000/search') // change URL to match your dev URL


    cy.get('input[name*="name"]').type('Guiness')
    cy.get('button[type*="submit"]').click()
    cy.get('a[href*="/beer/2/view"]').contains('Guiness').should('not.null')
  })
})