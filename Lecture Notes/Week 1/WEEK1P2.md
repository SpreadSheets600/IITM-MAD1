## 📖 Quick Summary

**Key Takeaways** :

- Evolution of web technologies from early packet-switched networks to modern Web 3.0
- Key protocols (TCP/IP, HTTP) form the foundation of internet communication
- Web servers handle client requests through standardized ports and protocols
- Performance considerations include latency, response size, and memory management
- IPv4 and IPv6 addressing schemes enable global device connectivity
- Web has transformed from static pages to dynamic, interactive applications

## 📒 Notes

## Web

### Historical Background

### **Telephone Networks ~ 1890 +**

- Circuit Switching - Allows A to talk with B though complex switching network.
- Physical wires tied up for duration of call even if nothing said.

### **Packet Switched Networks ~ 1960 +**

- Data divided into packets, each routed independently through network
- More efficient use of network resources - links shared between multiple communications
- Foundation for modern internet communication

### **ARPANet ~ 1969 +**

- Node to node network
- Mostly used in universities and military
- Pioneered packet switching and TCP/IP protocols

### **Others**

- IBM SNA, Digital DECNet, Xerox XNS - Early proprietary networking protocols and systems that contributed to network evolution
- Each had unique features but eventually gave way to TCP/IP standardization

### Protocol

A protocol is a set of rules and standards that define how data is transmitted between different devices in a network. 

It establishes the format, timing, sequencing, and error control in data communication. 

In networking, protocols are essential as they ensure reliable and consistent communication between diverse systems.

- Key protocols include TCP/IP (Transmission Control Protocol/Internet Protocol), HTTP (Hypertext Transfer Protocol), and FTP (File Transfer Protocol)
- Protocols operate at different layers of the OSI model, each handling specific aspects of network communication
- Each network had its own protocol

### Inter Network Protocol

- How to communicate between different network protocol
- Replace all the different protocols with one single inter network protocol
- TCP/IP (Transmission Control Protocol/Internet Protocol) emerged as the universal protocol for internetworking
- Standardization of TCP/IP allowed different networks to communicate seamlessly
- This became the foundation of the modern internet, enabling global connectivity

### IP - Internet Protocol - 1983

- Defines header, packet types and interpretation
- Can be carried over different underlying networks
- Provides addressing and routing mechanisms for data packets across networks
- Ensures packets reach their intended destinations through best-path routing

### TCP - Transmission Control Protocol - 1983

- Establish reliable communication and error controlling
- Automatically scale and adjust the network limits
- Handles data segmentation, sequencing, and reassembly for reliable end-to-end communication
- Provides flow control to prevent network congestion and data overflow

### Domain Names - 1985

- use names instead of IP addresses
- Easy to remember .com revolution still in the future
- Hierarchical system translates human-readable domain names to numeric IP addresses
- DNS (Domain Name System) provides distributed database for domain name resolution
- Enables scalable and decentralized management of internet addressing

### Hypertext - 1989 +

- Formatting hints inside document to link to other documents
- Links between documents allow easy navigation and cross-referencing
- Tim Berners-Lee developed HTML and HTTP for document sharing at CERN
- Created foundation for World Wide Web with linked documents and resources

## The World Wide Web ( WWW )

The World Wide Web, invented by Tim Berners-Lee in 1989, revolutionized how we access and share information over the Internet.

 It introduced a standardized way to create, format, and link documents using HTML (HyperText Markup Language) and HTTP (HyperText Transfer Protocol). 

This system allowed for the creation of websites that could be accessed through web browsers, making information sharing more intuitive and accessible to the general public.

### The Original Web - 1990 +

- Static pages
- Complicated executable interfaces
- Limited styling
- Browser capability issues

### Web 2.0 - 2004 +

- Dynamic pages - generate on fly
- HTTP as a transport mechanism - binary data & serialized objects
- Client side computation and rendering
- Rich user interfaces with advanced interactivity
- Social features and user-generated content
- Integration with databases and external services

### Web 3.0 - 2014 +

- Decentralized and blockchain-based applications
- Semantic web with AI-powered data interpretation
- Enhanced privacy and user data control
- Integration of virtual and augmented reality
- Focus on personalization and context-aware services

### NOTES :

