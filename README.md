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

## Edit Configuration
Copy the [example configuration](src/conf/config-example.yml) to
`src/conf/config.yml`, and edit the parameters to reflect your
desired configuration.

## Usage
```shell
cd src
python3 ./main.py
```