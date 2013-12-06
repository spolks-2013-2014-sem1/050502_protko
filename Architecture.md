Architecture overview
================================

Main goal of my implementation, is to separate business logic from network layer. Business just need to convert `Request` object to `Response`, and server will handle it's delivering. This is adds flexibility for server, as we may change implementation without need of changing logic of our application.

##nonblocking IO and TCP
We need to implement set of IO Workers to handle concurrent connections.

##nonblocking IO and UDP
Within this research we do not trying to implement congestion control for UDP. thereon, as well as UDP have single socket for reading and writing data, there is no need of IO control.