- TCP is connection-oriented, requiring a virtual connection before communication begins.
- In contrast, UDP is connectionless—it simply sends packets without ensuring reliability, which can lead to data loss.
- TCP requires acknowledgment of received data. TCP/IP functions as a session initiation protocol.
- ARPANET (Advanced Research Projects Agency Network) pioneered networking protocols—the rules defining how data packets are formatted and transmitted.
- IP serves as a bridge between different network protocols by establishing a standardized header format.
- The Internet is a vast network of networks connecting devices worldwide, while the World Wide Web (WWW) uses the Internet to deliver webpages (via HTTPS and other protocols) to users.
- The WWW is essentially a collection of interconnected webpages.

## How The Web Works ?

### Web Server

A web server is a software or hardware system that stores, processes, and delivers web content to users over the Internet.

It responds to client requests (typically from web browsers) using HTTP/HTTPS protocols. 

Web servers handle tasks like serving static files, processing dynamic content, and managing concurrent connections from multiple users.

**Software :** 

- Listens for incoming network connections at a fixed port
- Responds in specific ways and opening network connection ports already known to the OS

**Protocol :** 

- What should client ask the server
- How should it respond to client calls / requests

**Ports :**

- It is assign a number between 0 and 65535, i.e.  $2^{16} -1$
- In computer networking, ports are numerical identifiers that enable different applications and services to share network resources on the same device.
- Standard port numbers are assigned for common services (e.g., HTTP uses port 80, HTTPS uses port 443).
- Ports help manage multiple network connections simultaneously and ensure data reaches the correct application.

### HTTP

- **Hypertext**
    - Regular text document
    - Contains codes inside that indicate special functions
    - Links to other documents or resources embedded within the text
    - Allows for non-linear reading and navigation through content
- HyperText Transfer Protocol
    - Client requests and servers responds with hypertext document
    - Protocol for transferring hypertext documents over the internet
    - Uses request-response model between client and server
    - Defines methods like GET, POST, PUT, DELETE for different operations

