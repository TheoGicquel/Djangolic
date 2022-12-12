
describe('The random beer picking', () => {
  
  beforeEach(() => {
    cy.visit('/')
  })


  it('successfully navigates', () => {
    cy.get('a').contains("lucky").click()
    cy.url().should('include', '/random')
  })


  it('should not display the same beer each time', () => {
    cy.get('a').contains("lucky").click()

    let beer1 = document.getElementsByTagName('h1').value
  
    cy.visit('/random')
    let beer2 = document.getElementsByTagName('h1').value


    cy.visit('/random')
    let beer3 = document.getElementsByTagName('h1').value

    // extra redundancy just in case
    cy.visit('/random')
    cy.get('h1').should('not.have.value', beer1)
    cy.get('h1').should('not.have.value', beer2)
    cy.get('h1').should('not.have.value', beer3)

    
  })

})
