
![](https://github.com/galkan/flashlight/blob/master/images/flashlight.png "Flashlight") Automated Information Gathering Tool for Penetration Testers 
=====

### Videos :

https://www.youtube.com/watch?v=EUMKffaAxzs&list=PL1BVM6VWlmWZOv9Hv8TV2v-kAlUmvA5g7&index=4
https://www.youtube.com/watch?v=qCgW-SfYl1c&list=PL1BVM6VWlmWZOv9Hv8TV2v-kAlUmvA5g7&index=5
https://www.youtube.com/watch?v=98Soe01swR8&list=PL1BVM6VWlmWZOv9Hv8TV2v-kAlUmvA5g7&index=6
https://www.youtube.com/watch?v=9wft9zuh1f0&list=PL1BVM6VWlmWZOv9Hv8TV2v-kAlUmvA5g7&index=7

Pentesters spend too much time during information gathering phase. Flashlight (Fener) provides services to scan network/ports and gather information rapidly on target networks. So Flashlight should be the choice to automate discovery step during a penetration test. In this article, usage of Flashligh application will be explained.

For more information about using Flashlight, "-h" or "-help" option can be used.



Parameters for the usage of this application can be listed below

<ul>
<li>
-h, --help: It shows the information about using the Flashlight application.
</li>
<li>
-p &lt;ProjectName&gt; or --project &lt; ProjectName&gt;: It sets project name with the name given. This paramater can be used to save different projects in different workspaces.
</li>
<li>
-s &lt;ScanType&gt; or –scan_type &lt; ScanType &gt;: It sets the type of scans. There are four types of scans: Active Scan , Passive Scan, Screenshot Scan and Filtering. These types of scans will be examined later in detail.
</li>
<li>
-d &lt; DestinationNetwork&gt;, --destination &lt; DestinationNetwork &gt;: It sets the network or IP where the scan will be executed against.
</li>
<li>
-c &lt;FileName&gt;, --config &lt;FileName&gt;: It specifies the configuration file. The scanning is realized according to the information in the configuration file.
</li>
<li>
-u &lt;NetworkInterface&gt;, --interface &lt; NetworkInterface&gt;: It sets the network interface used during passive scanning.
</li>
<li>
-f &lt;PcapFile&gt;, --pcap_file &lt; PcapFile &gt;: It sets cap File that will be filtered.
</li>
<li>
-r &lt;RasterizeFile&gt;, --rasterize &lt; RasterizeFile&gt;: It sets the specific location of Rasterize JavaScript file which will be used for taking screenshots.
</li>
<li>
-t &lt;ThreadNumber&gt;, --thread &lt;Threadnember&gt;: It sets the number of Threads. This parameter is valid only on screenshot scanning (screen scan) mode.
</li>
<li>
-o &lt;OutputDiectory&gt;, --output &lt; OutputDiectory &gt;: It sets the directory in which the scan results can be saved. The scan results are saved in 3 sub-directories : For Nmap scanning results, "nmap" subdirectory, for PCAP files "pcap" subdirectory and for screenshots "screen" subdirectories are used. Scan results are saved in directory, shown under the output directories by this parameter. If this option is not set, scan results are saved in the directory that Flashlight applications are running.
</li>
<li>
-a, --alive: It performs ping scan to discover up IP addresses before the actual vulnerability scan. It is used for active scan.
</li>
<li>
-g &lt;DefaultGateway&gt;, --gateway &lt; DefaultGateway &gt;: It identifies the IP address of the gateway. If not set, interface with “-I” parameter is chosen.
</li>
<li>
-l &lt;LogFile&gt;, --log &lt; LogFile &gt;: It specifies the log file to save the scan results. If not set, logs are saved in “flashlight.log” file in working directory.
</li>
<li>
-k &lt;PassiveTimeout&gt;, --passive_timeout &lt;PassiveTimeout&gt;: It specifies the timeout for sniffing in passive mode. Default value is 15 seconds. This parameter is used for passive scan.
</li>
<li>
-m, --mim: It is used to perform MITM attack.
</li>
<li>
-n, --nmap-optimize: It is used to optimize nmap scan.
</li>
<li>
-v, --verbose: It is used to list detailed information.
</li>
<li>
-V, --version: It specifies version of the program.
</li>
</ul>


<h3> Installation </h3>
```
apt-get install nmap tshark tcpdump dsniff
```

In order to install phantomjs easily, you can download and extract it from https://bitbucket.org/ariya/phantomjs/downloads. 


Flashlight application can perform 3 basic scan types and 1 analysis type. Each of them are listed below.

<h2> 1) Passive Scan </h2>

In passive scan, no packets are sent into wire. This type of scan is used for listening network and analyzing packets.

To launch a passive scan by using Flashlight; a project name should be specified like “passive-pro-01”. In the following command, packets that are captured by eth0 are saved into “/root/Desktop/flashlight/output/passive-project-01/pcap" directory, whereas, Pcap files and all logs are saved into "/root/Desktop/log" directory.

```
./flashlight.py -s passive -p passive-pro-01 -i eth0 -o /root/Desktop/flashlight_test -l /root/Desktop/log –v
```

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-02.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-02.jpg" style="width: 50%;" /></a></center>
</p>

When the scan is completed a new directory, named “flashlight_test" and a log file, named “log”, are created in "/root/Desktop/" directory.

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-03.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-03.jpg" style="width: 50%;" /></a></center>
</p>


Directory structure of  “flashlight_test” is like below. PCAP file is saved into “/root/Desktop/flashlight_test/output/passive-pro-01/pcap” directory. This PCAP file can be used for analysis purposes.
ls /root/Desktop/flashlight_test -R

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg" style="width: 50%;" /></a></center>
</p>
 
 
Content of the log file is like command line output:
<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg" style="width: 50%;" /></a></center>
</p>


