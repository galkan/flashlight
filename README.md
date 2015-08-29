
![](https://github.com/galkan/flashlight/blob/master/images/flashlight.png "Flashlight") Automated Information Gathering Tool for Penetration Testers 
=====

Pentesters spends too much time during information gathering phase. Flashlight (Fener) provides to scan network/ports and gather information rapidly on network. So Flashlight can be preferred to automate discovery step on penetration testing. In this article, usage of Flashligh application will be examined.

For more information about usage Flashlight, "-h" or "-help" option can be used.

<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-01.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-01.jpg" style="width: 50%;" /></a>

Parameters for the usage of this application can be listed below

<ul>
<li>
-h, --help: It shows information about the use of the Flashlight application.
</li>
<li>
-p &lt;ProjectName&gt; or --project &lt; ProjectName&gt;: It sets project name with the name given. This paramater can be used to save different projects in different workspaces.
</li>
<li>
-s &lt;ScanType&gt; or –scan_type &lt; ScanType &gt;: It sets the type of scanning. There are four types of scanning: Active Scanning , Passive Scanning, Screenshot Scaning, Filtering. These types of scanning will be examined later in detail.
</li>
<li>
-d &lt; DestinationNetwork&gt;, --destination &lt; DestinationNetwork &gt;: It sets network or IP where the scaning will be examined.
</li>
<li>
-c &lt;FileName&gt;, --config &lt;FileName&gt;: It specifies the configuration file. The scanning is realized according to the information in the configuration file.
</li>
<li>
-u &lt;NetworkInterface&gt;, --interface &lt; NetworkInterface&gt;: It sets network interface on passive scanning.
</li>
<li>
-f &lt;PcapFile&gt;, --pcap_file &lt; PcapFile &gt;: It sets cap File that will be filtered.
</li>
<li>
-r &lt;RasterizeFile&gt;, --rasterize &lt; RasterizeFile&gt;: It sets the specific location of Rasterize JavaScript file which will be used for taking screenshots
</li>
<li>
-t &lt;ThreadNumber&gt;, --thread &lt;Threadnember&gt;: It sets the number of Thread. This parameter is valid only on screenshot screening (screen scan) mode.
</li>
<li>
-o &lt;OutputDiectory&gt;, --output &lt; OutputDiectory &gt;: It sets the directory in which the scan results can be saved. The scanning results are saved in 3 subdirectory : For Nmap scanning results, "nmap" subdirectory, for PCAP files "pcap" subdirectory and for screenshots "screen" subdirectories are used. Scanning results are saved in directory, shown under the output directories by this parameter. If this option is not set. Scaning results are saved in the directory that Flashlight applications are running.
</li>
<li>
-a, --alive: It performs ping scan to discover up IP address before scanning. It is used for active scan.
</li>
<li>
-g &lt;DefaultGateway&gt;, --gateway &lt; DefaultGateway &gt;: It identifies IP address of gateway. If not set, gateway for specified interface with “-I” parameter is choosen.
</li>
<li>
-l &lt;LogFile&gt;, --log &lt; LogFile &gt;: It specifies log file to save scan results. If not set, logs are saved in “flashlight.log” file in working directory.
</li>
<li>
-k &lt;PassiveTimeout&gt;, --passive_timeout &lt;PassiveTimeout&gt;: It specifies timeout for sniffing in passive mode. Default value is 15 sconds.This parameter is used for passive scan.
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

Flashlight application can perform 3 basic scan type and 1 analysis type. Each of them are listed below.

- 1) Passive Scan

In passive scan, no packets are sent to wire. This type of scan is used for listenning network and analyzing packets.

To launch a passive scan by using Flashlight; firstly project name should be specified like “passive-pro-01”. In the following command, packets that are captured by eth0 are saved into “/root/Desktop/flashlight/output/passive-project-01/pcap" directory as Pcap files and all logs are saved into "/root/Desktop/log" directory.

./flashlight.py -s passive -p passive-pro-01 -i eth0 -o /root/Desktop/flashlight_test -l /root/Desktop/log –v
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-02.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-02.jpg" style="width: 50%;" /></a>
 
After scanning a new directory is named as “flashlight_test" and log ile named as “log” are created in "/root/Desktop/" directory.
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-03.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-03.jpg" style="width: 50%;" /></a>
 
Directory structure of  “flashlight_test” is like below. PCAP file is saved into “/root/Desktop/flashlight_test/output/passive-pro-01/pcap” directory. This PCAP file can be used for analysis purpose.
ls /root/Desktop/flashlight_test -R
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg" style="width: 50%;" /></a>
 
Content of log file is like command line output:
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-04.jpg" style="width: 50%;" /></a>
 
During standard passive scanning Broadcast ackets and direct packets to scanning machines are captured. Beside this,by using “-mim/-m” parameter, Arp Spoof and MITM attack can be performed.
./flashlight.py -s passive -p passive-project-02 -i eth0 -g 192.168.74.2 -m -k 50 -v
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-06.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-06.jpg" style="width: 50%;" /></a>
 
