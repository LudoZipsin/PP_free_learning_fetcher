# PacktPub free learning fetcher
A little script to automate the claiming of free ebook from packtpub

## motivation

[PacktPub](https://www.packtpub.com/) is just awesome, the quality of their book is just great, they are easy to read and there is almost dozen of book for every topics you'll want. I visit their site very often to see their newest books and paying for a subscription to gain access to their library worth every single dime it cost.

They also provide an offer: [free learning](https://www.packtpub.com/packt/offers/free-learning). Basically, they propose a free random ebook from their library every day. Yes, for FREE, without DRM or some other nasty thing. 

Most of the time, I visit their site every day in order to claim this free ebook. However, I travel a lot, and sometime I can't have access to an internet connection and I miss the daily free ebook. And since Murphy is always there to have a fun, most of the time it is an ebook about the technologies I really want to learn more. 

So I wrote this little script to never miss one of those. Hope it will be helpfull.

## dependencies

For the script, we use `lxml`, `robobrowser`, `beautifulsoup` and `requests`. If one of them is missing from your system, the script will not run, so please fix these dependencies before.

I use `python 3` however the script may be used with `python 2` with some minor corrections (feel free to hack it)

## How to

Just put this on one of your computer/server/pi that will always have an access to internet. Make it executable and replace your `user_mail` and `user_password` form `to complete` to your account informations. Finally, put this in a cron task and here you are.
