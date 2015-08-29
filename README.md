
![](https://github.com/galkan/flashlight/blob/master/images/flashlight.png "Flashlight") Automated Information Gathering Tool for Penetration Testers 
=====


Pentesters spends too much time during information gathering phase. Flashlight (Fener) provides to scan network/ports and gather information rapidly on network. So Flashlight can be preferred to automate discovery step on penetration testing. In this article, usage of Flashligh application will be examined.
For more information about usage Flashlight, "-h" or "-help" option can be used.


<p>
    Parameters for the usage of this application can be listed below
</p>
<ul>
<li>
-h, --help: It shows information about the use of the Flashlight application.
</li>
<li>
-p &lt;ProjectName&gt; or --project &lt; ProjectName&gt;: It sets project name with the name given. This paramater can be used to save different projects
    in different workspaces.
</li>
<li>
-s &lt;ScanType&gt; or –scan_type &lt; ScanType &gt;: It sets the type of scanning. There are four types of scanning: Active Scanning , Passive Scanning,
    Screenshot Scaning, Filtering. These types of scanning will be examined later in detail.
</li>
<li>
-d &lt; DestinationNetwork&gt;, --destination &lt; DestinationNetwork &gt;: It sets network or IP where the scaning will be examined.
</li>
<li>
-c &lt;FileName&gt;, --config &lt;FileName&gt;: It specifies the configuration file. The scanning is realized according to the information in the
    configuration file.
</li>
<li>
-u &lt;NetworkInterface&gt;, --interface &lt; NetworkInterface&gt;: It sets network interface on passive scanning.
</li>
<li>
-f &lt;PcapFile&gt;, --pcap_file &lt; PcapFile &gt;: It sets cap File that will be filtered.
</li>
<li>
-r &lt;RasterizeFile&gt;, --rasterize &lt; RasterizeFile&gt;: It sets the specific location of Rasterize JavaScript file which will be used for taking
    screenshots
</li>
<li>
-t &lt;ThreadNumber&gt;, --thread &lt;Threadnember&gt;: It sets the number of Thread. This parameter is valid only on screenshot screening (screen scan)
    mode.
</li>
<li>
-o &lt;OutputDiectory&gt;, --output &lt; OutputDiectory &gt;: It sets the directory in which the scan results can be saved. The scanning results are
    saved in 3 subdirectory : For Nmap scanning results, "nmap" subdirectory, for PCAP files "pcap" subdirectory and for screenshots "screen" subdirectories
    are used. Scanning results are saved in directory, shown under the output directories by this parameter. If this option is not set. Scaning results are
    saved in the directory that Flashlight applications are running.
</li>
<li>
-a, --alive: It performs ping scan to discover up IP address before scanning. It is used for active scan.
</li>
<li>
-g &lt;DefaultGateway&gt;, --gateway &lt; DefaultGateway &gt;: It identifies IP address of gateway. If not set, gateway for specified interface with “-I”
    parameter is choosen.
</li>
<li>
-l &lt;LogFile&gt;, --log &lt; LogFile &gt;: It specifies log file to save scan results. If not set, logs are saved in “flashlight.log” file in working
    directory.
</li>
<li>
-k &lt;PassiveTimeout&gt;, --passive_timeout &lt;PassiveTimeout&gt;: It specifies timeout for sniffing in passive mode. Default value is 15 sconds.This
    parameter is used for passive scan.
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
<p>
    Flashlight application can perform 3 basic scan type and 1 analysis. Each of them are listed below.
</p>




- Active scan  
This method uses nmap in background to actively discover host in target network. Different nmap scan techniques are preconfigured and used in automated way. All scan resuls are saved in 3 different nmap report formats for later inspection. 
- Passive scan  
This method is used for stealty network discovery. No packet is send during this scan. Only network traffic is sniffed and analyzed to discover assets. This methos optionally can use arpsoof to perform man-in-the-middle and listen all network traffic. 
- Screenshot scan   
This method is used to quickly discover web applications in target network. Quick port scan is performed to discover open web ports and then screenshots of discovered web pages is taken and saved in output directory. With this method all web pakes in target network can be archived and examined offline. 