By analyzing captured PCAP file HTTP traffic can be seen.
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-07.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-07.jpg" style="width: 50%;" /></a>
 
By decoding Basic authentication message, access informations for web server will be accessed.
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-08.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-08.jpg" style="width: 50%;" /></a>
 
All parameters during passive scanning is listed below.

./flashlight.py -s passive -p passive-pro-03 -i eth0 -g 192.168.74.2 -m -k 50 -o /root/Desktop/flashlight_passive_full -l /root/Desktop/log -v

- 2) Active Scan
During active scan, NMAP scripts are used by reading configuration fie. An example configuration file (flashlight.yaml) is stored in “config” directory in the working directory.
tcp_ports:
         - 21, 22, 23, 25, 80, 443, 445, 3128, 8080
udp_ports: 
         - 53, 161
scripts:
         - http-enum
screen_ports:
         - 80, 443, 8080, 8443
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-09.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-09.jpg" style="width: 50%;" /></a>
 
According to "flashlight.yaml" configuration file scaning occurs via "21, 22, 23, 25, 80, 443, 445, 3128, 8080" TCP ports, "53, 161" UDP ports, "http-enum" script by using NMAP. 
Note: During active scan “screen_ports” option is useless. This option works on screen scan.
“-a” option is usefull to discover up IPs/hosts by sending ICMP packets. Beside this, incrementing thread number by using “-t” parameter increases scan speed.
./flashlight.py -p active-project -s active -d 192.168.74.0/24 –t 30 -a -v
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-10.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-10.jpg" style="width: 50%;" /></a>
 
Bu tarama sonucunda belirtilen çıktı dizinine 4 farklı tarama türünün (İşletim sistemi taraması, Ping taraması, Port taraması ve Betik taraması) her biri için 3 farklı formatta (Normal, XML ve Grepable) dosya oluşturulur. 
By running this command 3 format (Normal, XML and Grepable) output files  for 4 different scan type (Operating system scan, Ping scan, Port scan and Script Scan) are created.
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-11.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-11.jpg" style="width: 50%;" /></a>
 
The commands that Flashlight Application runs are like these:
<ul>
<li>Operating System Scan: /usr/bin/nmap -n -Pn -O -T5 -iL /tmp/<IPListesineAitDosya> -oA /root/Desktop/flashlight/output/active-project/nmap/OsScan-<Tarih>
</li><li>Ping Scan: /usr/bin/nmap -n -sn -T5 -iL /tmp/<IPListesineAitDosya> -oA /root/Desktop/flashlight/output/active-project/nmap/PingScan-<Tarih>
</li><li>Port Scan: /usr/bin/nmap -n -Pn -T5 --open -iL /tmp/<IPListesineAitDosya> -sS -p T:21,22,23,25,80,443,445,3128,8080,U:53,161 -sU -oA /root/Desktop/flashlight/output/active-project/nmap/PortScan-<Tarih>
</li><li>Script Scan: /usr/bin/nmap -n -Pn -T5 -iL /tmp/<IPListesineAitDosya> -sS -p T:21,22,23,25,80,443,445,3128,8080,U:53,161 -sU --script=default,http-enum -oA /root/Desktop/flashlight/output/active-project/nmap/ScriptScan-<Tarih>
</li>
<ul>

<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-12.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-12.jpg" style="width: 50%;" /></a>
 
To run effective and optimized active scan, “-n” parameter can be used:
./flashlight.py -p active-project -s active -d 192.168.74.0/24 -n -a –v
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-13.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-13.jpg" style="width: 50%;" /></a>
By using “-n” parameter, used additional NMAP options are shown as below. 
… -min-hostgroup 64 -min-parallelism 64 -host-timeout=300m -max-rtt-timeout=600ms -initial-rtt-timeout=300ms -min-rtt-timeout=300ms -max-retries=2 -min-rate=150 …


- 3) Ekran Görüntüsü Taraması
Screen Scan is used to get screenshots on web sites by using configurations in config file (flashlight.yaml). Configurations in this file provide screen scan for 4 ports ("80, 443, 8080, 8443") 
screen_ports:
         - 80, 443, 8080, 8443
Sample screen scan is like this:
./flashlight.py -p project -s screen -d 192.168.74.0/24 -r /usr/local/rasterize.js -t 10 -v
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-14.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-14.jpg" style="width: 50%;" /></a>
 
By running this command 3 web applications are detected. Screenshots of these web sites are saved in “screen” sub folder. These screenshts can be used for offline analysis.
<a href="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-15.jpg"><img src="http://www.siberportal.org/wp-content/uploads/2015/08/flashlight-automated-information-gathering-tool-for-penetration-testers-15.jpg" style="width: 50%;" /></a>
 

- 4) Filtreleme
Filtering option is used to analyse pcap files. An example for this option is shown as below:

./flashlight.py -p filter-project -s filter -f /root/Desktop/flashlight/output/passive-project-02/pcap/20150815072543.pcap -v


By running this command some files are created on “filter” sub folder.

This option analyzes PCAP packets according to below properties:
<ul>
<li>Windows hosts</li>
<li>Top 10 DNS requests</li>
</ul>
...







