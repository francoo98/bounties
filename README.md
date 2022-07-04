# bounties
A website to create coding bounties.
It allows the user to create bounties (programming tasks), post solutions for the bounties and choose a solution as the winner of a bounty.
It also has deletion functionalities for bounties and solutions.
# `bounties` app
Every functionality is developed in this app.
## Urls
1. `bounty/` Lists all bounties
2. `bounty/<int>` Display the details of a given bounty refered by `<int>`
3. `bounty/create` Lets de user create a new bounty
4. `bounty/delete/<int>` Deletes the bounty refered by `<int>`
5. `bounty/<int>/solution/create` Creates a solution to the bounty refered by `<int>`
6. `bounty/<int:bounty_pk>/solution/delete/<int:pk>` Deletes a solution (`<int:pk>`) posted to the bounty refered by `<int:bounty_pk>`
7. `bounty/<int:bounty_pk>/solution/award/<int:pk>` Chooses the solution (`<int:pk>`) as the winner of the bounty (`<int:bounty_pk>`)