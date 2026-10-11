---
title: "CLAUDE.md"
description: "This file provides guidance to Claude Code claude.ai/code when working with code in this repository."
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\core_ori\\core\\src\\main\\java\\com\\baidu\\qamate\\core\\CLAUDE.md"
---
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Baidu QAMate Server project, a Spring Boot-based application for question answering and management services. The project follows a multi-module Maven structure with the core module located at `/Users/zhuji_m4pro/code/baidu/core/core_ori/core/`.

## Build System

**Maven-based project** with the following commands:
- `mvn clean compile` - Compile the project
- `mvn clean package` - Build JAR files
- `mvn clean install` - Install to local repository
- `mvn test` - Run unit tests
- `mvn spring-boot:run` - Run the application (from core module)
- `mvn clean test -Dtest=ClassName` - Run specific test class

**Project Structure:**
- Working directory: `/Users/zhuji_m4pro/code/baidu/core/core_ori/core/src/main/java/com/baidu/qamate/core`
- Main application: `QaApplication.java`
- Configuration: `/Users/zhuji_m4pro/code/baidu/core/core_ori/core/src/main/resources/application.yml`

## Architecture

### Package Structure
- `com.baidu.qamate.core` - Main application package
  - `controller/` - REST API endpoints
  - `service/` - Business logic layer
  - `repository/` - Data access layer
  - `entity/` - Database entities
  - `config/` - Configuration classes
  - `util/` - Utility classes
  - `exception/` - Exception handling

### Key Components
- **QaApplication.java** - Spring Boot main application class
- **QueryController.java** - Main REST controller with endpoints for query processing
- **QueryService.java** - Core business logic for query processing and analysis
- Spring Boot with auto-configuration enabled (`@SpringBootApplication`)
- Standard layered architecture (Controller → Service → Repository)

### Database
- Uses Spring Data JPA for data persistence
- Repository interfaces annotated with `@Repository`
- Entity classes with JPA annotations (check for existing entities in the codebase)
- Database configuration in application.yml

## Development Workflow

### Running the Application
1. Navigate to the core module: `cd /Users/zhuji_m4pro/code/baidu/core/core_ori/core`
2. Run with Maven: `mvn spring-boot:run`
3. Application will be accessible via REST endpoints defined in controllers

### Testing
- Test directory: `src/test/java/com/baidu/qamate/core/`
- Run all tests: `mvn test`
- Run specific test class: `mvn test -Dtest=ClassName`
- Run tests in a package: `mvn test -Dtest="com.baidu.qamate.core.service.*"`
- Test naming convention: `*Test.java` or `*Tests.java`

### Code Quality
- No specific code quality configuration files found in the current module
- Follow standard Spring Boot and Java best practices

### Code Organization
- Follow Spring Boot conventions
- Use standard package-by-feature organization
- Controllers handle HTTP requests/responses
- Services contain business logic
- Repositories handle data access
- Entities represent database tables

## Configuration

Application configuration in `application.yml`:
- Server port and basic settings
- Database connection parameters (when configured)
- Logging configuration
- Spring Boot actuator endpoints (if enabled)
- Custom application properties for QAMate functionality

## Important Notes

- This is a multi-module Maven project - always be aware of the current working directory
- Core functionality is in the `core` module at `/Users/zhuji_m4pro/code/baidu/core/core_ori/core/`
- Spring Boot best practices apply throughout the codebase
- Use standard Maven lifecycle commands for building and testing
- REST APIs follow Spring MVC conventions with `@RestController` classes
- Business logic should be implemented in `@Service` classes
- Data access handled through Spring Data JPA repositories