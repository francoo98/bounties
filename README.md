# bounties
A website to create coding bounties.
It allows the user to create bounties (programming tasks), post solutions for the bounties and award a solution.
It also has deletion functionalities for bounties and solutions.
## apps
The site is developed int the `Bounties` app.
# `bounties` app
Every functionality is developed in this app.
## Urls
1. `bounty/` Lists all bounties
2. `bounty/<int>` Display the details of a given bounty refered by <int>
3. `bounty/create` Lets de user create a new bounty
4. `bounty/delete/<int>` Deletes the bounty refered by <int>
5. `bounty/<int>/solution/create` Creates a solution to the bounty refered by <int>
6. `bounty/<int>/solution/delete/<int>` Deletes a solution (second <int>) posted to the bounty refered by the fist <int>
7. `bounty/<int>/solution/award/<int>` Chooses the solution (second <int>) as the winner of the bounty (first <int>)