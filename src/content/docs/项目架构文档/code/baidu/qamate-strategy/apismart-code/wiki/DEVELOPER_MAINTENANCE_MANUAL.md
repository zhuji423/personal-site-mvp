---
title: "DEVELOPER_MAINTENANCE_MANUAL"
description: "Developer Maintenance Manual for apismart-code"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\wiki\\DEVELOPER_MAINTENANCE_MANUAL.md"
---
Developer Maintenance Manual for apismart-code

---

Purpose

This document is an exhaustive developer-facing maintenance manual for the repository located at /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code. It explains repository layout, responsibilities of each folder, key classes and interfaces, configuration items (Spring properties, environment variables, CI variables), and operational notes (how to run, build, test, and debug). The manual also includes the thinking process used to produce it and a quick navigation map.

Thinking process (summary)
- Performed initial high-level scan of repository structure under baidu/qamate-server for the two main product lines (core and apiExecutor) and supporting modules (api-smart-dispatch, inner-os/itp).  
- Prioritized auth-related components (RequestFilter, UuapToken, OpenApiToken, JwtWrap, Feign Configs) because they are central to both runtime request handling and the planned refactor.  
- Extracted representative files and methods to form canonical descriptions and identify cross-cutting concerns (Feign clients, header propagation, cookie handling, prometheus metrics).  
- Identified the areas most likely to require changes for an OAuth2+JWT migration: Filter/Token utilities, Feign clients and interceptors, product token table and OpenApiToken logic, and configuration.  

Top-level repo overview

- baidu/
  - inner-os/itp: legacy ITP product line and utilities. Contains older Passport-based login implementations and many build scripts. Reference material for backward-compatibility and encryption details.
  - qamate-server: primary product line with three collaborating services:
    - core: business orchestration, controllers/services/managers, MyBatis mappers and entity models. Contains authentication and token handling logic used across the system.
    - apiExecutor: execution engine—controllers accept test-execution requests and call Core via Feign; contains logic to inject cookies to downstream HTTP tests and a small in-memory cache for credentials.
    - api-smart-dispatch: dispatch center based on XXL-JOB; exposes /apismart/dispatch open APIs and calls back into Core (JobCompleteHelper).

Detailed folder responsibilities (core only — prioritized)

- core/src/main/java/com/baidu/qamate/core/apismartmgt/  (apismartmgt)
  - Purpose: High-level orchestration for API smart dispatch and management. Contains Feign client configuration (FeignConfig), dispatch clients (DispatchClient, WorkerClient), and plan-related controllers.
  - Key files:
    - FeignConfig.java: central Feign RequestInterceptor. Adds Authorization header for workerClient, sets special headers for dispatchClient, and uses WorkerClient.getToken to fetch worker token.
    - WorkerClient.java: Feign client for worker service; includes a static method stub getToken used to request tokens from the worker service.

- core/src/main/java/com/baidu/qamate/core/components/config/  (components.config)
  - Purpose: Global web filter, token adaptors, and bean configuration for RequestFilter and token handlers.
  - Key files:
    - RequestFilter.java: Servlet Filter that extracts headers and cookies, validates tokens using OpenApiToken and UuapToken, sets qamate_user attribute, logs/traces and injects ComateAuth tokens.
    - UuapToken.java: Token verifier that uses JwtWrap to decode and set qamate_user.
    - OpenApiToken.java: Legacy opaque token checker that compares incoming token to per-module tokens stored in ProductEntity DB rows (productService). Has hard-coded super/test tokens used by tests and special cases.
    - JwtWrap.java: Wrapper over a JwtUtils implementation (com.baidu.uuap.common.jwt.JwtUtils) with getToken and verifyToken helpers.
    - FilterConfig.java: Spring bean registration wiring RequestFilter into the servlet filter chain.

- core/src/main/java/com/baidu/qamate/core/components/common/
  - Purpose: Common utilities and wrappers used across modules.
  - Key files:
    - ContextHolder.java: stores thread-local request-scoped values (e.g., comateAuthToken, ugate token, module id) used by downstream code.
    - Response.java: standard response wrapper used by controllers.
    - JwtWrap.java: (see above)

