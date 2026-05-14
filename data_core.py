questions = [
    {
        "title": "REST vs GraphQL vs gRPC",
        "category": "Core Concepts",
        "tldr": "REST is resource-based and ubiquitous, GraphQL is query-based and solves over/under-fetching, while gRPC is highly performant and uses Protocol Buffers for service-to-service communication.",
        "explanation": """<p>Choosing the right API paradigm is critical for backend architecture.</p>
        <ul>
            <li><strong>REST (Representational State Transfer):</strong> Standard architecture using HTTP methods (GET, POST, PUT, DELETE) and endpoints mapped to resources. Great for public APIs.</li>
            <li><strong>GraphQL:</strong> A query language that lets clients request exactly what they need. Reduces multiple round-trips but adds complexity in caching and rate limiting.</li>
            <li><strong>gRPC:</strong> Developed by Google, runs over HTTP/2, and uses Protobuf (binary). Highly efficient, strongly typed, and ideal for internal microservices.</li>
        </ul>
        <table class="comparison-table">
            <thead>
                <tr><th>Feature</th><th>REST</th><th>GraphQL</th><th>gRPC</th></tr>
            </thead>
            <tbody>
                <tr><td>Payload</td><td>JSON / XML</td><td>JSON</td><td>Protobuf (Binary)</td></tr>
                <tr><td>Performance</td><td>Moderate</td><td>Moderate</td><td>High</td></tr>
                <tr><td>Use Case</td><td>Public APIs, CRUD</td><td>Complex UI, Mobile</td><td>Internal Microservices</td></tr>
            </tbody>
        </table>""",
        "diagram": """flowchart TB
    Client((Client)) -->|"REST: /api/users"| REST_API[REST API]
    Client -->|"GraphQL: query{user{id}}"| GQL_API[GraphQL Server]
    Client -->|"gRPC: GetUser()"| gRPC_API[gRPC Server]
    
    REST_API -. JSON .-> Client
    GQL_API -. JSON .-> Client
    gRPC_API -. Protobuf .-> Client
    
    classDef api fill:#1e2535,stroke:#6366f1,stroke-width:2px,color:#fff
    classDef client fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:#fff
    
    class REST_API,GQL_API,gRPC_API api
    class Client client"""
    },
    {
        "title": "Authentication vs Authorization",
        "category": "Core Concepts",
        "tldr": "Authentication confirms <strong>who you are</strong> (identity), while Authorization determines <strong>what you can do</strong> (permissions).",
        "explanation": """<p>Security is a two-step process:</p>
        <ul>
            <li><strong>Authentication (AuthN):</strong> The process of verifying a user's identity. This is typically done via passwords, biometric data, or multi-factor authentication (MFA).</li>
            <li><strong>Authorization (AuthZ):</strong> The process of verifying what specific applications, files, and data a user has access to. Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC) are common paradigms.</li>
        </ul>""",
        "diagram": """flowchart LR
    User([User]) -->|1. Provides Credentials| AuthN[Authentication]
    AuthN -->|2. Validates Identity| IdentityStore[(Identity DB)]
    IdentityStore -.->|3. Confirms Who| AuthN
    AuthN -->|4. Requests Resource| AuthZ[Authorization]
    AuthZ -->|5. Checks Permissions| RoleStore[(Roles/Permissions DB)]
    RoleStore -.->|6. Confirms Access Level| AuthZ
    AuthZ -->|7. Grants Access| Resource[Protected Resource]
    
    classDef process fill:#1e2535,stroke:#10b981,stroke-width:2px,color:#fff
    classDef db fill:#3b82f6,stroke:#1e40af,stroke-width:2px,color:#fff
    
    class AuthN,AuthZ process
    class IdentityStore,RoleStore db"""
    },
    {
        "title": "JWT vs Session-based Authentication",
        "category": "Core Concepts",
        "tldr": "Session-based auth is stateful (stored on server), whereas JWT is stateless (client stores token with a signed payload).",
        "explanation": """<p>These are the two dominant methods for maintaining user state across HTTP requests.</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Feature</th><th>Session-Based</th><th>JWT (Stateless)</th></tr>
            </thead>
            <tbody>
                <tr><td>State</td><td>Stateful (Stored in DB/Redis)</td><td>Stateless (Self-contained)</td></tr>
                <tr><td>Revocation</td><td>Easy (Delete session from DB)</td><td>Hard (Requires blacklists or short expiry)</td></tr>
                <tr><td>Scalability</td><td>Requires shared session store</td><td>Highly scalable, no DB lookups</td></tr>
                <tr><td>Security</td><td>Vulnerable to CSRF (if cookies)</td><td>Vulnerable to XSS (if stored in LocalStorage)</td></tr>
            </tbody>
        </table>
        <p><strong>Best Practice:</strong> Use sessions for high-security applications where immediate revocation is needed. Use JWTs for stateless microservices and mobile APIs.</p>"""
    },
    {
        "title": "OAuth 2.0 & OpenID Connect",
        "category": "Core Concepts",
        "tldr": "OAuth 2.0 is an authorization framework allowing third-party access (delegated access). OpenID Connect (OIDC) sits on top of OAuth to provide authentication (identity).",
        "explanation": """<p>OAuth 2.0 and OIDC power the modern "Log in with Google/GitHub" experience.</p>
        <ul>
            <li><strong>OAuth 2.0:</strong> Grants access tokens. It does NOT provide identity information. It just says "this app has permission to access your photos."</li>
            <li><strong>OpenID Connect (OIDC):</strong> An identity layer over OAuth 2.0. It provides an <code>id_token</code> (a JWT) that contains claims about the user (email, name).</li>
        </ul>
        <p>Common Grants: <code>Authorization Code Flow</code> (for web/mobile apps) and <code>Client Credentials Flow</code> (for machine-to-machine).</p>"""
    },
    {
        "title": "MVC Architecture",
        "category": "Core Concepts",
        "tldr": "Model-View-Controller separates an application into three interconnected components: Data (Model), UI (View), and Logic (Controller).",
        "explanation": """<p>MVC is a foundational software design pattern:</p>
        <ul>
            <li><strong>Model:</strong> Manages the data, logic, and rules of the application. Communicates with the database.</li>
            <li><strong>View:</strong> The user interface. Displays data to the user.</li>
            <li><strong>Controller:</strong> Handles user input, manipulates the model, and updates the view.</li>
        </ul>
        <p>In modern backend APIs, the "View" is often replaced by a JSON response, leading to patterns like Layered Architecture (Controller -> Service -> Repository).</p>"""
    },
    {
        "title": "Idempotency in APIs",
        "category": "Core Concepts",
        "tldr": "An API is idempotent if making multiple identical requests has the same effect as making a single request.",
        "explanation": """<p>Idempotency ensures that network retries (due to timeouts or failures) don't result in unintended side effects, such as a user being charged twice.</p>
        <ul>
            <li><strong>Idempotent Methods:</strong> <code>GET</code>, <code>PUT</code>, <code>DELETE</code>.</li>
            <li><strong>Non-Idempotent Methods:</strong> <code>POST</code>.</li>
        </ul>
        <p>To make <code>POST</code> idempotent, clients should generate a unique <code>Idempotency-Key</code> header. The server checks if it has seen this key before; if so, it returns the cached response instead of reprocessing.</p>"""
    },
    {
        "title": "API Gateways & BFF",
        "category": "Core Concepts",
        "tldr": "An API Gateway is a single entry point for all clients. A BFF (Backend-For-Frontend) is an API Gateway tailored for a specific UI client (e.g., Mobile vs. Web).",
        "explanation": """<p>In microservice architectures, clients shouldn't communicate directly with 50 different microservices.</p>
        <ul>
            <li><strong>API Gateway:</strong> Handles routing, rate limiting, authentication, SSL termination, and caching. Acts as a reverse proxy.</li>
            <li><strong>BFF Pattern:</strong> Instead of one giant API Gateway, you create multiple smaller gateways optimized for specific clients. A Mobile BFF might aggregate data differently than a Web BFF to save bandwidth.</li>
        </ul>""",
        "diagram": """flowchart TD
    Web[Web Client] --> BFF_Web[Web BFF]
    Mob[Mobile Client] --> BFF_Mob[Mobile BFF]
    
    BFF_Web --> Auth[Auth Service]
    BFF_Web --> User[User Service]
    
    BFF_Mob --> Auth
    BFF_Mob --> Order[Order Service]
    
    classDef bff fill:#3b82f6,stroke:#1e40af,color:#fff
    classDef svc fill:#1e2535,stroke:#6366f1,color:#fff
    
    class BFF_Web,BFF_Mob bff
    class Auth,User,Order svc"""
    },
    {
        "title": "WebSockets vs Long Polling",
        "category": "Core Concepts",
        "tldr": "WebSockets provide a persistent, full-duplex connection. Long Polling holds an HTTP request open until data is available.",
        "explanation": """<p>For real-time applications (chat, stock tickers):</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Technique</th><th>Description</th><th>Best For</th></tr>
            </thead>
            <tbody>
                <tr><td>Polling</td><td>Client repeatedly requests data every X seconds. High overhead.</td><td>Legacy systems.</td></tr>
                <tr><td>Long Polling</td><td>Server holds request open until data arrives. Lower overhead but requires reconnects.</td><td>Environments where WebSockets are blocked.</td></tr>
                <tr><td>WebSockets</td><td>Persistent TCP connection. Bidirectional communication with minimal overhead.</td><td>Chat apps, live games.</td></tr>
                <tr><td>SSE (Server-Sent Events)</td><td>Unidirectional (Server to Client) over HTTP.</td><td>Real-time notifications, logs.</td></tr>
            </tbody>
        </table>"""
    },
    {
        "title": "Service Discovery",
        "category": "Core Concepts",
        "tldr": "A mechanism for microservices to locate each other dynamically as their IP addresses and ports change in dynamic environments like Kubernetes.",
        "explanation": """<p>In modern cloud environments, instances scale up and down. Hardcoding IP addresses is impossible.</p>
        <ul>
            <li><strong>Service Registry:</strong> A database containing the network locations of service instances (e.g., Consul, Eureka, ZooKeeper).</li>
            <li><strong>Client-Side Discovery:</strong> The client queries the registry and load balances the requests itself.</li>
            <li><strong>Server-Side Discovery:</strong> The client routes through a load balancer, which queries the registry.</li>
        </ul>
        <p>In Kubernetes, CoreDNS and ClusterIP services handle this natively.</p>"""
    },
    {
        "title": "Rate Limiting Strategies",
        "category": "Core Concepts",
        "tldr": "Techniques to control the rate of traffic sent or received by a network to prevent DoS attacks and resource exhaustion.",
        "explanation": """<p>Common Rate Limiting Algorithms:</p>
        <ul>
            <li><strong>Token Bucket:</strong> Tokens are added at a constant rate. Each request costs a token. Allows bursts of traffic.</li>
            <li><strong>Leaky Bucket:</strong> Requests enter a queue (bucket) and are processed at a constant rate. Smooths out traffic.</li>
            <li><strong>Fixed Window Counter:</strong> Tracks requests per minute (e.g., 00:00 to 00:01). Suffers from the "boundary effect" (spikes at the edge of the window).</li>
            <li><strong>Sliding Window Log:</strong> Keeps a timestamp of every request. Extremely accurate but high memory cost.</li>
        </ul>""",
        "diagram": """flowchart LR
    Req[Incoming Request] --> Check{Has Tokens?}
    Check -->|Yes| Bucket[Token Bucket]
    Bucket -->|Consume Token| Process[Process Request]
    Check -->|No| Reject[Return 429 Too Many Requests]
    
    Refill((Refill at Constant Rate)) -.-> Bucket
    
    classDef process fill:#10b981,stroke:#047857,color:#fff
    classDef reject fill:#ef4444,stroke:#b91c1c,color:#fff
    
    class Process process
    class Reject reject"""
    }
]
