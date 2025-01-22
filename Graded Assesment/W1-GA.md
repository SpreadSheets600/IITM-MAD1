## Week 1 Graded Assesment

### 1. Components of the curl statement
**Question**: Consider the statement given below:
```
curl http://127.0.0.1:8080
```
Select the appropriate option that correctly identifies different components of the given statement.

**Explanation**: 
- **Protocol**: `http` - This specifies the protocol used for communication.
- **Host-name**: `127.0.0.1` - This is the IP address of the local machine.
- **Port**: `8080` - This is the port number on which the server is listening.
- **Command**: `curl` - This is the command-line tool used to make the HTTP request.

### 2. RTT Calculation
**Question**: Suppose a client machine C is communicating with a data center D located 12,500 km away from C. Assume that the TCP connection has been established and is kept alive. Calculate the RTT (Round trip time) in ms for an HTTP request. (Assume speed of light in cable is \(2 \times 10^8\) m/s).

**Explanation**: 
- **Distance**: 12,500 km = 12,500,000 meters
- **Speed of light in cable**: \(2 \times 10^8\) m/s
- **One-way time**: \(\frac{12,500,000 \text{ meters}}{2 \times 10^8 \text{ m/s}} = 62.5 \text{ ms}\)
- **RTT (Round Trip Time)**: \(2 \times 62.5 \text{ ms} = 125 \text{ ms}\)

### 3. Components of the given URL
**Question**: Consider the given URL below:
```
http://myserver.com/index.html?uid=10&sid=4032013
```
Select the appropriate option that correctly identifies different components of the given URL.

**Explanation**: 
- **Protocol**: `http` - This specifies the protocol used for communication.
- **Query-string**: `uid=10&sid=4032013` - This is the query string containing parameters.
- **Host-name**: `myserver.com` - This is the domain name of the server.
- **File-path**: `index.html` - This is the path to the requested resource.

### 4. True statements for a web browser
**Question**: Which of the following is/are true for a web browser?

**Explanation**: 
- A web browser is an application program to display web documents.
- A web browser sends an HTTP request and receives an HTTP response.

### 5. Order of tasks for an HTTP request
**Question**: Identify the correct order of the tasks that takes place when we request for `http://myserver.com/index.html`.

**Explanation**: 
1. The web browser connects to the DNS server to get the server IP address for `myserver.com`.
2. The web browser sends an HTTP request to the server, requesting a copy of `index.html`.
3. The server responds either with the requested resource or an error code.
4. The web browser assembles the response and displays it.

### 6. Responsibility of the view in MVC architecture
**Question**: The view in MVC architecture is responsible for ______.

**Explanation**: 
- The view is responsible for displaying the data.

### 7. Minimum bandwidth for the server
**Question**: Let A be a website that receives 10,000 requests in a second. If each request has to be sent a response of size 150kB, what should be the minimum bandwidth (approximately) of the server serving A?

**Explanation**: 
- **Requests per second**: 10,000
- **Response size per request**: 150 kB = 150,000 bytes
- **Total data per second**: \(10,000 \times 150,000 \text{ bytes} = 1,500,000,000 \text{ bytes} = 12 \text{ Gbps}\)

### 8. True statements
**Question**: Which of the following statements is/are true?

**Explanation**: 
- Internet Protocol (IP) is a set of rules that specifies one way to deliver data over the network.
- Domain Names are used in place of IP addresses.
- Hypertext is the text which contains links to other documents or websites.

### 9. Components of the webpage link
**Question**: Consider the webpage link shown below:
```
https://onlinedegree.iitm.ac.in/academics.html
```
Which among the following is/are true?

**Explanation**: 
- HTTPS is a protocol.
- `https://onlinedegree.iitm.ac.in/academics.html` is a URL.

### 10. Valid IPv4 addresses
**Question**: Which of the following is/are valid IPv4 address(es)?

**Explanation**: 
- Valid IPv4 addresses must be in the format `x.x.x.x` where `x` is a number between 0 and 255.
- Examples of valid addresses: `192.168.64.34`, `34.39.43.202`

I hope these explanations help! If you have any more questions or need further clarification, feel free to ask.