![image](https://github.com/user-attachments/assets/f9594892-ea3b-4193-b9e5-210d2933b44e)

### NOTES :

- FTP (File Transfer Protocol) and HTTP have different approaches to handling connections.
- HTTP is a stateless protocol—it sends requests and the server responds based on the current state.
- In contrast, FTP is stateful—the client maintains an ongoing connection with the server and will resend requests if no response is received.
- Common stateless protocols include HTTP, UDP, and DNS, while stateful protocols include FTP and Telnet.
- In stateless protocols, clients and servers are loosely coupled, making the server design simpler and faster than stateful systems.
- Standard ports used are:
    - HTTP: Port 80
    - FTP: Port 21
- Popular web servers include Apache, Nginx, Boa, FoxServ, Lighttpd, Microsoft IIS, Savant, and Mongoose.
- The Internet is an interconnected network of devices, while the World Wide Web (WWW) is a collection of resources (like webpages) accessed through the Internet.
- While the WWW requires the Internet for browsing, the Internet supports many other services like IoT devices and FTP.

### Simple Web Server

```bash
while true; 
	do echo -e "HTTP/1.1 200 OK\n\n $(date)" | nc -l localhost 1500; 
done 
```

- This simple web server code creates a basic HTTP server that listens on localhost port 1500. When a client connects, it responds with a 200 OK status and the current date.
- While this is a minimal example, it demonstrates the fundamental concept of how web servers listen for and respond to HTTP requests.

```bash
curl http://localhost:1500
```

### Loopback Devices

- Referred to as virtual network interfaces that allow a computer to communicate with itself.
- The most common loopback address is 127.0.0.1, which is often referred to as "localhost". This interface is crucial for testing network applications and services locally before deploying them to actual networks.

### CGI - Common Gateway Interface

- It is  an interface specification that enables web servers to execute an external program, typically to process user requests.

## Protocols

- A protocol is a set of rules and standards that govern how data is transmitted between devices in a network.
- These rules define everything from how the initial connection is established to how data is formatted, encrypted, and error-checked during transmission.
- Common protocols like TCP/IP, HTTP, and FTP each serve specific purposes in network communication, forming the foundation of modern internet infrastructure.
    - Network protocols can be categorized into different layers based on their function (Application, Transport, Network, etc.)
    - Each protocol has specific roles and responsibilities in the communication process
    - Protocols ensure interoperability between different devices and systems

### HTTP - Hypertext Transfer Protocol

- HTTP is a foundational protocol of the World Wide Web that enables clients (usually web browsers) to communicate with web servers.
- It follows a request-response model where clients send requests for resources, and servers respond with the requested data along with status information.
- The protocol is stateless, meaning each request-response cycle is independent and the server doesn't maintain information about previous requests.

**Requests Are Specified As :** 

- GET  - Used to retrieve data from the server without modifying any resources - **simple requests**
- POST - Used to submit data to the server for processing, often from HTML forms -  **more complex form data**
- PUT - Similar to POST but used to update existing resources at a specific URL. If the resource doesn't exist, PUT will create it -

## Performance Of Websites

### Latency

- Speed of light in vacuum 3e8 m/s ( $3 * 10^8$ )
- Speed of light in cable ~2e8 m/s ( $2 * 10^8$ )
- What it means is -
    - To cover a distance of 1000 km it will take around 5 ms
    - 5 ns / m ⇒ 5 ms for 1000 km
- For example there is a data center  2000 km away ⇒
    - For one way request it will take about 10 ms ( $\text{Time} = \frac{2 \times 10^6 \text{ meters}}{2 \times 10^8 \text{ m/s}} = 10 \times 10^{-3} \text{ seconds} = 10 \text{ ms}$ )
- **Round Trip Time ( RTT ) :** Refers to the total time it takes for a signal to travel from a source to a destination and back again.
    - In practice, actual latency is often higher due to additional network processing, routing, and queuing delays at various points along the path.
    - This physical constraint of light speed creates a fundamental lower bound for network latency that cannot be overcome.
- Larger responses require more time to transmit and process
- Response size directly impacts download time and bandwidth usage
- Compression and optimization techniques can help reduce response size

### Response Size

- Response size affects website performance in several ways:
    - Larger files take longer to download and process
    - Increases server load and bandwidth consumption
    - Can impact user experience, especially on slower connections
- Content delivery networks (CDNs) and caching strategies can help optimize response size and delivery

### Memory

- Memory management is crucial for website performance as it affects how efficiently resources are utilized.
- Browser memory usage impacts page load times and overall responsiveness. Proper memory management includes clearing unused resources, managing DOM elements efficiently, and avoiding memory leaks in JavaScript code.
- Key memory considerations include:
    - Managing browser cache effectively
    - Minimizing memory leaks in web applications
    - Efficient allocation and deallocation of resources

### Internet Protocol - IP

- IP (Internet Protocol) is a fundamental networking protocol that enables data routing and addressing across networks.
- It provides unique addresses (IP addresses) to identify devices and determines how data packets should be routed from source to destination.
- The protocol operates at the network layer and works in conjunction with other protocols like TCP to ensure reliable data transmission.

### IPv4

- IPv4 (Internet Protocol version 4) uses **32-bit addresses**, typically written in four octets (e.g., 192.168.1.1).
- This addressing scheme allows for approximately 4.3 billion unique addresses, though this limit has led to the development of IPv6.
- IPv4 remains widely used and employs various techniques like NAT (Network Address Translation) to manage address scarcity.

### IPv6

- IPv6 (Internet Protocol version 6) is the next generation of IP addressing, using 128-bit addresses that provide an vastly larger address space compared to IPv4.
- Written in hexadecimal notation (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334), IPv6 can support approximately 340 undecillion unique addresses.
- This expanded capacity helps address IPv4's limitations and better supports the growing number of Internet-connected devices.
- The IPv6 has groups of four hexadecimal digits ( $4 \times 4 = 16 \text{ bits}$ ) which are seperated by colons.
- The groups are :
    - Hextets
    - Hexadectets
    - Quibble
    - Quad-Nibble

### Port Numbers

- Port numbers are crucial identifiers that help direct network traffic to specific applications or services running on a device.
- They range from 0 to 65535, with well-known ports (0-1023) reserved for common services like HTTP (80) and HTTPS (443). Dynamic ports (49152-65535) are used for temporary connections.
- Common well-known ports include:
    - HTTP : 80
    - HTTPS : 443
    - FTP : 21
    - SSH : 22
    - SMTP : 25
