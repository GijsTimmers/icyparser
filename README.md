## icyparser

A script to retrieve an Icecast/Shoutcast's ICY stream and relevant metadata.

### Installation

    $ sudo pip3 install icyparser

### Usage

    >>> from icyparser import IcyParser
    >>> ip = IcyParser()
    >>> ip.getIcyInformation(url) ## starts thread, values become acccessible
    >>> print(ip.icy_streamtitle)
    Bonobo - Cirrus
    >>> print(ip.icy_genre)
    Alternative
    >>> ip.stop()                 ## stops thread
    


