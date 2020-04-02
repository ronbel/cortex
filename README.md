

# Cortex

A submission project for the Advanced Systems Design class in Tel Aviv University

##Prerequisites
    Python v3.8
    Node v10.0.0+
    npm v6.0.0+
    Docker v 18.06+
    docker-compose v1.20+

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:ronbel/cortex.git
    ...
    $ cd cortex/
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    ```

3. To check that everything is working as expected, run the tests:

    ```sh
    $ pytest tests/
    ```

## Quick Start

To run all the services together, simply enter:
```sh
$ docker-compose up -d
```
When all services are running, you can access the user interface via `http://localhost:8080`

##Basic Usage

