# DeviantArt-watchRSS
Make deviant art easier to use, adding the capability to export your personal watcher as rss feeds.

##Installation
You need python version 2.7 or upper,
You need to install RoboBrowser
```shell
$ easy_install robobrowser
```
you need to patch the helpers file due to a bug
```shell
 # geany /usr/local/lib/python2.7/dist-packages/robobrowser/helpers.py
```
and adding at line 111
```python
  mdelay=3
  multiplier=2
```

After editing the two file with your data and put them in the right place on your raspberry pi or your server you can add on chrontab the task to launch dawatcher.py each hour.

```shell
@hourly python /path/devwatch.py
```

be sure to have apache well configured on the server because each time you want to see your WATCH you need to reach the folder where devwatch.php be.
For example http://mywebsite.com/folder/devwatch.php

finally you can make that wtch a rss using this amazing web site:

[Page2Rss http://page2rss.com/](http://page2rss.com/)

you need to pass as a paramether the url of the index.html page that the script generate.
For example http://mywebsite.com/folder/index.html

##Usage
Open your rssReader as feedly and past the link genrated from Page2Rss now you have a perfect feed from your watch in deviant art.

##Configuration

```shell
this var sets the output file that python use for working is not inteded to be used as a permanent saving file
OUTPUT_FILE='results.html'
your account on deviant art
USERNAME='USERNAME'
your password on deviant art
PSWD='pswd'
if the hosting is on another domain it must be specified the full path
HOSTING='http://www.miosito.com/folder/devwatch.php'
this key must be shared in the php file and in py file it must be secret and complex some example include (agnuenainubanopgmignnapdnaoing3q9ru83h93039ajf39hrionafuebho)
PERSONAL_KEY='some random character'
```

