questions = [
    {
        "title": "Circuit Breaker Pattern",
        "category": "Reliability & Real-World Problems",
        "tldr": "A design pattern that prevents an application from repeatedly trying to execute an operation that's likely to fail, saving system resources and preventing cascading failures.",
        "explanation": """<p>When Service A calls Service B, and Service B is down, Service A will hang until it times out. If 1,000 requests hit Service A, it will exhaust its threads waiting for B, causing Service A to crash too (Cascading Failure).</p>
        <p>A Circuit Breaker wraps the network call and monitors for failures:</p>
        <ul>
            <li><strong>Closed:</strong> Everything is fine. Requests flow normally.</li>
            <li><strong>Open:</strong> The failure threshold is reached (e.g., 5 timeouts). The breaker "trips". All subsequent requests immediately fail (Fail Fast) without even trying to hit Service B.</li>
            <li><strong>Half-Open:</strong> After a timeout, the breaker lets a single test request through. If it succeeds, the breaker resets to Closed. If it fails, it goes back to Open.</li>
        </ul>""",
        "diagram": """flowchart TD
    Req[Incoming Request] --> CB{Circuit Breaker State}
    CB -->|Closed| Call[Call External Service]
    CB -->|Open| Fail[Immediate Fallback / Error]
    CB -->|Half-Open| Test[Send 1 Test Request]
    
    Test -->|Success| Reset[Reset to Closed]
    Test -->|Fail| Open[Back to Open]
    
    classDef state fill:#1e2535,stroke:#6366f1,color:#fff
    class CB state"""
    },
    {
        "title": "Rate Limiting vs Throttling",
        "category": "Reliability & Real-World Problems",
        "tldr": "Rate limiting restricts the total number of requests a user can make. Throttling slows down the processing of requests rather than outright rejecting them.",
        "explanation": """<p>Both control traffic, but their UX impact differs.</p>
        <ul>
            <li><strong>Rate Limiting:</strong> "You can only make 100 API calls per minute." If you make 101, you get an HTTP 429 (Too Many Requests) error. It's a hard stop.</li>
            <li><strong>Throttling:</strong> "We will process your data, but we're going to do it slowly to save bandwidth." Think of an ISP slowing down your internet speed after you hit a data cap. The request succeeds, but at a degraded performance level.</li>
        </ul>"""
    },
    {
        "title": "Saga Pattern (Distributed Transactions)",
        "category": "Reliability & Real-World Problems",
        "tldr": "A sequence of local transactions where each transaction updates data within a single service. If a step fails, compensating transactions are triggered to undo preceding steps.",
        "explanation": """<p>In a monolith, you use ACID transactions. In microservices, you cannot wrap a database commit around three different databases spanning three services.</p>
        <p><strong>Example (E-Commerce):</strong></p>
        <ol>
            <li>Order Service creates Order (Pending).</li>
            <li>Inventory Service reserves items.</li>
            <li>Payment Service charges credit card. <em>(Fails due to insufficient funds)</em></li>
        </ol>
        <p>Because Payment failed, a <strong>Compensating Transaction</strong> must be sent backward: Inventory Service must un-reserve the items, and Order Service must mark the Order as Failed. This is eventually consistent.</p>"""
    },
    {
        "title": "Race Conditions",
        "category": "Reliability & Real-World Problems",
        "tldr": "A flaw that occurs when the timing of events affects the correctness of an operation, usually happening when multiple threads access and mutate shared data concurrently.",
        "explanation": """<p><strong>The classic ATM problem:</strong></p>
        <ul>
            <li>Account Balance is $100.</li>
            <li>Thread A reads $100. Thread B reads $100.</li>
            <li>Thread A subtracts $50 and writes $50.</li>
            <li>Thread B subtracts $40 and writes $60 (overwriting Thread A's math!).</li>
            <li>Final balance is $60 instead of $10.</li>
        </ul>
        <p><strong>Solutions:</strong> Use Database Locks (Pessimistic/Optimistic), Atomic Operations (e.g., Redis `INCR`), or synchronize thread access in code (Mutexes).</p>"""
    },
    {
        "title": "Deadlocks",
        "category": "Reliability & Real-World Problems",
        "tldr": "A situation where two or more processes are unable to proceed because each is waiting for the other to release a resource.",
        "explanation": """<p>Deadlocks freeze systems completely.</p>
        <p><strong>Scenario:</strong></p>
        <ul>
            <li>Process 1 locks Table A, and needs Table B to finish.</li>
            <li>Process 2 locks Table B, and needs Table A to finish.</li>
            <li>They wait for each other infinitely.</li>
        </ul>
        <p><strong>Prevention:</strong> Always acquire locks in the same hierarchical order across the entire application (e.g., always lock A before B). Use lock timeouts so transactions eventually fail rather than hanging forever.</p>"""
    },
    {
        "title": "Polling vs Webhooks",
        "category": "Reliability & Real-World Problems",
        "tldr": "Polling is the client constantly asking the server if an event happened. A Webhook is the server telling the client exactly when the event happens.",
        "explanation": """<p>When waiting for a third-party event (e.g., waiting for Stripe to confirm a payment):</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Feature</th><th>Polling</th><th>Webhooks</th></tr>
            </thead>
            <tbody>
                <tr><td>Mechanism</td><td>Client: "Is it done yet?" (Every 5 secs)</td><td>Server: "Hey Client, it's done. Here's the data."</td></tr>
                <tr><td>Overhead</td><td>Very High (99% of requests return "No")</td><td>Very Low (1 request upon completion)</td></tr>
                <tr><td>Latency</td><td>Delayed up to the polling interval</td><td>Real-time</td></tr>
                <tr><td>Setup</td><td>Simple</td><td>Requires the client to expose a public endpoint</td></tr>
            </tbody>
        </table>"""
    },
    {
        "title": "Single Point of Failure (SPOF)",
        "category": "Reliability & Real-World Problems",
        "tldr": "A part of a system that, if it fails, will stop the entire system from working.",
        "explanation": """<p>System design interviews heavily scrutinize SPOFs.</p>
        <p><strong>Common SPOFs:</strong></p>
        <ul>
            <li>A single un-replicated relational database.</li>
            <li>A single Load Balancer routing all traffic.</li>
            <li>A single availability zone (Data Center).</li>
        </ul>
        <p><strong>Mitigation:</strong> Redundancy. Deploy multiple load balancers, use database replication (Master-Slave), and deploy across Multi-AZ (Availability Zones).</p>"""
    },
    {
        "title": "Disaster Recovery: RTO vs RPO",
        "category": "Reliability & Real-World Problems",
        "tldr": "Metrics that define business continuity. RTO is how fast you must recover. RPO is how much data you can afford to lose.",
        "explanation": """<p>When the database server literally catches fire:</p>
        <ul>
            <li><strong>RTO (Recovery Time Objective):</strong> The maximum acceptable downtime. If RTO is 1 hour, your system must be back online in 1 hour. Requires automated failover scripts.</li>
            <li><strong>RPO (Recovery Point Objective):</strong> The maximum acceptable data loss, measured in time. If RPO is 15 minutes, you must back up data every 15 minutes. If a crash happens, you lose at most 15 minutes of user data.</li>
        </ul>
        <p><em>Lowering RTO and RPO to near-zero requires active-active multi-region deployments, which is astronomically expensive.</em></p>"""
    },
    {
        "title": "Observability (Logs, Metrics, Traces)",
        "category": "Reliability & Real-World Problems",
        "tldr": "The Three Pillars of Observability allow engineers to understand the internal state of a system from the outside.",
        "explanation": """<p>Monitoring tells you a system is broken. Observability tells you <em>why</em>.</p>
        <ul>
            <li><strong>Logs:</strong> Discrete records of events (e.g., "User 123 failed login at 10:04 AM"). Tools: ELK Stack, Splunk, Datadog.</li>
            <li><strong>Metrics:</strong> Aggregated numeric data over time (e.g., "CPU is at 95%", "500 errors spiked"). Highly efficient to store. Tools: Prometheus, Grafana.</li>
            <li><strong>Distributed Traces:</strong> Tracks the lifecycle of a single request as it jumps across 10 different microservices. Identifies exactly which service is causing the latency. Tools: Jaeger, OpenTelemetry.</li>
        </ul>""",
        "diagram": """flowchart LR
    Req[Request] --> S1[Service 1]
    S1 -->|Span A: 50ms| S2[Service 2]
    S2 -->|Span B: 200ms| DB[(Database)]
    S1 -->|Span C: 10ms| Cache[(Redis)]
    
    classDef trace fill:#1e2535,stroke:#a855f7,stroke-width:2px,color:#fff
    class S1,S2,DB,Cache trace"""
    },
    {
        "title": "Blue-Green vs Canary Deployments",
        "category": "Reliability & Real-World Problems",
        "tldr": "Deployment strategies that eliminate downtime and reduce the risk of deploying broken code to production.",
        "explanation": """<p>Replacing code on a live server causes dropped requests. Advanced routing solves this.</p>
        <ul>
            <li><strong>Blue-Green Deployment:</strong> You have two identical production environments. Blue is currently live. You deploy new code to Green. Once tested, you flip the router to point 100% of traffic to Green. If something breaks, flip back to Blue instantly.</li>
            <li><strong>Canary Release:</strong> You route a tiny subset of traffic (e.g., 5%) to the new version (the Canary). If error rates are stable, you slowly ramp up traffic (10%, 25%, 100%). Identifies bugs without affecting the entire user base.</li>
        </ul>"""
    }
]
