from pathlib import Path

files = {
    "b:/workshop/fcj-workshop-template/content/3-BlogsPosted/3.1-Blog1/_index.md": """---
title: \"Announcing Bedrock AgentCore Web Search for Agent-Oriented Retrieval\"
date: 2024-06-25T11:45:54+07:00
weight: 1
---

## **Announcing Web Search on Amazon Bedrock AgentCore for Agent-Oriented Retrieval**

Amazon Bedrock AgentCore now supports web search as a retrieval source for agents. This feature allows agents to use web pages as a dynamic knowledge base, making them much more capable with up-to-date and context-relevant information.

### **1) What is AgentCore?**
AgentCore is a framework for building intelligent agents on Amazon Bedrock. It combines retrieval and reasoning to help agents answer questions using external sources, including local content, RAG datasets, and now web pages.

### **2) What does this update add?**
The new web search support enables Bedrock agents to retrieve content from the public web. This is especially useful for tasks that require current information or content not captured in existing RAG datasets.

### **3) Why is this important?**
Web search gives agents access to the latest public content without requiring manual dataset updates. It also lets agents reason over more diverse sources, improving accuracy for knowledge-seeking tasks.

### **4) How does Bedrock implement it?**
Amazon Bedrock AgentCore integrates with the web search workflow by first sending the user’s query to a search provider. The results are then converted into passages and used by the agent’s retrieval pipeline to support answers.

### **5) What’s new for retrieval chains?**
The update extends retrieval chain support so agents can combine web search with other Bedrock retrieval sources, such as:
- local files
- structured RAG content
- existing Bedrock retrieval connectors

### **6) Who should use it?**
This feature is ideal for developers building agents that need:
- real-time or recent information
- broad coverage of web content
- context-aware answers from live web search

### **7) How does it compare with existing sources?**
Unlike static RAG datasets, web search is live and continually refreshed. It is not a replacement for curated knowledge bases, but it is a powerful complement when you need current or hard-to-predict content.

### **8) Customer voices**
Many customers are excited about using web search in their agents. It helps them deliver better user experiences in domains like customer support, product discovery, and knowledge retrieval.

### **9) Where to learn more**
If you are already using AgentCore, try adding the new web search source to your retrieval configuration. The Bedrock documentation and release notes include examples for integrating web search with your agents.

### **10) What’s next?**
Expect this feature to evolve with richer search connectors and better ranking for agent retrieval. Amazon Bedrock is continuing to improve agent-based web retrieval so agents can answer more complex questions with current web knowledge.
""",
    "b:/workshop/fcj-workshop-template/content/3-BlogsPosted/3.2-Blog2/_index.md": """---
title: \"Why and How to Migrate to AWS Network Firewall Attached Directly to Transit Gateway (TGW-attached)\"
date: 2024-06-25T11:44:00+07:00
weight: 2
---

## **Why and How to Migrate to AWS Network Firewall Attached Directly to Transit Gateway (TGW-attached)**

Migrating to an AWS Network Firewall deployment directly attached to AWS Transit Gateway (TGW-attached) improves security, scalability, and operational simplicity for multi-account, multi-VPC environments.

### **1) When should you migrate?**
You should consider migrating when your architecture includes multiple VPCs connected through Transit Gateway and you need centralized network protection. TGW-attached Network Firewall is designed to operate at scale across large AWS environments.

### **2) What is the value of TGW-attached Network Firewall?**
Key benefits include:
- centralized, consistent firewall policy enforcement across VPCs
- no need to manage individual firewall appliances per VPC
- easier administration when new VPCs are added
- better support for hybrid and multi-account network topologies

### **3) What changes with the architecture?**
With TGW-attached deployment, traffic flows through Transit Gateway, and Network Firewall policies are applied at the TGW level. This reduces the need for multiple independent inspection points and simplifies routing.

### **4) What does the migration process involve?**
The migration usually includes:
- evaluating your current firewall architecture
- preparing your TGW and route tables
- deploying TGW-attached Network Firewall
- validating policy enforcement and traffic flow
- cutting over from the existing firewall deployment

### **5) When is migration not necessary?**
If you have a small single-VPC environment or require unique per-VPC firewall configurations, the conversion might not be worth the effort. TGW-attached is most valuable in larger, shared network ecosystems.

### **6) What must be planned?**
Migration planning should cover:
- route table design
- firewall rule policy translation
- failure and fallback paths
- monitoring and logging for the TGW firewall deployment

### **7) What are common risks?**
Potential risks include:
- route conflicts during cutover
- incorrect inspection policies
- visibility gaps if logging is not configured properly
- overloading a single inspection point without proper scaling

### **8) What do customers say?**
Teams adopting TGW-attached Network Firewall report better manageability and more consistent security across their AWS network. Centralizing firewall controls helps reduce human error and speeds up deployment of new VPCs.

### **9) How do you start?**
Begin by reviewing your existing network topology and Transit Gateway configuration. Then evaluate the AWS Network Firewall setup options and test the TGW-attached deployment in a staging account before production migration.

### **10) Where to find more detail?**
For further guidance and migration examples, refer to AWS documentation on Transit Gateway Network Firewall attachments and best practices for centralized network security.
""",
    "b:/workshop/fcj-workshop-template/content/3-BlogsPosted/3.3-Blog3/_index.md": """---
title: \"CloudFront in Game Backend: What It Accelerates and Protects, and What It Does Not Replace\"
date: 2024-06-25T11:44:42+07:00
weight: 3
---

## **CloudFront in Game Backend: What It Accelerates and Protects, and What It Does Not Replace**

AWS CloudFront can greatly improve game backend performance, reduce latency, and protect applications from traffic spikes. However, it is important to understand what CloudFront is meant to accelerate and protect, and what it does not replace.

### **1) What does CloudFront accelerate?**
CloudFront accelerates static and dynamic content delivery by caching at edge locations close to players. This is especially useful for assets such as:
- game binaries and client downloads
- game patches and updates
- static UI resources
- API responses when properly configured for edge caching

### **2) What does CloudFront protect?**
CloudFront protects your backend by handling large volumes of requests at the edge, absorbing traffic spikes, and blocking malicious traffic before it reaches the origin. Combined with AWS WAF, CloudFront can defend against DDoS, injection attacks, and other common threats.

### **3) What does CloudFront not replace?**
CloudFront is not a replacement for game server logic or backend state management. It does not replace:
- backend game session management
- player matchmaking systems
- real-time gameplay servers
- database and stateful persistence layers

### **4) Why use CloudFront with a game backend?**
Using CloudFront lets the game backend focus on core gameplay while edge infrastructure handles content delivery, traffic bursts, and security filtering. It is a powerful tool for improving availability and responsiveness.

### **5) Does CloudFront accelerate everything automatically?**
Not always. Dynamic game APIs may still require careful caching rules. You should choose which responses are cacheable and configure headers, query string behavior, and TTL appropriately.

### **6) When should CloudFront be used?**
CloudFront is a good choice when your game backend must serve global players, deliver large assets, or protect APIs from overload. It is especially useful when combined with optimized origins such as S3, Application Load Balancer, or custom HTTP backends.

### **7) What are the limitations?**
Limitations include cache invalidation complexity, the need for correct origin configuration, and the fact that CloudFront is not designed for real-time server-to-server game traffic.

### **8) What do customers say?**
Game teams often report improved startup experience and lower bandwidth costs when using CloudFront for asset delivery. They also value the added security layer and the ability to offload request volume away from their backend.

### **9) What should you verify?**
Check that your CloudFront distribution is configured with the right caching policy, origin protocol, and security settings. Test how your backend behaves under traffic spikes and verify that CloudFront is reducing origin load as intended.

### **10) What is the recommended approach?**
Use CloudFront as a delivery and protection layer for static and cacheable content, while keeping game server logic and stateful APIs in the backend. This hybrid architecture delivers better performance without replacing the backend’s core responsibilities.
"""
}

for path, content in files.items():
    p = Path(path)
    p.write_text(content, encoding='utf-8')

print('Updated files:', ', '.join(files.keys()))
