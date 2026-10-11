---
title: "TESTS_GENERATED"
description: "Tests generated unit and integration for Core authentication components"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\wiki\\TESTS_GENERATED.md"
---
Tests generated (unit and integration) for Core authentication components

Purpose

This document contains runnable test code skeletons (unit tests and integration tests) that cover the core authentication components (RequestFilter, UuapToken, OpenApiToken, FeignConfig) and the expected edge cases: missing tokens, invalid tokens, valid Bearer JWT tokens, compatibility fallback to legacy headers, and feign interceptor behavior (Authorization header injection). Tests use JUnit 5, Mockito, and WireMock for integration tests.

Notes before adding tests
- Add test dependencies to core/pom.xml if not present:
  - junit-jupiter
  - mockito-core
  - mockito-junit-jupiter
  - spring-boot-starter-test (includes MockMvc)
  - wiremock-jre8 (for WireMock)

Unit test: RequestFilterTest (core/src/test/java/.../RequestFilterTest.java)

Description: Tests doFilter behavior for missing token, legacy token (OpenApiToken), and Bearer JWT (new flow). Uses Mockito to stub OpenApiToken and UuapToken beans.

Code (skeleton):

```java
package com.baidu.qamate.core.components.config;

import com.baidu.qamate.core.components.common.Response;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.mock.web.MockFilterChain;
import org.springframework.mock.web.MockHttpServletRequest;
import org.springframework.mock.web.MockHttpServletResponse;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

class RequestFilterTest {

    @InjectMocks
    RequestFilter requestFilter;

    @Mock
    OpenApiToken openApiToken;

    @Mock
    UuapToken uuapToken;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void testDoFilter_missingToken_returnsFail() throws Exception {
        MockHttpServletRequest req = new MockHttpServletRequest();
        req.setMethod("GET");
        req.setRequestURI("/api/test");

        MockHttpServletResponse resp = new MockHttpServletResponse();
        MockFilterChain chain = new MockFilterChain();

        requestFilter.doFilter(req, resp, chain);

        String content = resp.getContentAsString();
        assertTrue(content.contains("Token为空"));
        assertEquals(200, resp.getStatus());
    }

    @Test
    void testDoFilter_openApiToken_valid_passesFilter() throws Exception {
        MockHttpServletRequest req = new MockHttpServletRequest();
        req.addHeader(RequestFilter.QAMATE_TOKEN, "valid-token");
        req.addHeader(RequestFilter.QAMATE_MODULEID, "42");
        MockHttpServletResponse resp = new MockHttpServletResponse();
        MockFilterChain chain = new MockFilterChain();

        when(openApiToken.checkFromToken(eq("valid-token"), eq("42"), any())).thenReturn(true);

        requestFilter.doFilter(req, resp, chain);

        // If valid, the filter should pass the request down the chain (MockFilterChain will have a non-null request)
        assertNotNull(chain.getRequest());
    }

    @Test
    void testDoFilter_uuapToken_valid_setsQamateUser() throws Exception {
        MockHttpServletRequest req = new MockHttpServletRequest();
        req.addHeader(RequestFilter.QAMATE_UUAP_TOKEN, "uuap-token");
        MockHttpServletResponse resp = new MockHttpServletResponse();
        MockFilterChain chain = new MockFilterChain();

        when(uuapToken.checkFromToken(eq("uuap-token"), any())).thenAnswer(invocation -> {
            var request = invocation.getArgument(1, javax.servlet.http.HttpServletRequest.class);
            request.setAttribute("qamate_user", "testuser");
            return true;
        });

        requestFilter.doFilter(req, resp, chain);
        assertNotNull(chain.getRequest());
    }
}
```

Unit test: UuapTokenTest (core/src/test/java/.../UuapTokenTest.java)

Description: Tests jwtWrap interaction and getUserFromToken mapping.

Skeleton:

```java
package com.baidu.qamate.core.components.config;

import com.baidu.qamate.core.components.common.JwtWrap;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import javax.servlet.http.HttpServletRequest;
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

class UuapTokenTest {

    @InjectMocks
    UuapToken uuapToken;

    @Mock
    JwtWrap jwtWrap;

    @BeforeEach
    void setUp(){
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void testCheckFromToken_success_setsAttribute() {
        HttpServletRequest req = mock(HttpServletRequest.class);
        when(jwtWrap.verifyToken("jwt-token")).thenReturn(Map.of("user","alice"));

        boolean ok = uuapToken.checkFromToken("jwt-token", req);
        assertTrue(ok);
        verify(req).setAttribute("qamate_user", "alice");
    }
}
```

