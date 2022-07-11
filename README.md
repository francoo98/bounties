# bounties
A website to create coding bounties.

It supports `Bounty` (model to represent a programming task) and `Solution` creation and deletion, choosing a `Solution` instance as the winner of a `Bounty` and login/logout using Django built in auth system.

### APIs
The website has two APIs implemented with `django-rest-framework`.
These APIs have endpoints to work with bounties, solutions and users (see details below).
## `bounties` app
This app provides the base application to work with bounties.
### Urls
1. `bounty/` Lists all bounties
2. `bounty/<int>` Display the details of a given bounty refered by `<int>`
3. `bounty/create` Lets de user create a new bounty
4. `bounty/delete/<int>` Deletes the bounty refered by `<int>`
5. `bounty/<int>/solution/create` Creates a solution to the bounty refered by `<int>`
6. `bounty/<int:bounty_pk>/solution/delete/<int:pk>` Deletes a solution (`<int:pk>`) posted to the bounty refered by `<int:bounty_pk>`
7. `bounty/<int:bounty_pk>/solution/award/<int:pk>` Chooses the solution (`<int:pk>`) as the winner of the bounty (`<int:bounty_pk>`)
## `bounties_api` app
In this app the project exposes REST endpoints to work with bounties.
### Urls
1. `/api/bounty/` Retrieves a list of `Bounty` (GET) or creates a new `Bounty` (POST)
2. `/api/bounty/<int>/` Applies any of the CRUD operation to a `Bounty` instance
3. `/api/solution/` GETs a list of `Solution` or creates a new one (POST)
4. `/api/solution/<int>/` Applies any of the CRUD operation to a `Solution` instance
NOTE: the delete action is not implemented to remove the object from the DB, but to change the status of the object to `DELETED`.
## `users_api` app
In this app the project exposes REST endpoints to work with users.
### Urls
1. `/api/user/` Retrieves a list of `User` (GET)
2. `/api/user/<int>/` Retrieves the details of a specific `User` (Only GET is implemented)
