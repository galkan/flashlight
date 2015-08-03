
![](https://github.com/galkan/flashlight/blob/master/images/flashlight.png "Flashlight") Automated Information Gathering Tool for Penetration Testers 
=====


Flashlight (fener) is automated info gathering tool that can be used by penetration testers. Main purpose is to automate and speed up network discovery, port scanning and info gathering phase.
Fener gathers information with 3 different methods:

- Active scan  
This method uses nmap in background to actively discover host in target network. Different nmap scan techniques are preconfigured and used in automated way. All scan resuls are saved in 3 different nmap report formats for later inspection. 
- Passive scan  
This method is used for stealty network discovery. No packet is send during this scan. Only network traffic is sniffed and analyzed to discover assets. This methos optionally can use arpsoof to perform man-in-the-middle and listen all network traffic. 
- Screenshot scan   
This method is used to quickly discover web applications in target network. Quick port scan is performed to discover open web ports and then screenshots of discovered web pages is taken and saved in output directory. With this method all web pakes in target network can be archived and examined offline. 


