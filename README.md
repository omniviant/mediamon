# mediamonitor
Download all the things. I'm too lazy to document this right now,
so either read the code to figure out how to use it, or wait until
I tag an "official" release.

## Install
```shell
git clone https://github.com/omniviant/mediamon
cd mediamon/src
pip install -r requirements.txt
```

## Configuration
Copy the [example configuration](src/conf/config-example.yml) to
`src/conf/config.yml`, and edit the parameters to reflect your
desired configuration.

## Usage
```shell
cd src
python3 ./main.py
```

## Contributors
- [monanon](https://github.com/monanon)

## Development
```shell
git clone https://github.com/omniviant/mediamon.git
git checkout dev-somebranchname
pip install -r src/requirements.txt
pip install -r src/requirements-dev.txt

pylint src/
flake8 src/
bandit -r src/

pytest -v tests/
```