Unit test: OpenApiTokenTest

Description: Test legacy token acceptance and super token handling.

Skeleton:

```java
package com.baidu.qamate.core.components.config;

import com.baidu.qamate.core.othermgt.service.ProductService;
import com.baidu.qamate.core.othermgt.entity.ProductEntity;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import javax.servlet.http.HttpServletRequest;
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

class OpenApiTokenTest {
    @InjectMocks
    OpenApiToken openApiToken;

    @Mock
    ProductService productService;

    @BeforeEach
    void setUp() { MockitoAnnotations.openMocks(this); }

    @Test
    void testSuperToken() {
        HttpServletRequest req = mock(HttpServletRequest.class);
        boolean ok = openApiToken.checkFromToken(OpenApiToken.SUPER_QAMATE_TOKEN, "1", req);
        assertTrue(ok);
        verify(req).setAttribute(eq("qamate_user"), any());
    }

    @Test
    void testProductTokenMismatch() {
        HttpServletRequest req = mock(HttpServletRequest.class);
        ProductEntity p = new ProductEntity();
        p.setId(2L);
        p.setToken("abc");
        when(productService.getOne(any())).thenReturn(p);

        boolean ok = openApiToken.checkFromToken("other-token", "2", req);
        assertFalse(ok);
    }
}
```

Unit test: FeignConfigTest (mocking WorkerClient)

Skeleton:

```java
package com.baidu.qamate.core.apismartmgt.manager;

import feign.RequestTemplate;
import org.junit.jupiter.api.Test;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import org.springframework.mock.web.MockHttpServletRequest;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class FeignConfigTest {

    @Test
    void testAuthInterceptor_workerClient_addsAuthorization() {
        // Create a Feign RequestTemplate stub
        RequestTemplate template = new RequestTemplate();
        // Create RequestContextHolder with a mock servlet request
        MockHttpServletRequest servletRequest = new MockHttpServletRequest();
        RequestContextHolder.setRequestAttributes(new ServletRequestAttributes(servletRequest));

        FeignConfig config = new FeignConfig();
        // Using defaults from properties might be required; set values via reflection if needed
        var interceptor = config.authInterceptor();

        template.feignTarget(() -> "workerClient");
        interceptor.apply(template);

        // After applying, Authorization header should be present (may be null token in default impl)
        assertTrue(template.headers().containsKey("Authorization"));
    }
}
```

Integration test: CoreAuthIntegrationTest (WireMock)

- Use WireMock to mock JWKS endpoint and token introspection for JWT verification, and to mock uuap/comate endpoints used by injectComateAuthToken.
- Place tests under core/src/test/java/.../integration/

Skeleton (concept):

```java
// Use @SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
// Start WireMockServer before tests and configure application-test.properties to point oauth.jwks-uri and token endpoints to WireMock

// Test cases:
// - valid JWT: start WireMock return JWKS & a valid JWT verification path; perform HTTP call to application endpoint and assert request passes
// - invalid JWT: wiremock returns 401; assert filter returns Token非法
// - legacy token fallback: when auth.compatibility.enabled=true, mock productService to return matching token and assert pass
```

Run commands

- Unit tests (module):

```bash
cd baidu/qamate-server/core
mvn -Dtest=RequestFilterTest,UuapTokenTest,OpenApiTokenTest,FeignConfigTest test
```

- Integration tests (requires WireMock & test profile):

```bash
cd baidu/qamate-server/core
mvn verify -Pintegration-tests
```

Where to add these tests

- Unit tests: add to src/test/java under corresponding packages (mirror main package structure)
- Integration tests: add to src/test/java under an integration package and guard with profile or maven profile

Next steps I can take automatically

- Create these test files in the repository under the suggested paths and run `mvn -pl core test` to validate compilation and some test runs (requires building the module; may need dependency resolution and local Maven settings). I can also add WireMock test dependency to pom.xml if permitted.