During standard passive scanning Broadcast packets and direct packets to scan machines are captured. Beside this, by using “-mim/-m” parameter, Arp Spoof and MITM attack can be performed.


```
./flashlight.py -s passive -p passive-project-02 -i eth0 -g 192.168.74.2 -m -k 50 -v
```

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-06.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-06.jpg" style="width: 50%;" /></a></center>
</p>

By analyzing captured PCAP file HTTP traffic can be seen.

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-07.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-07.jpg" style="width: 50%;" /></a></center>
</p>
 
By decoding Basic Authentication message, credentials denoting access information for web servers will be accessed.
<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-08.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-08.jpg" style="width: 50%;" /></a></center>
</p>

All parameters during passive scanning are listed below.

```
./flashlight.py -s passive -p passive-pro-03 -i eth0 -g 192.168.74.2 -m -k 50 -o /root/Desktop/flashlight_passive_full -l /root/Desktop/log -v
```


<h2> 2) Active Scan </h2>

During an active scan, NMAP scripts are used by reading the configuration file. An example configuration file (flashlight.yaml) is stored in “config” directory under the working directory.

tcp_ports:

       - 21, 22, 23, 25, 80, 443, 445, 3128, 8080

udp_ports: 

       - 53, 161

scripts:

       - http-enum

screen_ports:
       - 80, 443, 8080, 8443

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-09.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-09.jpg" style="width: 50%;" /></a></center>
</p>
 
According to "flashlight.yaml" configuration file, the scan executes against "21, 22, 23, 25, 80, 443, 445, 3128, 8080" TCP ports, "53, 161" UDP ports, "http-enum" script by using NMAP. 

<strong>Note:</strong> During active scan “screen_ports” option is useless. This option just works with screen scan.

“-a” option is useful to discover up hosts by sending ICMP packets. Beside this, incrementing thread number by using “-t” parameter increases scan speed.

```
./flashlight.py -p active-project -s active -d 192.168.74.0/24 –t 30 -a -v
```

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-10.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-10.jpg" style="width: 50%;" /></a></center>
</p>

By running this command; output files in three different formats (Normal, XML and Grepable) are emitted for four different scan types (Operating system scan, Ping scan, Port scan and Script Scan).

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-11.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-11.jpg" style="width: 50%;" /></a></center>
</p>

The example commands that Flashlight Application runs can be given like so:

<ul>
<li>Operating System Scan: /usr/bin/nmap -n -Pn -O -T5 -iL /tmp/"IPListFile" -oA /root/Desktop/flashlight/output/active-project/nmap/OsScan-"Date"
</li><li>Ping Scan: /usr/bin/nmap -n -sn -T5 -iL /tmp/"IPListFile" -oA /root/Desktop/flashlight/output/active-project/nmap/PingScan-"Date"
</li><li>Port Scan: /usr/bin/nmap -n -Pn -T5 --open -iL /tmp/"IPListFile" -sS -p T:21,22,23,25,80,443,445,3128,8080,U:53,161 -sU -oA /root/Desktop/flashlight/output/active-project/nmap/PortScan-"Date"
</li><li>Script Scan: /usr/bin/nmap -n -Pn -T5 -iL /tmp/"IPListFile" -sS -p T:21,22,23,25,80,443,445,3128,8080,U:53,161 -sU --script=default,http-enum -oA /root/Desktop/flashlight/output/active-project/nmap/ScriptScan-"Date"
</li>
<ul>

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-12.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-12.jpg" style="width: 50%;" /></a></center>
</p>

To run an effective and optimized active scan, “-n” parameter can be used:

```
./flashlight.py -p active-project -s active -d 192.168.74.0/24 -n -a –v
```

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-13.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-13.jpg" style="width: 50%;" /></a></center>
</p>

“-n” parameter adds additional NMAP options which are shown below;

<p><i><strong>… -min-hostgroup 64 -min-parallelism 64 -host-timeout=300m -max-rtt-timeout=600ms -initial-rtt-timeout=300ms -min-rtt-timeout=300ms -max-retries=2 -min-rate=150 … </i></strong></p>


<h2> 3) Screen Scan </h2>

Screen Scan is used to get screenshots of web sites/applications by using directives in config file (flashlight.yaml). Directives in this file provide screen scan for four ports ("80, 443, 8080, 8443") 

screen_ports:

       - 80, 443, 8080, 8443

Sample screen scan can be performed like this:

```
./flashlight.py -p project -s screen -d 192.168.74.0/24 -r /usr/local/rasterize.js -t 10 -v
```

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-14.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-14.jpg" style="width: 50%;" /></a></center>
</p>

For example, assume that by running this command three web applications are detected. Screenshots of these web sites are saved in “screen” sub folder. These screenshts can be used for an offline analysis.

<p>
<center><a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-15.jpg"><img  src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-15.jpg" style="width: 50%;" /></a></center>
</p>

<h2> 4) Filtering</h2>
Filtering option is used to analyse pcap files. An example for this option is shown below:

```
./flashlight.py -p filter-project -s filter -f /root/Desktop/flashlight/output/passive-project-02/pcap/20150815072543.pcap -v
```

By running this command some files are created on “filter” sub-folder.

This option analyzes PCAP packets according to below properties:
<ul>
<li>Windows hosts</li>
<li>Top 10 DNS requests</li>
</ul>
...

<h3> Thanks To: </h3>

- Bahtiyar Bircan
- Bedirhan Urgun
- Ertugrul Basaranoglu
- Johan Nestaas







