# spotify-api-demo

This is a copy of [Cassetteify](https://github.com/estaudere/cassetteify) but with
portions removed for tutorial purposes. Follow along to create your own version of
Cassetteify with the Spotify API and Flask!

Inspired by the popular [Receiptify](https://receiptify.herokuapp.com/), Cassetteify
allows you to view your current month's most top ten artists in a little cassette
illustration (each made out of a single div!).

Runs on Flask and uses [Spotipy](https://github.com/plamere/spotipy) to interact with
Spotify's API.

## Running locally

To run, create a `.env` file with the following information from your Spotify developer
dashboard:

```
CLIENT_ID=<id>
CLIENT_SECRET=<secret>
```

Make sure your environment has the latest versions of `flask`, `spotipy`, `dotenv`, and
`os` downloaded, then run `python app.py` in the terminal.

## Tutorial

1. At the top of `app.py`, set your global vars that contain Spotify scopes and IDs. You can manually set these, or you can add it from an external `.env` file.
2. Also instantiate your authorizer and spotipy client here.
3. Add routes for `callback()` and `top_artists()` and complete the code.
4. Complete the code for `auth()` (which returns the callback url) and `index()` (which returns your main page).
5. Don't forget to add the relevant libraries at the top.
6. Complete Jinja code in the cassettes div in `cassettes.html` to display the right information.
7. Don't forget to add your CSS here as well! (CSS pre-completed in `cassettes.html`, but you can use a different stylesheet.)