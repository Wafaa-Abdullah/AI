#!/usr/bin/env python
# coding: utf-8

# # Task 1:Ternary search?
# It is similar to binary search where we divide the array into two parts but in it, we divide the given array into three parts and determine which has the key. We can divide the array into three parts by taking mid1 and mid2 which can be calculated. Initially, l and r will be equal to 0 and n-1, where n is the length of the array. 
# Its time complexity is O(log n base 3) and that of binary search is O(log n base 2).
# It must be sorted as binary search
# mid1 = l + (r-l)/3 
# mid2 = r – (r-l)/3 
# 
# Steps to perform Ternary Search: 
# First, we compare the key with the element at mid1. If found equal, we return mid1.
# If not, then we compare the key with the element at mid2. If found equal, we return mid2.
# If not, then we check whether the key is less than the element at mid1. If yes, then recur to the first part.
# If not, then we check whether the key is greater than the element at mid2. If yes, then recur to the third part.
# If not, then we recur to the second (middle) part.

# # Task 2: Design patterns
# 
# Creational Design Patterns
# 1)Factory Method: Creates objects with a common interface and lets a class defer instantiation to subclasses.
# 2)Abstract Factory: Creates a family of related objects.
# 3)Builder: A step-by-step pattern for creating complex objects, separating construction and representation.
# 4)Prototype: Supports the copying of existing objects without code becoming dependent on classes.
# 5)Singleton: Restricts object creation for a class to only one instance.
# Structural Design Patterns
# 1)Adapter: How to change or adapt an interface to that of another existing class to allow incompatible interfaces to work together.
# 2)Bridge: A method to decouple an interface from its implementation.
# 3)Composite: Leverages a tree structure to support manipulation as one object.
# 4)Decorator: Dynamically extends (adds or overrides) functionality.
# 5)Façade: Defines a high-level interface to simplify the use of a large body of code.
# 6)Flyweight: Minimize memory use by sharing data with similar objects.
# 7)Proxy: How to represent an object with another object to enable access control, reduce cost and reduce complexity.
# Behavioral Design Patterns
# 1)Chain of Responsibility: A method for commands to be delegated to a chain of processing objects.
# 2)Command: Encapsulates a command request in an object.
# 3)Interpreter: Supports the use of language elements within an application.
# 4)Iterator: Supports iterative (sequential) access to collection elements.
# 5)Mediator: Articulates simple communication between classes.
# 6)Memento: A process to save and restore the internal/original state of an object.
# 7)Observer: Defines how to notify objects of changes to other object(s).
# 8)State: How to alter the behavior of an object when its stage changes.
# 9)Strategy: Encapsulates an algorithm inside a class.
# 10)Visitor: Defines a new operation on a class without making changes to the class.
# 11)Template Method: Defines the skeleton of an operation while allowing subclasses to refine certain steps.

# # Task 3:Difference between Agile and DevOps
# Agile versus DevOps is that Agile is a philosophy about how to develop and deliver software(in iterative method), while DevOps describes how to continuously deploy code through the use of modern tools and automated processes.

# # What are the tools used in DevOps?
# DevOps Automation Tools
# 1. Jenkins
# 2. Docker
# 3. Puppet
# 4. Apache Maven
# 5. Gradle
# DevOps Pipeline (CI/CD) Tools
# 6. CircleCI
# 7. Bamboo
# 8. TeamCity
# 9. Travis CI
# 10. Buddy
# DevOps Version Control Tools
# 11. Git
# 12. GitHub
# DevOps Configuration Management Tools
# 13. Chef
# 14. Kubernetes
# 15. Ansible
# 16. Vagrant
# 17. Consul
# 18. Terraform
# DevOps Testing Tools
# 19. Selenium
# 20. Tricentis Tosca
# 21. TestSigma
# 22. IBM Rational Functional Tester
# 23. SoapUI
# DevOps Monitoring Tools
# 24. Nagios
# 25. Prometheus
# 26. New Relic
# 27. PagerDuty
# 28. Sensu
# 29. Splunk
# 30. ELK Stack
# 
# 
