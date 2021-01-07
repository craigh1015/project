# Open Gaming

## Entities

Users (Players, Admin)
    Player (Idle, Looking, Reserved, Playing, Running Game)
Locations (Open, Reserved)
Games (Open, Running, Complete, Abandoned:flag)

## Actions

User:Admin -> Register
User:Admin -> Login
DONE - User:Admin -> CRUD Location (Location Description, Max Slots, state)

User:Player -> Register
User:Player -> Login
DONE - User:Player -> List available locations
User:Player -> Create OpenGame (Location, GameDescription, Slots, Start, Duration)
  : no overlap on location
  : start within X minutes
  : max duration (2 hrs)
  : notify players that are looking
User:Player(Own Game) -> Cancel Reservation
User:Player(Own Game) -> View slots / reservations
User:Player(Own Game) -> Check in a player
User:Player(Own Game) -> Start game early
User:Player(Own Game) -> Abandon game (notify Players with reservations)
User:Player(Own Game) -> End game (free location)

User:Player -> List Games()
User:Player -> Reserve Slot(Open game) : no overlap
User:Player -> Register Looking

System -> timer warnings - Notify "GM" of duration end (30, 10, 5, end)

## Waiting list

Groups - Reserving as part of group
Delegate reservations - book on behalf of someone else
User:GM -> End game
