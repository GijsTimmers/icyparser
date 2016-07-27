## icyparser

A script to retrieve an Icecast/Shoutcast's ICY stream and relevant metadata.

### Installation

    $ sudo pip3 install icyparser

### Usage

- From the terminal: 

        $ icyparser URL

- From another Python script:
    
        from icyparser import IcyParser
        ip = IcyParser(url)
        ip.getIcyInformation()  ## returns a dictionary object

- Without installing:

        ./icyparser-runner.py URL
