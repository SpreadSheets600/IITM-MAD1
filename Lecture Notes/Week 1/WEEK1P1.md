## 📖 Quick Summary

**Key Takeaways** :

- A comprehensive introduction to mobile app development, covering different types of applications (desktop, mobile, web) and their key characteristics
- Detailed exploration of application components: storage, presentation, and communication systems
- In-depth analysis of software architectures, focusing on client-server and peer-to-peer models
- Overview of software design patterns, with particular emphasis on the MVC (Model-View-Controller) paradigm and its variations
- Discussion of architectural considerations including scalability, performance constraints, and system interactions

## 📒 Notes

## APPS ?!

- computer software or a program most commonly a small specific one used for mobile devices. The term app originally referred to any mobile or desktop application,
- but as more app stores have emerged to sell mobile apps to smartphone and tablet users, the term app has evolved to refer to small programs that can be downloaded and installed at once.
- **Program** - it’s a package to solve a problem, or in other terms it's a set of instructions that tells a computer how to perform specific tasks.
- Programs are written in programming languages that provide a structured way to create these instructions and control how the computer processes data and interacts with users.

### Desktop Applications

- These are usually standalone, editor, word processors, web browsers or mail clients.
- They are designed to run on desktop operating systems like Windows, macOS, or Linux and typically offer more comprehensive features and functionality compared to mobile apps.
- Desktop applications often have access to more system resources and can perform more complex operations, making them suitable for tasks like video editing, 3D modeling, and professional software development.
- They often work offline utilizing local data storage or with possible network connections.
- **SDK ( Software Development Kit )** are custom, OS specific frameworks that provide tools, libraries, and resources for developers to create applications for specific operating systems.
- They include APIs, development environments, and debugging tools essential for native app development.

### Mobile Applications

- These are applications targeted specifically towards running on mobile phones or tablets.
- **Constrains -**
    - They have limited screen size
    - user interaction ( audio, camera, touch )
    - limited memory processing power
    - limited battery life
- **Framework -**
    - OS Specific SDK ( Android Studio, XCode )
    - Cross Platform SDK ( Flutter, React Native )
- **Network -**
    - Usually network oriented requiring constant internet connectivity for real-time data updates, user authentication, and accessing cloud-based services.
    - This connectivity requirement affects app design and functionality, making offline capability an important consideration.

### Web Applications

- Web applications are software programs that run in web browsers, accessible through internet connections without requiring installation.
- They offer cross-platform compatibility since they work on any device with a modern web browser, making them highly accessible.
- Web apps are built using web technologies like HTML, CSS, and JavaScript, and can range from simple static pages to complex dynamic applications.
- **Key Features -**
    - Platform independence
    - No installation required
    - Easy updates and maintenance
    - Accessible from any device with a browser

## Components Of An APP

- Storage - The component responsible for managing and persisting data within the application, including local databases, file systems, and cloud storage solutions. This ensures data integrity and availability across sessions.
- Presentation - The user interface layer that handles how information is displayed to users and manages user interactions. This includes layouts, visual elements, animations, and responsive design considerations.
- Communication - The networking and data exchange component that manages interactions between different parts of the application, external services, and APIs. This includes handling requests, responses, and real-time data synchronization.

## Architectures

### 1. Client - Server Architecture

- **Server**
    - Stores Data for the clients
    - Provides data on demand
    - May or may not perform computations
- **Client**
    - Requests data from server
    - Handles user interface and interactions
    - Performs local computations and processing
- **Network**
    - Connects server to the client through various communication protocols and networking technologies, enabling data exchange and synchronization between them
    - It can be local network or internet based connection depending on the application's requirements and deployment setup
    - Different protocols like HTTP, WebSocket, or custom protocols may be used for communication

### **Client - Server Model**

- **Explicit Server**
    - A dedicated machine or system that provides services, resources, and data to clients across a network
    - Handles data storage, processing, and security management
    - Can serve multiple clients simultaneously while maintaining performance and reliability
- **Explicit Clients**
    - End-user devices or applications that request and consume services from the server, including web browsers, mobile apps, and desktop applications
    - Responsible for presenting data to users and handling user interactions while maintaining communication with the server
    - Can operate independently with local data caching when server connection is unavailable
- **Local System**
    - Server and client operate on the same machine using a local network
    - While not a traditional network, it functions conceptually as a networked system
- **Machine Clients**
    - Automated systems or devices that function as clients in a client-server setup, including IoT devices, sensors, and automated processes
    - These clients communicate with servers autonomously, following predetermined protocols and schedules
- **Variants**
    - Single-tier: All components (client, server, database) run on the same machine
    - Two-tier: Client directly communicates with server, typical in simple client-server applications
    - Three-tier: Adds a middle layer between client and server for better scalability and security
    - Multi-tier: Complex architectures with multiple specialized layers for different functionalities

### 2. Peer To Peer Architecture

- In peer-to-peer (P2P) architecture, all nodes act as both clients and servers, sharing resources directly without a central server.
- Each peer can request and provide services, creating a decentralized network where responsibilities are distributed equally among participants.
- Common examples include file-sharing networks, blockchain systems, and distributed computing platforms, where peers collaborate to achieve tasks without relying on centralized infrastructure.
- All the nodes on a peer to peer architecture are equivalent and equipoint, no one node is important than other.

### Notes :

- Client server architecture may be bottle - necked by high traffic at server.
- Peer to peer architecture are hard to choke, and can be fast if the peer is near us.
- Client server architecture may fail if the server fails, since there is no important node in peer to peer it will withstand most of the failures.
- Peer to peer architecture is very expensive to maintain but is good for redundancy and data safety.

## Software Architecture Patterns

### Design Pattern

- A general reusable solution to a commonly occurring problem within a given context in software design.
- Experienced designer observer the patterns in code
- Reusing these patterns can make design and development faster

**Metadata**

- Design patterns provide a shared vocabulary and proven solutions that help developers communicate and implement robust architectures more effectively.
- They encapsulate best practices developed over time by experienced software engineers. Common examples include MVC (Model-View-Controller), Singleton, and Observer patterns.

### M V C Paradigm

**Model - View - Controller**

- Model
    - Core data to be stored for the application
    - Mostly contains databases indexing for easy searching and manipulation
- View
    - User facing side of application
    - Interfaces for finding information, manipulating data
- **Controller**
    - Manages communication between Model and View components
    - Handles user input, processes business logic, and updates the Model and View accordingly
    - Acts as an intermediary that ensures separation of concerns between data management and presentation
- Controller is used to manipulate the model, the view observes and updates based on changes in the model.
- This creates a clear separation of responsibilities, where each component has a specific role in the application's architecture.
- The MVC pattern promotes maintainable and scalable code by reducing dependencies between different parts of the application.

### Other Design Paradigm

1. Model View Adapter
2. Model View Presenter
3. Model View Viewmodel
4. Hierarchical MVC
5. Presentation Abstraction Control
6. Resource View Coordinator
7. Entity Component System
8. Clean Architecture
