# Q&A

## When might you use sed, awk and cut together?

Extract/replace/delete some part of a line/text.

Example get the time of the Nginx's log then print out as HH-MM format 

```
# Sample
202.61.222.153 - - [17/Dec/2016:06:29:22 +0000] "GET /api/test HTTP/1.1" 200 304 "-" "-" "api.example.com" 0.099 "52.201.164.65:443" -

# You want to get 06:29 (HH:MM) but then print out as 06-29
echo '202.61.222.153 - - [17/Dec/2016:06:29:22 +0000] "GET /api/test HTTP/1.1" 200 304 "-" "-" "api.example.com" 0.099 "52.201.164.65:443" -' | awk '{print $4}' | cut -c14-18 | sed 's/:/-/g'
06-29
```

## What is your favourite text editor and why?

I use `vim` for 80% of the time with a couple of main reasons

- it is one of the most powerful text editor with tons of useful plugins.
- it is default on many servers.
- I perfer to use keyboard most of the time.

But I also use `Sublime Text` sometime when I am tired with the keyboard and and to click and scroll with my mouse. Or when writting markdown document since I like the way it pre-render the text.

For me the text editor just a tool. I only want something stable, easy to use and support multiple platforms. I will not join the fight between `vim` vs. `sublime` since it is just personal taste.

## What steps would you take to configure a server to use Apache and Tomcat?

I have not worked with Java app for a while, but the most basic steps are

- check the requirements from the tool. Eg Tomcat requires Java
- check the latest stable version on the OS (Ubuntu 14.04, 16.04?)
    - if you have a preferred version of Apache or Tomcat then it would be easier
- pick the method to install for example from the default repo or custom repo using apt-get or manually setup using the binary build
- think about how will you manage the services like Apache was support by upstart/init.d by default but if you want to setup Tomcat manually then you may have to config an upstart script for it.
- tweak the service setting depends on the server size, type like the number of concurences processes, maximum heapsize, etc

## Users begin complaining about "slowness" on your web application. What steps would you take to investigate this?

Let's say you have a standard web app stack with HTTP loadbalancer, Nginx reversed proxy, Tomcat, MySQL.

Depends on the information you have about your system, application then you can identify the root of the "slowness". It can be from one layer or many layers. Can be app servers high load, can be database high load because of high traffic than usual or just because of a bad SQL query. 

If you have application monitoring (like NewRelic, ScoutApp, etc) or not since those tools allow you to see many metrics from deeper layer of application level. So most of the time you will find the bottleneck there, maybe from a slow query, or the server is out of memory because memory leak, etc

But if you don't have 3rd app monitoring then what you can do is

### Check the app servers, database servers load

Can easily grab those information if you have a server monitoring system like Zabbix, NewRelic, etc 

If you are lucky then you can see the app servers are out of memory or the MySQL are on high IO write load, etc

### Verify from command line, browers console or 3rd service like https://tools.pingdom.com/ to know how slow is the web

If you have a website then I recommended you to use https://tools.pingdom.com/ or https://www.webpagetest.org/ to check the load speed from specific location like in the US or Singapore.

You will find some slow endpoints or all of the requests to your web/api servers are slow. But the idea is to verify if it is really slow and which part of it is slow.

### Check the log from all level HTTP load balancer, Nginx, Tomcat, MySQL

Maybe only one endpoint was slow and it cause the whole web page load slower or the whole API was slow.

There is must be something related to a kind of exception or slow query from the application log. Then you can have more info to conclude.

