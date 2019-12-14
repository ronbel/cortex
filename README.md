

# Thought System

A submission project for the Advanced Systems Design class in Tel Aviv University

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:advanced-system-design/project-3123350812.git
    ...
    $ cd project-312350812/
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

## Usage

The `thought_system` package provides the following classes:

- `Thought`

   Description goes here

    ```pycon
    Sample code goes here
    ```



The `thought_system` package also provides a command-line interface:

```sh
$ python -m thought_system
```


The CLI provides the `upload-thought`, `serve` and `serve-web` subcommands

```sh
$ python -m thought_system upload-thought 0.0.0.0:3000 1 "Hello there"
Uploading to 0.0.0.0:3000 a thought by user 1

$ python -m thought_system serve 0.0.0.0:3000 "./tmp"
Starting a server on 0.0.0.0:3000 which stores data in ./tmp


$ python -m thought_system serve-web 0.0.0.0:3000 "./tmp" -d
Starting a webserver on 0.0.0.0:3000 which reads data from ./tmp with debugging
 * Serving Flask app "thought_system.website.webserver" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
 * Restarting with stat
Starting a webserver on 0.0.0.0:3000 which reads data from ./tmp with debugging
 * Debugger is active!
 * Debugger PIN: 300-823-397

```

