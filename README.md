
## Where in the world is the International Space Station (ISS) ?

<!-- ### Objectives
- Use the requests package to query real-world data
- Improve skills with dictionaries and indexing
- Learn about the built-in Python [Turtle](https://docs.python.org/3.3/library/turtle.html?highlight=turtle) graphics library. -->

### Part A
Using this public API, write a python program to obtain a list of the astronauts who are currently in space.  Print their full names, the spacecraft they are currently on board, and the total number of astronauts in space.
> [http://api.open-notify.org/astros.json](http://api.open-notify.org/astros.json)

### Part B
Using another public API, obtain the current geographic coordinates (lat/lon) of the space station, along with a timestamp.
> [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)

### Part C
With the [turtle](https://docs.python.org/2/library/turtle.html) graphics library (part of standard Python), create a graphics screen with the world map background image.  Use turtle methods such as `Screen`, `setup`, `bgpic`, `setworldcoordinates`.  Register an icon image for the ISS station within the turtle screen context, and create a `turtle.Turtle()` context to move the ISS station to its current lat/lon on the map.  Use methods such as `shape`, `setheading`, `penup`, and `goto`.

### Part D
Find out the next time that the ISS will be overhead of Indianapolis IN.  Use our geographic lat/lon to plot a yellow dot on the map.  Use this public API to query the next pass:
>[http://api.open-notify.org/iss-pass.json](http://api.open-notify.org/iss-pass.json)

You will need to supply the lat/lon coordinates as query parameters to this url.  The passover times are returned as timestamps, so you will need to use the `time.ctime()` method to convert them to human-readable text.  Render the next passover time next to the Indianapolis location dot that you plotted earlier.

<!--  ### PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.  -->



![spacestation](https://user-images.githubusercontent.com/24884380/161321060-1e4968bb-6fb0-4d39-aae9-f704dd87d2bf.jpeg)



