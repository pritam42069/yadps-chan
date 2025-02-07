# Description
- Neo Version: 0.0.5

Neo is a templated Discord bot written in python.

The main objective I had with this bot was to make it user friendly and modular, i.e. interchangeable components without messing with core function.

# Roadmap
 * [x] Logging system
 * [x] Parsable configurations
 * [x] Modular command system with a built-in dynamic loader
 * [x] Docker support

# Setup
## Local development - without Docker
1. Run `python -m pip install --editable ".[dev]"`. Alternatively run with `.` over `.[dev]` for production
2. Set `TOKEN` environment variable with Discord token inside `settings/.env` file
3. Then run `python main.py`

You can adjust how the data is loaded inside `config\neoconfig.py` `read()` function if necessary.

## Local development - with Docker
1. Run `docker build . -t neo:latest`
2. Run `docker compose up`

Alternatively alter the `Dockerfile` to build and run the image for you when running `docker compose up`.