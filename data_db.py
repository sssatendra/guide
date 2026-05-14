questions = [
    {
        "title": "Relational vs NoSQL",
        "category": "Databases & Data Handling",
        "tldr": "Relational (SQL) databases use rigid schemas and tables, ensuring strong consistency. NoSQL databases use flexible data models (documents, key-value, graphs) optimized for specific access patterns and horizontal scale.",
        "explanation": """<p>Choosing a database is the most critical architectural decision.</p>
        <table class="comparison-table">
            <thead>
                <tr><th>Feature</th><th>Relational (PostgreSQL, MySQL)</th><th>NoSQL (MongoDB, DynamoDB)</th></tr>
            </thead>
            <tbody>
                <tr><td>Structure</td><td>Tables with rows and columns (rigid schema)</td><td>JSON Documents, Key-Value, Wide-Column, Graph</td></tr>
                <tr><td>Scaling</td><td>Vertical (Scale Up - bigger CPU/RAM)</td><td>Horizontal (Scale Out - more commodity servers)</td></tr>
                <tr><td>Transactions</td><td>Strong ACID compliance</td><td>Often BASE, limited to single-document transactions</td></tr>
                <tr><td>Use Case</td><td>Financial data, complex joins, strict integrity</td><td>Rapid prototyping, massive read/write scale, unstructured data</td></tr>
            </tbody>
        </table>""",
        "diagram": """flowchart LR
    subgraph SQL [Relational]
        Tables[(Users Table)] --- ForeignKeys[Foreign Keys] --- Orders[(Orders Table)]
    end
    
    subgraph NoSQL [Document NoSQL]
        JSON[{ "id": 1, "name": "Alice", "orders": [...] }]
    end
    
    classDef sql fill:#3b82f6,stroke:#1e40af,color:#fff
    classDef nosql fill:#10b981,stroke:#047857,color:#fff
    
    class SQL sql
    class NoSQL nosql"""
    },
    {
        "title": "ACID vs BASE Properties",
        "category": "Databases & Data Handling",
        "tldr": "ACID guarantees exact data validity (relational). BASE provides high availability and accepts eventual consistency (NoSQL).",
        "explanation": """<p>These paradigms describe how a database handles state changes.</p>
        <ul>
            <li><strong>ACID:</strong>
                <ul>
                    <li><strong>Atomicity:</strong> All or nothing (entire transaction succeeds or fails).</li>
                    <li><strong>Consistency:</strong> Data moves from one valid state to another.</li>
                    <li><strong>Isolation:</strong> Concurrent transactions don't interfere with each other.</li>
                    <li><strong>Durability:</strong> Once committed, data remains even in a crash.</li>
                </ul>
            </li>
            <li><strong>BASE:</strong>
                <ul>
                    <li><strong>Basically Available:</strong> The system guarantees availability.</li>
                    <li><strong>Soft State:</strong> State may change over time without input due to eventual consistency.</li>
                    <li><strong>Eventual Consistency:</strong> The system will eventually become consistent once it stops receiving input.</li>
                </ul>
            </li>
        </ul>"""
    },
    {
        "title": "Database Normalization",
        "category": "Databases & Data Handling",
        "tldr": "The process of organizing data in a relational database to minimize redundancy and dependency.",
        "explanation": """<p>Normalization structures tables to reduce data anomalies (Insert, Update, Delete anomalies).</p>
        <ul>
            <li><strong>1NF (First Normal Form):</strong> Each column must contain atomic (indivisible) values. No repeating groups.</li>
            <li><strong>2NF (Second Normal Form):</strong> Must be in 1NF. All non-key attributes must be fully functionally dependent on the primary key. (Removes partial dependencies).</li>
            <li><strong>3NF (Third Normal Form):</strong> Must be in 2NF. All non-key attributes must be independent of other non-key attributes. (Removes transitive dependencies).</li>
        </ul>
        <p><em>Note: Denormalization is often applied in read-heavy applications or data warehouses to improve read performance by avoiding expensive Joins.</em></p>"""
    },
    {
        "title": "Indexes and B-Trees",
        "category": "Databases & Data Handling",
        "tldr": "An index is a data structure that improves the speed of data retrieval at the cost of additional storage and slower writes. Most relational DBs use B-Trees for indexing.",
        "explanation": """<p>If you query a table without an index, the database must perform a <strong>Full Table Scan (O(N))</strong>. An index works like a book's index at the back.</p>
        <ul>
            <li><strong>B-Tree (Balanced Tree):</strong> The default index type. It keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time <strong>O(log N)</strong>.</li>
            <li><strong>Hash Index:</strong> Excellent for exact match lookups (O(1)) but cannot be used for range queries (e.g., <code>age > 20</code>).</li>
        </ul>
        <p><strong>Trade-off:</strong> Every time you INSERT, UPDATE, or DELETE a row, the database must also update the index, making writes slower.</p>"""
    },
    {
        "title": "Sharding vs Partitioning",
        "category": "Databases & Data Handling",
        "tldr": "Partitioning divides a large table into smaller, manageable pieces. Sharding is a form of horizontal partitioning where pieces are distributed across multiple servers.",
        "explanation": """<p>When a database gets too large for a single disk, we must split it.</p>
        <ul>
            <li><strong>Vertical Partitioning:</strong> Splitting columns of a table into separate tables. Used for isolating infrequently accessed columns (e.g., large text blobs).</li>
            <li><strong>Horizontal Partitioning:</strong> Splitting rows of a table into separate tables on the same server based on a partition key (e.g., partitioned by year).</li>
            <li><strong>Sharding:</strong> Distributing horizontally partitioned data across multiple independent database servers (nodes). Crucial for massive scale, but introduces complexity (distributed joins are very slow).</li>
        </ul>""",
        "diagram": """flowchart TD
    DB[(Massive DB)] -->|Sharding| S1[(Shard 1: A-H)]
    DB -->|Sharding| S2[(Shard 2: I-P)]
    DB -->|Sharding| S3[(Shard 3: Q-Z)]
    
    classDef db fill:#1e2535,stroke:#6366f1,stroke-width:2px,color:#fff
    class DB,S1,S2,S3 db"""
    },
    {
        "title": "Database Replication",
        "category": "Databases & Data Handling",
        "tldr": "Copying data across multiple servers to improve read performance, ensure high availability, and provide disaster recovery.",
        "explanation": """<p>Replication ensures that if one server dies, data is not lost.</p>
        <ul>
            <li><strong>Master-Slave (Leader-Follower):</strong> One node handles all Writes. Changes are replicated asynchronously to Slave nodes. Slaves handle Read requests. Great for read-heavy apps. <em>Risk: Data lag on slaves.</em></li>
            <li><strong>Multi-Master (Leader-Leader):</strong> Multiple nodes accept Writes. Highly available for writes, but conflict resolution (when two nodes write to the same record) is highly complex.</li>
        </ul>"""
    },
    {
        "title": "CAP Theorem",
        "category": "Databases & Data Handling",
        "tldr": "A distributed system can only provide two of three guarantees simultaneously: Consistency, Availability, and Partition Tolerance.",
        "explanation": """<p>In distributed systems, network partitions (P) are inevitable (networks will fail). Therefore, you must choose between C and A.</p>
        <ul>
            <li><strong>CP (Consistency & Partition Tolerance):</strong> If a network fails, the system blocks requests (reducing availability) until it can guarantee consistency. <em>(e.g., MongoDB, HBase, Redis Cluster)</em></li>
            <li><strong>AP (Availability & Partition Tolerance):</strong> The system returns the most recent data available, even if it's stale (sacrificing consistency). <em>(e.g., Cassandra, DynamoDB, CouchDB)</em></li>
            <li><strong>CA:</strong> A single-node relational database. Cannot survive network partitions.</li>
        </ul>"""
    },
    {
        "title": "PACELC Theorem",
        "category": "Databases & Data Handling",
        "tldr": "An extension of CAP. If there is a Partition (P), how does the system trade off Availability (A) and Consistency (C)? Else (E), when the system is running normally, how does it trade off Latency (L) and Consistency (C)?",
        "explanation": """<p>CAP only applies when there's a failure. PACELC explains what happens during normal operations.</p>
        <p><strong>Example: DynamoDB (PA/EL)</strong></p>
        <ul>
            <li>Under a Partition (P), it chooses Availability (A).</li>
            <li>Else (E), under normal operations, it chooses Latency (L) over strong Consistency (C) (yielding eventual consistency for faster reads).</li>
        </ul>"""
    },
    {
        "title": "Optimistic vs Pessimistic Locking",
        "category": "Databases & Data Handling",
        "tldr": "Strategies for handling concurrent updates. Optimistic checks for conflicts before committing. Pessimistic locks the record the moment it's read.",
        "explanation": """<p>When two users try to buy the last concert ticket simultaneously, how do you prevent double-selling?</p>
        <ul>
            <li><strong>Optimistic Locking:</strong> Assumes conflicts are rare. Adds a <code>version</code> column. Both users read version 1. User A updates and increments to version 2. User B tries to update version 1, but the DB sees it's now version 2 and rejects User B.</li>
            <li><strong>Pessimistic Locking:</strong> Assumes conflicts are common. Uses <code>SELECT ... FOR UPDATE</code>. User A reads and locks the row. User B's read is blocked until User A finishes their transaction. Slower, but prevents conflicts entirely.</li>
        </ul>"""
    },
    {
        "title": "Change Data Capture (CDC)",
        "category": "Databases & Data Handling",
        "tldr": "A design pattern used to track and propagate data changes (INSERT, UPDATE, DELETE) in a database to downstream systems in real-time.",
        "explanation": """<p>Instead of doing expensive batch queries (e.g., "give me all users updated in the last 10 minutes"), CDC listens to the database's internal transaction log (like PostgreSQL's WAL or MySQL's Binlog).</p>
        <p><strong>Use Cases:</strong></p>
        <ul>
            <li>Keeping a search index (Elasticsearch) in sync with a primary database.</li>
            <li>Updating an in-memory cache (Redis) automatically when DB data changes.</li>
            <li>Streaming data to an analytical data warehouse.</li>
        </ul>
        <p><em>Debezium</em> is the industry standard open-source tool for CDC.</p>"""
    }
]
