# Group Project 1 - DiceWare

## Introduction
A password's strength is determined based on the length and complexity of the password: Passwords become exponentially harder to crack with each added character, [i.e.](https://www.hivesystems.io/blog/are-your-passwords-in-the-green) a password that is 8 lowercase letters will be cracked in 3 seconds while a password that is 9 lowercase letters will take 1 minute to crack.
The complexity of a password has a much greater impact on the time it takes to crack a password than the number of characters in the password. Changing the previous 8 character password to use both upper and lower case characters would make the password take 13 minutes to crack instead of just 1. However, this added security comes at the cost of being much harder on the users that need to remember and actually use their passwords. 

Passphrases are designed to address this problem by being simpler to remember while still long enough to be secure; a 18 character long password using only lowercase letters would take ~13 million years to crack.

Small extra note on the cracking times mentioned above, they are taken from the tests on password cracking using a single RTX 3090 in the Hive Systems blog on password strength. This means that the times above are based on 2 year old consumer hardware and not state of the art data centers. 

## Assignment
[Diceware](https://diceware.dmuth.org/) is an online passphrase generator based on rolling dice to randomly select words to use in a passphrase.

For this assignment you will work as a team to create a basic web application that can accomplish the same basic idea.

## Requirements
 1. A simple flask app that hosts the website, which:
    * Displays gifs of dice being rolled according to the chosen word (i.e. 5 Dice with 1 dot)
    * Displays the word that is associated with the dice roll (i.e. abacus)
    * Does this for every word that is chosen in the passphrase

 2. A simple Python function that:
    * Only uses the PIL, flask, json, & datetime / time libraries
    * Can randomly select 5 numbers from 1 to 6 and get the associated word
    * Creates gifs of dice rolling to the chosen numbers

 3. The flask app should use the Python function to get all words and gifs
    * By default the webpage should show at least 6 words and associated gifs
 
 4. This should all be done in a new branch for this repository
 