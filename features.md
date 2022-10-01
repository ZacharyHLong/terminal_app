# Terminal App
The application will be an assistant for casual sport team managers. A common problem I have encountered when participating in organised sport is that the team information is unknown or is hidden within big group chats. Typically, each week, someone is required to pay for the teamsheet and we rotate through. I thought that I could build a terminal application that will have each players contact information and be able to track who has paid for the teamsheet, and randomly determine who pays next. 

---
## The Features
Underpinning this application are several features that enable the team manager to organise the players data, and determine the next payee.

1. Welcome message and menu.
   - Upon initialisation, the team manager will be welcomed and asked to provide their name.
   - They will be provided with a menu of options.
   - View roster, add player, remove player, track payments, and determine payee.
   - Each option will be possible to be selected by the corresponding number next to the option. Notably, the option to remove player, track payments and determine payee will not be available until at least one player has been registered.
   - Testing will be enabled to ensure correct inputs have been included.
   - Upon initialisation, the included csv file will be loaded into the application, allowing returning managers to continue or update the team roster.

2. View Roster
   - The view roster feature will display the team roster (if players have been added) in a table.
   - Information for each player will be displayed.
   - Could potentially add the ability to sort players by number or alphabetically.
   - Imported table graphic

3. Add Player
   - The add player feature will prompt the user with several input options required to add the player to the roster.
   - Will ask user for each player's first name, last name, jersey number, phone number.
   - Once a player entry has been completed, the user will be asked if they would like to add another player, depending on their answer they will either restart the loop or be taken back to the menu.

4. Remove Player
   - The remove player feature will display the list of players along with an index number.
   - The usre will be prompted to select the index number of the player they wish to remove, or will be able to return to the menu.
   - If a player has been selected for removal, their entry will be deleted.
   - How this will be done is yet to be determined.

5. Teamsheet Payment Organiser
   - Takes user to a seperate menu where they can select one of two options.
   - Can generate a randomly chosen person from the team to be selected to pay.
   - Once someone has been selected they are removed from the pool until all people have been selected once, then it will reset.
   - Can see who has paid in the current cycle. And maybe if there is time, there can be a cycle tracker?