- core/src/main/java/com/baidu/qamate/core/v2/**
  - Purpose: v2 modules (kamixmgt, lumosgmt, etc.) contain features like knowledge, kami user token persistence, and feign client configs (ComateAuthClientConfig, KuClientConfig). They interact heavily with RequestFilter to obtain tokens and user context.
  - Key files:
    - AuthController (kamixmgt): APIs for user product list and deletion.
    - KamiUserTokenService: service that persists comate/ugate tokens for users.

- core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/client/
  - Purpose: Feign clients that call other services (worker, dispatch). Many clients rely on FeignConfig for header injection.
  - Key files:
    - WorkerClient.java, DispatchClient.java

- core/src/test/java
  - Purpose: existing unit tests; you will find tests that assert behavior using hard-coded QAMate tokens (e.g., ApiPlanControllerTest). They will need updates after auth refactor.

Executor (apiExecutor) overview (high level)

- apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/
  - controller/: local REST endpoints used by test scripts.
  - common/conf/feign/: Feign client configs for calling Core. These configuration classes add QAMate-Token headers by default to outgoing requests (see QAMateCoreClientConfig.java, QAMateDeviceClientConfig.java).
  - service/: contains AuthService/impl which will call Core /apismart/login endpoint (to be implemented per LOGIN_IMPLEMENTATION_PLAN.md).

Key configuration items in the repo (spring properties & environment variables)

- Core properties (application-*.yml/properties)
  - comate.app-key: used when generating comate API tokens.
  - comate.clientId / comate.clientSecret: used to exchange uuap tokens for comate tokens.
  - uuap.secrete: secret used by JwtWrap/uuap JWT generation & verification.
  - worker.url: base URL for worker service used by WorkerClient.
  - worker.username, worker.password: credentials used by FeignConfig.getWorkerToken() to fetch a worker token.
  - Ku/KuAppToken: used when requesting ugate token for knowledge service.

- Executor properties
  - URLs and credentials for core endpoints (core.url) and any test-runner-specific configuration in application properties.

- Build/CI environment variables
  - See core/ci.yml, api-smart-dispatch/ci.yml and apiExecutor/ci.yml for env variables used during build and publish steps. These include MAVEN profiles (-Pdev, -Ptest), and artifact paths.

Operational notes & how to run locally

- Build core:
  - cd baidu/qamate-server/core
  - mvn clean package (or mvn -Pdev spring-boot:run for dev profile)

- Build executor:
  - cd baidu/qamate-server/apiExecutor
  - mvn -pl executor-server spring-boot:run

- Running tests (module-specific):
  - cd baidu/qamate-server/core
  - mvn test

- Environment and dependencies
  - Many modules rely on internal Maven repos (maven.baidu-int.com). If outside the internal network, builds may fail. You can switch to offline testing by mocking or replacing Feign clients.

Prometheus metrics & tracing

- RequestFilter logs and emits metrics using PrometheusMetricManager and Microscope (MeterRegistry). Key counters:
  - totalCounter: total incoming requests
  - userCounter: successful user-authenticated requests
  - invalidTokenCounter: invalid token occurrences
  - errorReqCounter: malformed requests
- MDC context includes traceId inserted by RequestFilter.

Database notes

- ProductEntity table stores per-module token (used by OpenApiToken). The LOGIN_IMPLEMENTATION_PLAN.md prescribes creating a new table `apismart_auth_credentials` when implementing cookie/password login storage.
- KamiUserTokenService persists comate/ugate tokens to `kamix_user_token` table — used by ContextHolder injection.

Cross-cutting conventions and patterns

- Layering: controller -> service -> manager -> mapper/entity/vo. New code should follow the same structure and naming variants (*mgt for managers).
- Feign clients: use FeignConfig-based RequestInterceptor classes to inject headers and tokens. When changing auth semantics, update these configuration classes first to avoid scattered changes.
- Tokens: multiple token types are in play:
  - QAMate-Token / Kami-Token: opaque per-module tokens (OpenApiToken) used by machine-to-machine calls.
  - QAMate-U-Token / Kami-U-Token: uuap tokens (JWT-like) decoded by UuapToken using JwtWrap.
  - comateAuthToken / ugateToken: generated from uuap cookies and then stored into ContextHolder.

Important classes to know (quick reference)

- com.baidu.qamate.core.components.config.RequestFilter
  - Responsibilities: parse headers/cookies, validate tokens (OpenApiToken / UuapToken), set qamate_user attribute, inject comate/ugate tokens, trace logging, and metrics.
  - Key methods: init(FilterConfig), doFilter(ServletRequest, ServletResponse, FilterChain), injectComateAuthToken(HttpServletRequest)

- com.baidu.qamate.core.components.config.OpenApiToken
  - Responsibilities: validate opaque tokens by comparing with product database entries or hard-coded super tokens.
  - Key method: checkFromToken(String qamateToken, String qamateModuleId, HttpServletRequest request)

- com.baidu.qamate.core.components.config.UuapToken
  - Responsibilities: validate uuap JWT tokens using JwtWrap and set qamate_user.
  - Key method: checkFromToken(String token, HttpServletRequest request)

- com.baidu.qamate.core.components.common.JwtWrap
  - Responsibilities: wrapper around JwtUtils.genToken and verifyToken using configured secret and issuer.

- com.baidu.qamate.core.apismartmgt.manager.FeignConfig
  - Responsibilities: Feign RequestInterceptor that adds headers for dispatchClient and workerClient; fetches worker token via WorkerClient.getToken.

- com.baidu.qamate.core.apismartmgt.manager.client.WorkerClient
  - Responsibilities: Feign client to the worker service; used to fetch worker token via /api/auth/login.

- com.baidu.qamate.core.v2.kamixmgt.service.KamiUserTokenService
  - Responsibilities: persist comate/ugate tokens (saveOrUpdateComateAuthToken, saveOrUpdateUgateToken)

Testing strategy and places to add tests

- Add unit tests for:
  - RequestFilter: forgery of different headers (QAMate-Token, QAMate-U-Token, invalid tokens) and behavior validation (qamate_user set, metrics incremented, response on invalid token).
  - OpenApiToken: verify matching/mismatching tokens and special super tokens.
  - UuapToken + JwtWrap: token generation and verification tests with known secrets.
  - FeignConfig: verify authInterceptor attaches Authorization header and that getWorkerToken fetches tokens as expected (mock WorkerClient).

- Add integration tests:
  - Core Authentication integration test: start application under test profile and use WireMock to mock uuap/comate endpoints (genApiToken, comateAuthClient), test injectComateAuthToken flows.
  - Executor integration test: mock Core endpoints and test caching and fallback logic.

Appendix: Where to look for more (quick file list)
- core/components/config/RequestFilter.java (central filter)
- core/components/config/OpenApiToken.java (opaque token checker)
- core/components/config/UuapToken.java (jwt checker)
- core/components/common/JwtWrap.java (jwt utils)
- core/apismartmgt/manager/FeignConfig.java (feign interceptor)
- core/apismartmgt/manager/client/WorkerClient.java (worker feign client)
- apiExecutor/executor-server/common/conf/feign/*.java (feign configs adding QAMate-Token)
- LOGIN_IMPLEMENTATION_PLAN.md (design doc for login feature)

If you want, I will now create the remaining deliverables (refactor plan, complex-function annotations, and the generated test scaffolding) under apismart-code/wiki. I will follow the OAuth2 + JWT (JWKS) model by default (client_credentials for services and Resource Owner Password Credentials for automated username/password flows) and include an incremental compatibility strategy that preserves legacy headers behind a feature flag. If you prefer a different OAuth grant type, tell me and I will adapt the plan.

