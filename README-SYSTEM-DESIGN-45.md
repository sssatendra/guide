# 🏗️ System Design - 45 Questions & Solutions

[![GitHub Pages](https://img.shields.io/badge/Hosted-GitHub%20Pages-blue?style=flat-square)](https://sssatendra.github.io/system-design-45)
[![Open Source](https://img.shields.io/badge/Open%20Source-MIT-green?style=flat-square)](LICENSE)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-May%202024-orange?style=flat-square)](.)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)](#contributing)

> **Master System Design Interviews** — Comprehensive guide covering 45 real-world system design questions with detailed solutions, architecture patterns, and best practices for backend, frontend, and full-stack engineers.

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Design Topics Covered](#system-design-topics-covered)
- [How to Use](#how-to-use)
- [Getting Started](#getting-started)
- [Key Topics](#key-topics)
- [Best For](#best-for)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This is a **comprehensive interactive learning platform** for **system design interviews** and **distributed systems architecture**. Whether you're preparing for FAANG interviews (Facebook, Amazon, Apple, Netflix, Google) or building scalable systems, this resource covers everything you need to know.

### What is System Design?

System Design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It's essential for:

- **Backend engineers** building scalable APIs
- **Frontend engineers** optimizing user experience
- **Full-stack developers** designing end-to-end solutions
- **DevOps engineers** setting up infrastructure
- **Machine learning engineers** deploying models at scale
- **Tech leads** making architectural decisions

---

## ✨ Features

### 🎨 Modern, Responsive Interface
- **Dark mode** for comfortable learning
- **Mobile-friendly** design works on all devices
- **Smooth animations** and intuitive navigation
- **Clean typography** optimized for readability

### 🔍 Interactive Learning
- **45 carefully curated questions** covering real-world scenarios
- **Real company use cases**: Facebook, Twitter, Uber, Netflix, Amazon
- **Color-coded difficulty levels**: Fundamental, Intermediate, Advanced
- **Instant search** across all topics
- **Filter by category** for focused learning

### 💡 In-Depth Solutions
- **Architecture diagrams** and system flows
- **Trade-offs analysis** for each approach
- **Performance metrics** and scalability considerations
- **Database choices** explained
- **Caching strategies** and optimization techniques
- **Load balancing** approaches
- **Data consistency** patterns (ACID, BASE, CAP theorem)

### 🚀 Real-World Focus
- **Production-ready solutions** from tech giants
- **Practical implementation details**
- **Common pitfalls** and how to avoid them
- **Industry best practices**

---

## 🛠️ System Design Topics Covered

### 🔴 Core Infrastructure & Data
1. **Distributed Metrics Logging & Aggregation**
2. **Distributed Stream Processing System (like Kafka)**
3. **Key-Value Store**
4. **Top K Most Shared Articles in Time Windows**
5. **API Rate Limiter**
6. **Collect Performance Metrics from Thousands of Servers**

### 🟡 Messaging & Queues
7. **Google Calendar**
8. **Distributed Queue (like RabbitMQ)**
9. **Google Analytics — User Analytics Dashboard**
10. **Sorting Large Data Sets**
11. **Top K Elements — App Store Rankings / Amazon Bestsellers**

### 🟢 Storage & File Systems
12. **Dropbox / Google Drive**
13. **Distributed Job Scheduler**
14. **Notification Service at Scale**
15. **Surge Pricing System (Uber)**
16. **Netflix — Limit Concurrent Screens**

### 🔵 Location & Real-Time Services
17. **ETA Service & Location Sharing (Uber)**
18. **Hotel Booking System**
19. **A/B Testing System (Optimizely)**
20. **Price Alert System (Amazon / Stock Prices)**

### 🟣 Advanced Patterns
21. **IoC / Dependency Injection Framework**
22. **Credit Card Processing System**
23. **Count Facebook Likes (High-Profile Users)**
24. **Control Plane for Distributed Database**
25. **User Login & Authentication System**

### 🌐 Real-Time & Analytics
26. **Weather Application**
27. **Collaborative Document System (Google Docs / Notion)**
28. **Facebook Marketplace**
29. **Monitor Health of a Cluster**
30. **Find a Rider/Driver (Uber Dispatch)**

### 📊 Advanced Systems
31. **Distributed Tracing System**
32. **Distribute 6M Free Burgers in 1 Hour**
33. **File Downloader Library**
34. **View Latest Stock Prices Worldwide**
35. **Photo Sharing Platform (Flickr / Google Photos)**

### 🔐 Enterprise Systems
36. **On-Call Escalation System**
37. **Wire Transfer API**
38. **Live Comments Feature (Facebook)**
39. **Count Users Viewing a Page**
40. **Facebook Likes with Live Updates**

### 🌍 Scale & Infrastructure
41. **Migrate Large Data to Google Cloud**
42. **Distributed Botnet (Defense-Focused)**
43. **Distributed File Transfer (BitTorrent)**
44. **Parts Compatibility for eCommerce**
45. **Ads Management & Display System**

---

## 📖 How to Use

### 1. **Open in Browser**
```bash
# Clone and open the HTML file
git clone https://github.com/sssatendra/system-design-45.git
cd system-design-45
open system-design-45.html
# Or simply open the hosted version
```

### 2. **Search for Topics**
- Use the **search bar** to find specific system design questions
- Search by keywords: "API", "Database", "Scaling", "Real-time", etc.

### 3. **Filter by Difficulty**
- **Fundamental**: Core concepts everyone should know
- **Intermediate**: Advanced patterns and optimizations
- **Advanced**: Complex enterprise systems

### 4. **Study Systematically**
- Start with Fundamental level topics
- Progress to Intermediate concepts
- Master Advanced systems
- Use navigation buttons to move between topics

### 5. **Practice Interview Format**
- Cover one topic per day
- Take notes on key points
- Draw architecture diagrams on paper
- Explain solutions out loud
- Time yourself for realistic interview prep

---

## 🚀 Getting Started

### For Interview Preparation

```
Week 1: Fundamentals
├── Data Storage (KV stores, Databases)
├── Caching (Redis, Memcached)
└── Message Queues (Kafka, RabbitMQ)

Week 2: Core Systems
├── Load Balancing
├── Auto-scaling
└── Monitoring & Logging

Week 3: Real Applications
├── Social Media (Facebook, Twitter)
├── Ride Sharing (Uber)
└── Video Streaming (Netflix)

Week 4: Advanced Topics
├── Distributed Transactions
├── Consensus Algorithms
└── Geo-replication
```

### Prerequisites
- Basic understanding of databases
- Familiarity with APIs and HTTP
- Knowledge of basic networking
- Understanding of Big O notation
- General programming experience

### Recommended Learning Path

1. **Start Here**: Load Balancing & Horizontal Scaling
2. **Then Learn**: Database Design & Sharding
3. **Master**: Caching & Consistency Patterns
4. **Challenge Yourself**: Complex distributed systems

---

## 💎 Key Topics & Concepts Explained

### Scalability Patterns
- **Vertical Scaling**: Adding more power to existing servers
- **Horizontal Scaling**: Adding more servers
- **Load Balancing**: Distributing traffic across servers
- **Database Sharding**: Splitting data across multiple databases
- **Caching Strategies**: Improving read performance

### High Availability
- **Replication**: Creating multiple copies of data
- **Failover**: Automatic switching to backup systems
- **Health Checks**: Detecting failed services
- **Disaster Recovery**: Recovering from major failures

### Data Consistency
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition tolerance
- **BASE Model**: Basically Available, Soft state, Eventual consistency
- **Conflict Resolution**: Handling concurrent updates

### Performance Optimization
- **CDN (Content Delivery Network)**: Caching content globally
- **Database Indexing**: Speeding up queries
- **Query Optimization**: Writing efficient SQL
- **Compression**: Reducing data transfer size

### Security & Compliance
- **Authentication & Authorization**: Verifying user identity
- **Encryption**: Protecting data in transit and at rest
- **Rate Limiting**: Preventing abuse and DoS attacks
- **Data Privacy**: GDPR, CCPA compliance

---

## 👥 Best For

| Role | Benefit |
|------|---------|
| **Backend Engineers** | Learn to design scalable APIs and microservices |
| **Full-Stack Developers** | Understand complete system architecture |
| **Frontend Engineers** | Learn backend considerations for better UX |
| **DevOps Engineers** | Master infrastructure and deployment patterns |
| **Technical Leads** | Make informed architectural decisions |
| **Data Engineers** | Design data pipelines and analytics systems |
| **Mobile Developers** | Understand backend constraints and optimization |
| **Tech Leads** | Interview preparation and technical assessment |
| **Interview Candidates** | Comprehensive prep for FAANG and top-tier companies |

---

## 💻 Tech Stack

This resource covers system design with the following technologies:

### Databases
- **SQL**: PostgreSQL, MySQL, Oracle
- **NoSQL**: MongoDB, Cassandra, DynamoDB
- **Search**: Elasticsearch, Solr
- **Cache**: Redis, Memcached

### Message Queues & Streaming
- **Kafka**: High-throughput messaging
- **RabbitMQ**: Reliable message delivery
- **Apache Pulsar**: Multi-tenancy support
- **AWS SQS**: Cloud-native queues

### Infrastructure
- **Load Balancers**: Nginx, HAProxy, AWS ELB
- **Containers**: Docker, Kubernetes
- **Orchestration**: Kubernetes, Docker Swarm
- **Monitoring**: Prometheus, Grafana, DataDog

### Design Patterns
- **Microservices Architecture**
- **Event-Driven Architecture**
- **CQRS Pattern**: Command Query Responsibility Segregation
- **Saga Pattern**: Distributed transactions
- **Circuit Breaker**: Fault tolerance

---

## 🎓 Learning Outcomes

After studying this guide, you'll understand:

✅ How to approach system design problems  
✅ Key architectural patterns and trade-offs  
✅ Database selection criteria and sharding strategies  
✅ Caching strategies and cache invalidation  
✅ Load balancing and auto-scaling techniques  
✅ Message queues and event-driven systems  
✅ Monitoring, logging, and alerting  
✅ Security and data privacy considerations  
✅ Cost optimization for large-scale systems  
✅ Real-world production systems from FAANG companies  

---

## 🔗 Related Resources

### Complementary Learning
- **System Design Interview** - Alex Xu (Book)
- **Designing Data-Intensive Applications** - Martin Kleppmann (Book)
- **High Performance MySQL** - Baron Schwartz (Book)
- **Site Reliability Engineering** - Google (Book)

### Tools & Simulators
- **LeetCode System Design**: Practice problems
- **Excalidraw**: Draw architecture diagrams
- **DrawIO**: Create flowcharts and diagrams
- **Miro**: Collaborative whiteboarding

### Communities
- **System Design Daily**: Discord community
- **Dev.to**: Articles and discussions
- **HackerNews**: Technology discussions
- **Reddit r/learnprogramming**: Q&A community

---

## 🛠️ Installation & Setup

### Option 1: Open Directly
```bash
# Simply open the HTML file in your browser
open system-design-45.html
```

### Option 2: Clone from GitHub
```bash
git clone https://github.com/sssatendra/system-design-45.git
cd system-design-45
# Open in browser
open system-design-45.html
```

### Option 3: Run Local Server
```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js
npx http-server

# Open http://localhost:8000/system-design-45.html
```

### Option 4: Use GitHub Pages
- Push to GitHub repository
- Enable GitHub Pages in settings
- Access at: `https://sssatendra.github.io/system-design-45/`

---

## 📊 Topics by Company

### Facebook / Meta
- Count Facebook Likes (High-Profile Users)
- Facebook Marketplace
- Live Comments Feature (Facebook)
- Facebook Likes with Live Updates
- Distributed Tracing System

### Amazon
- Top K Elements — Amazon Bestsellers
- Price Alert System
- eCommerce Systems
- Parts Compatibility

### Google
- Google Calendar
- Google Analytics Dashboard
- Google Drive (Dropbox comparison)
- Google Photos

### Netflix
- Netflix — Limit Concurrent Screens
- Video Streaming Infrastructure
- Recommendation Systems

### Uber
- Surge Pricing System
- ETA Service & Location Sharing
- Find a Rider/Driver (Dispatch)
- Real-time Tracking

### Twitter
- Tweet Timeline Distribution
- Notification Service at Scale
- Real-time Analytics

---

## 🤝 Contributing

We welcome contributions! Help make this resource better:

### How to Contribute

1. **Fork the repository**
```bash
git clone https://github.com/sssatendra/system-design-45.git
cd system-design-45
```

2. **Create a feature branch**
```bash
git checkout -b feature/improvement-name
```

3. **Make your changes**
   - Add new questions
   - Improve explanations
   - Fix typos
   - Add diagrams
   - Update code examples

4. **Commit and push**
```bash
git add .
git commit -m "Add: New system design topic"
git push origin feature/improvement-name
```

5. **Create a pull request**
   - Describe your changes
   - Explain why it's valuable
   - Reference related issues

### Areas for Contribution

- 📝 Adding more detailed explanations
- 🎨 Creating system architecture diagrams
- 🔍 Fixing typos and grammar
- 📊 Adding performance benchmarks
- 💡 Suggesting new topics
- 🐛 Reporting bugs and issues
- 🌍 Translating to other languages
- 📚 Adding recommended resources

---

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### You are free to:
- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute copies
- ✅ Use privately

### You must:
- ✅ Include license and copyright notice
- ✅ State changes made

---

## 🌟 Show Your Support

If this resource helped you, please:

- ⭐ **Star this repository** on GitHub
- 📢 **Share with your network**
- 💬 **Give feedback and suggestions**
- 🤝 **Contribute improvements**
- 📝 **Write a review or testimonial**

### Share on Social Media

```
"Just aced my system design interview with this amazing resource! 
45 questions covering real-world scenarios from Facebook, Google, Uber, Netflix. 
Perfect for interview prep! #SystemDesign #Backend #FAANG"

@sssatendra's System Design 45 Questions
https://github.com/sssatendra/system-design-45
```

---

## 📞 FAQ

**Q: Do I need prior experience to use this?**  
A: Basic programming knowledge is helpful, but we cover fundamentals.

**Q: How long does it take to study all topics?**  
A: Plan 6-8 weeks studying 1 topic per day, 30-60 minutes each.

**Q: Can I use this for real interviews?**  
A: Absolutely! This covers actual interview questions from top companies.

**Q: Is this resource frequently updated?**  
A: Yes! We add new topics and improve content regularly.

**Q: Can I contribute?**  
A: Definitely! We welcome all contributions. See [Contributing](#contributing) section.

---

## 🚀 Quick Links

- 🌐 [Live Demo](https://sssatendra.github.io/system-design-45)
- 📖 [Full Documentation](#)
- 🐛 [Report Issues](https://github.com/sssatendra/system-design-45/issues)
- 💬 [Discussions](https://github.com/sssatendra/system-design-45/discussions)
- 🔗 [Clone Repository](https://github.com/sssatendra/system-design-45)

---

## 📈 SEO Keywords

*This resource is optimized for the following search terms:*

- System Design Interview Questions
- System Design Tutorial
- Distributed Systems Design
- Backend System Architecture
- Scalable Systems Design
- FAANG Interview Preparation
- System Design Patterns
- Microservices Architecture
- Database Sharding
- Load Balancing Algorithms
- Caching Strategies
- Kafka Message Queue
- Redis Caching
- NoSQL vs SQL
- CAP Theorem
- API Design
- Rate Limiting
- Service Discovery
- Monitoring and Logging
- Data Consistency Patterns

---

## 👨‍💻 Author

Created with ❤️ for developers who want to master system design.

**Your Name**  
GitHub: [@sssatendra](https://github.com/sssatendra)  
Twitter: [@yourhandle](https://twitter.com/yourhandle)  

---

## 📅 Last Updated

May 2024 | Version 2.0

---

<div align="center">

**⭐ If this helped you, please star the repository! ⭐**

[⬆ Back to top](#-system-design---45-questions--solutions)

</div>
