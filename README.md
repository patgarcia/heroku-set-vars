# heroku-set-vars

Set Heroku environmental variables given a local `.env.heroku` file

### This script assumes:

- Heroku CLI is available
- The user is already signed-in -- `heroku login`
- An app was already created -- `heroku create`
- If no arguments passed, it uses [`.env.heroku`](https://github.com/patgarcia/heroku-set-vars/blob/main/.env.heroku) as the default filename, and corresponding file available in the same path.
- When using the `-f` make sure to provide a full path if file not in same path as script

If you have a `.env.heroku` in the same path just run the file: `$ python3 upload_heroku_env.py`

#### option flags:

`-f` to provide a custom filename

`-u` to unset the config vars

#### examples:

To set all env variables: <br />`$ python3 upload_heroku_env.py`

To **unset** all env variables: <br />`$ python3 upload_heroku_env.py -u`

<hr>

Using a different filename: <br />`$ python3 upload_heroku_env.py -f .env.another`

To **unset** all env variables in different filename: <br />`$ python3 upload_heroku_env.py -f .env.another -u`

> Check the example `.env.heroku` file
