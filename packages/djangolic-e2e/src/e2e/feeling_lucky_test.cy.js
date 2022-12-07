import { webcrypto } from "crypto"

describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.contains('I\'m feeling lucky').click()
    cy.url().should('include', 'http://127.0.0.1:8000/random')
    let biere1 = document.getElementsByTagName('h1').value

    cy.visit('http://127.0.0.1:8000/') // change URL to match your dev URL
    cy.contains('I\'m feeling lucky').click()
    cy.url().should('include', 'http://127.0.0.1:8000/random')
    cy.get('h1').should('not.have.value', biere1)
    
  })
})