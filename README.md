## icyparser

A script to retrieve an Icecast/Shoutcast's ICY stream and relevant metadata.

### Installation

    $ sudo python3 setup.py install

### Usage

- From the terminal: 

        $ icyparser URL

- From another Python script:
    
        from icyparser import icyparser
        icyparser(url)

- Without installing:

        ./icyparser-runner.py URL
