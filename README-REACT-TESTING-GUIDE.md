# React Testing Guide: Senior Engineer Edition

A comprehensive, interactive guide to mastering **React Testing Library (RTL)** and **Vitest** for production-grade applications.

## 🚀 Overview
This guide is designed for developers who want to move beyond basic unit tests and implement robust, accessibility-first testing strategies that ensure reliability in high-stakes production environments.

## 🛠️ Tech Stack Covered
- **Runner**: Vitest (Modern, fast Vite-native test runner)
- **Library**: React Testing Library (Querying and Assertions)
- **Interactions**: `@testing-library/user-event`
- **Mocking**: Mock Service Worker (MSW) & Vitest Mocks
- **Standards**: WCAG Accessibility (jest-axe)

## 📖 What's Inside?
1.  **Testing Strategy**: The Testing Trophy vs. The Testing Pyramid.
2.  **Environment Setup**: Configuring Vitest with JSDOM and globals.
3.  **Querying RTL**: Master role-based queries and the query hierarchy.
4.  **Asynchronous Testing**: Handling `find*` queries and `waitFor`.
5.  **Senior Mocking Patterns**: MSW for APIs, module mocking, and dependency injection.
6.  **Advanced Logic**: Testing Custom Hooks, Context, Redux, and Routers.
7.  **Quality Gates**: Accessibility auditing, Snapshots, and CI/CD integration.
8.  **The Assertions Toolbelt**: A deep dive into `describe`, `it`, and `expect` matchers.

## 🖥️ How to Use
1.  Open `react-testing-guide.html` in any modern browser.
2.  Use the **Search Bar** to find specific topics (e.g., "MSW", "Hook").
3.  Filter by **Category** (Fundamentals vs. Advanced).
4.  Click on any topic to see:
    - **Senior Definition**: Concise, high-level explanation.
    - **Pro Tip**: Real-world advice from senior engineers.
    - **Code Examples**: Copy-pasteable snippets with syntax highlighting.
    - **Step-by-Step Breakdown**: Detailed explanation of the implementation.

## 🎯 Production Best Practices
- **Accessibility First**: Always use `getByRole` before `getByTestId`.
- **Black Box Testing**: Test behavior, not implementation details.
- **Isolation**: Reset mocks and stores between every test case.
- **Resilience**: Use MSW to mock the network, not the library.

---
*Built for excellence by Antigravity.*
