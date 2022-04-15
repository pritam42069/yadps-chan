# Setting up yadps-chan

## Standard
1. [First install minimum Python 3.10](https://www.python.org/downloads/)
2. Clone the project
3. Run: `python -m pip install --editable .[dev]` for the development environment.
Use `.` instead of `.[dev]` for production. 
4. Setup your bot token in `settings/.env` with key `TOKEN=`
5. Run `python main.py`

## Docker
1. [This guide is under the presumption you have Docker installed.](https://docs.docker.com/get-docker/)
2. Setup `.env` file inside `settings/` folder with key value `TOKEN=XXX`
3. It is heavily suggested to use `compose v2` which can be [installed from official Docker documentation](https://docs.docker.com/compose/cli-command/)
4. Run the following command: `docker build -t "yadps:latest" .` to build the image `yadps:latest`
5. Using `v2 compose` to run the bot: `docker compose up` in the same location as `docker-compose.yml`

# Contributing
If you're having trouble with setting up the project, you can find us on the official [Discord](https://discord.gg/zFBfXDY7RY)

## Submitting a pull request
If you've decided to fix a bug, even something as small as a single-letter typo, we welcome anything that improves code/documentation for all future users and developers.

If you decide to work on a feature in the issues section it's best to let us (and everyone else) know what you're working on to avoid any duplication of effort. You can do this by replying to the original Issue for the request.
We can assign and lock it until it's ready if necessary.

If you want to contribute an example; go for it! We might not always be able to accept your code, but there's a lot to be learned from trying anyway and if you're new to GitHub we're willing to guide you on that journey.

When contributing a new example or making a change to a library please keep your code style consistent with ours and latest PEP guidelines.