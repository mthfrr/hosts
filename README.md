# Spotify
This was meant to block ads on the android Spotify app using Dns66.

It never worked.

Dns66 as it's name impiles only filters dns request.
I have read that ads are stored on the same spotify hostname as the music which makes this kind of blocking useless.
I am not sure if this is entirely true as many people talk about spotify ad blocking rules for piholes. (see this gihub gist for example: https://gist.github.com/teomaragakis/cb187d880c9a3ca2c8a2)

## My solution
I know I can block all Spotify on my pc while using the spotify webapp on Firefox with uBlock origin.
However I could not use the webapp on Firefox for Android so I resorted to using Bromite (chromebased browser with an integrated ad-blocker).
This solution is working for me at the moment 31/05/2021.
