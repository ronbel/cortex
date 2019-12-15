

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

   A class that encapsulates the thought object

    ```pycon
    >>> t1 = Thought(1, datetime.datetime.now(), 'General Kenobi!')
    >>> t1.user_id
    1
    >>> t1.timestamp
    datetime.datetime(2019, 12, 15, 12, 19, 38, 341471)
    >>> t1.thought
    'General Kenobi!'

    ```



The `thought_system` package also provides a command-line interface:

```sh
$ python -m thought_system
```


The CLI provides the `upload-thought`, `serve` and `serve-web` subcommands

`upload-thought <Address> <User ID> <Thought>`: Uploads a given `Thought` with the ID of
the user given by `User ID` to the server on `Address`

`serve <Address> <Data Dir>`: Starts a server on `Address` that stores thoughts uploaded
to it in `Data Dir`

`serve-web <Address> <Data Dir> [-d\--debug]`: Starts a server that serves a web interface
for the system on `Address`, reads data from `Data Dir`. Use `-d` 
or `--debug` to enable debugging on the server

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

