
# FastAPI Books Project - Project Description

## Overview
This project demonstrates the fundamentals of FastAPI by building a books management system. It covers all basic HTTP request methods (GET, POST, PUT, DELETE) and CRUD operations.

## Objective
Learn FastAPI basics through practical implementation of a books database with full CRUD functionality.

## Features

### Data Structure
Each book contains:
- **Title**: Title One through Title Five
- **Author**: Author One through Author Five
- **Category**: Science, History, Math

### CRUD Operations
- **Create**: Add new books to the list (POST)
- **Read**: Retrieve all books or specific books (GET)
- **Update**: Modify existing book details (PUT)
- **Delete**: Remove books from the list (DELETE)

## HTTP Request Methods
| Operation | HTTP Method |
|-----------|-------------|
| Create    | POST        |
| Read      | GET         |
| Update    | PUT         |
| Delete    | DELETE      |

## Key Concepts
- **Request/Response Pattern**: Client requests data → FastAPI server processes → Server responds
- **Swagger UI**: Built-in interactive documentation at `/docs` endpoint
- **Endpoints**: RESTful endpoints for managing book resources

## Tools & Technologies
- FastAPI framework
- Swagger UI for API testing and documentation
