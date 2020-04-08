[![Build Status](https://travis-ci.com/ronbel/cortex.svg?branch=master)](https://travis-ci.com/ronbel/cortex) 
[![Documentation Status](https://readthedocs.org/projects/cortex-rb/badge/?version=latest)](https://cortex-rb.readthedocs.io/en/latest/?badge=latest)

# Cortex

A submission project for the Advanced Systems Design class in Tel Aviv University

## Prerequisites
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

## Basic Usage
After installation and running all the services, you can upload a `.mind` or `.mind.gz` file containing snapshot data to the server by running

```sh
$ python -m cortex.client upload-sample /path/to/file
```

After you're done uploading the sample, you can view the information using the GUI on `http://localhost:8080`, or query the data by running:

```sh
$ python -m cortex.cli get-users
[
    {"user_id": 1, "username": "John Doe"}
]
$ python -m cortex.cli get-user 1
{
    "user_id": 1, "username": "John Doe", "birthday": 123456, "gender": "Male"
}
```


## Deployment

Each submodule (except for client and cli) comes with its own Dockerfile. All of those depend on the cortex-base image (It is build automatically during installation)
If you wish to build your own image of a submodule, simply run:

```sh
$ docker build ./cortex/<module_name>
```

## Documentation

You can view the full documentation here