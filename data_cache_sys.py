questions = [
    {
        "title": "Cache Invalidation & Eviction",
        "category": "Caching & Performance",
        "tldr": "Eviction decides which data leaves when memory is full (e.g., LRU). Invalidation is actively removing data because the underlying database record changed.",
        "explanation": """<p>Phil Karlton famously said: <em>"There are only two hard things in Computer Science: cache invalidation and naming things."</em></p>
        <p><strong>Eviction Policies (When full):</strong></p>
        <ul>
            <li><strong>LRU (Least Recently Used):</strong> Discards items accessed furthest in the past. The most common algorithm.</li>
            <li><strong>LFU (Least Frequently Used):</strong> Discards items accessed least often overall.</li>
            <li><strong>FIFO (First In, First Out):</strong> Evicts the oldest items in the cache regardless of usage.</li>
        </ul>
        <p><strong>Invalidation Strategies (Keeping data fresh):</strong></p>
        <ul>
            <li><strong>Write-Through:</strong> Data is written into the cache and the database simultaneously. High write latency, but ensures strong consistency.</li>
            <li><strong>Write-Around:</strong> Data goes directly to the DB, bypassing the cache. Cache is updated only on a cache miss.</li>
            <li><strong>Write-Back:</strong> Data is written to the cache immediately and confirmed to the client. The cache asynchronously writes to the DB. High risk of data loss on crash.</li>
        </ul>"""
    },
    {
        "title": "Redis vs Memcached",
        "category": "Caching & Performance",
        "tldr": "Both are fast, in-memory data stores. Memcached is simple and strictly for caching strings. Redis is an advanced data structure server with persistence capabilities.",
        "explanation": """<p>When choosing an in-memory cache:</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Feature</th><th>Redis</th><th>Memcached</th></tr>
            </thead>
            <tbody>
                <tr><td>Data Structures</td><td>Strings, Hashes, Lists, Sets, Sorted Sets, Bitmaps</td><td>Only Strings (Key-Value)</td></tr>
                <tr><td>Persistence</td><td>Yes (RDB Snapshots and AOF logs)</td><td>No (Volatile only)</td></tr>
                <tr><td>Pub/Sub Support</td><td>Yes</td><td>No</td></tr>
                <tr><td>Threading</td><td>Single-threaded (avoids locks)</td><td>Multi-threaded (scales better vertically)</td></tr>
            </tbody>
        </table>
        <p><strong>Verdict:</strong> Use Memcached if you literally just need a dumb, lightning-fast HTML/JSON string cache. Use Redis for virtually everything else (queues, leaderboards, sessions, geospacial data).</p>"""
    },
    {
        "title": "CDN (Content Delivery Network)",
        "category": "Caching & Performance",
        "tldr": "A geographically distributed network of proxy servers that cache static assets closer to the end user to reduce latency.",
        "explanation": """<p>If your server is in New York, a user in Tokyo will experience 200ms+ latency just to download your logo. CDNs solve this.</p>
        <ul>
            <li><strong>Edge Servers:</strong> The servers located near the users (e.g., in Tokyo).</li>
            <li><strong>Origin Server:</strong> Your actual backend server in New York.</li>
        </ul>
        <p>When a user requests an image, the Edge Server intercepts it. If cached (Cache Hit), it serves it immediately (10ms). If not (Cache Miss), it pulls from the Origin, caches it, and serves it.</p>
        <p><em>Modern CDNs (Cloudflare, Fastly) can also cache dynamic API responses and execute edge compute functions (WebAssembly/V8 Isolates).</em></p>""",
        "diagram": """flowchart LR
    User[User in Tokyo] -->|Requests Image| Edge[Edge Server (Tokyo)]
    Edge -->|Cache Miss| Origin[Origin Server (New York)]
    Origin -->|Returns Image| Edge
    Edge -->|Caches & Returns| User
    
    User2[User 2 in Tokyo] -->|Requests Image| Edge
    Edge -->|Cache Hit (Fast!)| User2
    
    classDef edge fill:#f59e0b,stroke:#b45309,color:#fff
    classDef origin fill:#1e2535,stroke:#6366f1,color:#fff
    
    class Edge edge
    class Origin origin"""
    },
    {
        "title": "Message Queues vs Event Streams",
        "category": "Systems & Scaling",
        "tldr": "Queues (RabbitMQ) are for executing tasks where messages are consumed and deleted. Streams (Kafka) are an immutable log of events that multiple consumers can read and replay.",
        "explanation": """<p>Both are forms of asynchronous communication, but their semantics are drastically different.</p>
        <ul>
            <li><strong>Message Queues (Command pattern):</strong> "Service A tells Service B to Send an Email." Once Service B reads the message, it is acknowledged and removed from the queue. Great for task distribution (worker pools).</li>
            <li><strong>Event Streams (Event-driven pattern):</strong> "Service A announces a User was Created." The event is appended to a log. It is NOT deleted when read. Service B (Email), Service C (Analytics), and Service D (Billing) can all independently read the same event from the log at different speeds.</li>
        </ul>"""
    },
    {
        "title": "Kafka vs RabbitMQ",
        "category": "Systems & Scaling",
        "tldr": "RabbitMQ is a traditional message broker focusing on complex routing. Kafka is a distributed event streaming platform built for massive throughput and replayability.",
        "explanation": """<p>Choosing the right broker prevents architectural headaches later.</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Feature</th><th>RabbitMQ (Queue)</th><th>Apache Kafka (Stream)</th></tr>
            </thead>
            <tbody>
                <tr><td>Architecture</td><td>Smart Broker, Dumb Consumers</td><td>Dumb Broker, Smart Consumers</td></tr>
                <tr><td>Data Retention</td><td>Deleted after acknowledgment</td><td>Retained based on time/size (Replayable)</td></tr>
                <tr><td>Throughput</td><td>10K - 50K msgs/sec</td><td>100K - 1M+ msgs/sec</td></tr>
                <tr><td>Routing</td><td>Complex (Direct, Topic, Fanout exchanges)</td><td>Simple (Topics/Partitions)</td></tr>
            </tbody>
        </table>"""
    },
    {
        "title": "Forward vs Reverse Proxy",
        "category": "Systems & Scaling",
        "tldr": "A Forward Proxy protects the client. A Reverse Proxy protects the server.",
        "explanation": """<p>Proxies act as intermediaries in network traffic.</p>
        <ul>
            <li><strong>Forward Proxy:</strong> Sits in front of client machines. When an employee tries to visit a website, the request goes through the corporate forward proxy. The internet only sees the proxy's IP. Used for content filtering, anonymity (VPNs), and corporate security.</li>
            <li><strong>Reverse Proxy:</strong> Sits in front of backend servers. When a user tries to visit your website, they hit the reverse proxy (like Nginx). The proxy then forwards the request to the appropriate backend server. Used for load balancing, SSL termination, caching, and hiding internal architecture.</li>
        </ul>""",
        "diagram": """flowchart LR
    subgraph Forward Proxy Setup
        Client1[Client] --> FProxy[Forward Proxy]
        FProxy --> Int1((Internet))
    end
    
    subgraph Reverse Proxy Setup
        Int2((Internet)) --> RProxy[Reverse Proxy (Nginx)]
        RProxy --> Srv1[Server A]
        RProxy --> Srv2[Server B]
    end
    
    classDef proxy fill:#3b82f6,stroke:#1e40af,color:#fff
    class FProxy,RProxy proxy"""
    },
    {
        "title": "Load Balancing Algorithms",
        "category": "Systems & Scaling",
        "tldr": "Techniques used by a Load Balancer to distribute incoming traffic efficiently across multiple backend servers.",
        "explanation": """<p>A reverse proxy is useless if it sends all traffic to one node.</p>
        <ul>
            <li><strong>Round Robin:</strong> Distributes requests sequentially (Server A, then B, then C, repeat). Bad if servers have different capacities.</li>
            <li><strong>Least Connections:</strong> Sends the request to the server with the fewest active connections. Great for long-lived requests (like WebSockets).</li>
            <li><strong>IP Hash:</strong> Uses a hash of the client's IP address to determine the server. Guarantees a specific client always hits the same server (Sticky Sessions). Useful for legacy stateful apps.</li>
            <li><strong>Weighted Round Robin:</strong> Assigns a weight to each server. A server with weight 3 gets 3 times more requests than a server with weight 1.</li>
        </ul>"""
    },
    {
        "title": "Horizontal vs Vertical Scaling",
        "category": "Systems & Scaling",
        "tldr": "Vertical scaling (Scale Up) means adding more power to one machine. Horizontal scaling (Scale Out) means adding more machines to the pool.",
        "explanation": """<p>How do you handle increased traffic?</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Aspect</th><th>Vertical Scaling (Scale Up)</th><th>Horizontal Scaling (Scale Out)</th></tr>
            </thead>
            <tbody>
                <tr><td>How?</td><td>Upgrade CPU, RAM, or Disk</td><td>Add more servers behind a load balancer</td></tr>
                <tr><td>Limits</td><td>Hardware constraints (can't have infinite RAM)</td><td>Theoretically infinite</td></tr>
                <tr><td>Downtime</td><td>Requires restarting the server</td><td>Zero downtime (add nodes dynamically)</td></tr>
                <tr><td>Complexity</td><td>Very low (code doesn't change)</td><td>High (requires stateless architecture, distributed databases)</td></tr>
            </tbody>
        </table>"""
    },
    {
        "title": "Microservices vs Monolith",
        "category": "Systems & Scaling",
        "tldr": "Monoliths package all features into one deployable unit. Microservices split features into independent, network-communicating services.",
        "explanation": """<p>The architectural pendulum.</p>
        <ul>
            <li><strong>Monolith:</strong> Simple to develop, test, and deploy initially. However, as the team grows, merge conflicts explode, the codebase becomes spaghetti, and scaling requires copying the entire app even if only the "Billing" feature is under load.</li>
            <li><strong>Microservices:</strong> Services are split by business domain. Independent deployments, independent scaling, and you can use different languages. <em>The massive downside:</em> Operational complexity, network latency, distributed debugging, and complex data joins.</li>
        </ul>
        <p><strong>Rule of thumb:</strong> Start with a modular monolith. Extract microservices only when organizational scaling or severe performance bottlenecks demand it.</p>"""
    },
    {
        "title": "Serverless Architecture",
        "category": "Systems & Scaling",
        "tldr": "An execution model where the cloud provider dynamically manages the allocation and provisioning of servers (e.g., AWS Lambda). You only pay for exact compute time used.",
        "explanation": """<p>"Serverless" does not mean no servers; it means you don't manage them.</p>
        <ul>
            <li><strong>Pros:</strong> Zero maintenance, auto-scaling to thousands of concurrent requests instantly, and extremely cheap for low-traffic applications (pay per millisecond).</li>
            <li><strong>Cons:</strong> "Cold Starts" (the delay when a function is invoked after being idle), vendor lock-in, and terrible pricing for highly predictable, constant, heavy workloads (a dedicated EC2 instance is cheaper for 24/7 heavy CPU usage).</li>
        </ul>"""
    }
]
