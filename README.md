# Aruna Computers Care (Namma Ooru Service - ACC)

Welcome to the **Aruna Computers Care** digital platform! This repository contains the complete frontend architecture for a highly responsive, modern IT service and hardware repair storefront designed primarily for households and businesses in Sivakasi.

## 🚀 Objective
The primary objective of this project is to create an elegant, incredibly fast, and user-friendly digital platform for **Aruna Computers Care**. Historically, scheduling hardware repairs or purchasing specialized peripherals required physical visits. This platform bridges that gap by offering:
- **Instant Service Requests:** Book repairs for laptops, desktops, and printers instantly.
- **Dynamic E-Commerce Showcase:** View hardware inventories directly integrated from our live backend.
- **Seamless Notifications:** Keep customers updated with real-time lifecycle tracking.

## 🖥️ Technology Stack
This platform is built primarily focusing on high-speed static delivery and complex Javascript manipulation for state handling without the overhead of heavy SPA frameworks.

- **Frontend Core:** Pure HTML5, CSS3, and Vanilla JavaScript.
- **Styling Architecture:** Custom-compiled **Tailwind CSS (CDN)** integrated with native CSS variables for extreme customizability, dark/light mode hooks, and precise Flexbox/Grid responsive scaling.
- **Database / Backend:** **Google Sheets (CSV Export)** is utilized as an ultra-lightweight dynamic database to render hardware products (laptops, accessories, etc.) into the frontend instantly via the PapaParse extraction method.
- **Session Management:** HTML5 `localStorage` dictates user authentication logic seamlessly without requiring complex SQL databases, permitting direct-login functionality.

## 🗂️ Code Structure
The codebase follows a modular HTML architecture, grouping similar user experiences into designated files while dynamically sharing core CSS stylesheets.

- `home.html` - The central landing page featuring hero banners, quick navigation tokens, and the dynamic search system.
- `service.html` - Core booking form integrating direct-to-backend submission APIs to capture customer service queries.
- `profile.html` - Customer dashboard handling Login/Signup mechanisms natively through localStorage saving.
- `product.html` (and subcategories `laptops.html`, `desktops.html`, etc.) - Dynamic layout files that use fetch APIs to parse external inventory sheets and render beautiful CSS inventory cards populated with price tags and checkout features.
- `style.css` - The foundational Global CSS system declaring deep-level color palettes, hover micro-interactions, and navbar behaviors.

## 📞 Integrations: Managers & Messaging
To make the platform genuinely useful, it features smart hook integrations mapping digital elements to real-world communication:

1. **Manager Call Network (`Ask Manager` Button)**
   - Every product card injected into the document features an **Ask Manager** action.
   - **Technique:** This employs the native HTML anchor `tel:` protocol (`<a href="tel:+919876543210">`). Clicking this immediately skips intermediate steps and opens the device's native phone dialer to directly bridge a communication link for pricing reviews and personalized support.

2. **Backend Submission (Make.com & Supabase)**
   - **Technique:** To handle service requests, the frontend utilizes JavaScript `fetch()` calls to send JSON payloads to an active backend webhook/Supabase instance. 
   - Once the submission payload hits the database, external automation tools (like **Make.com / Twilio**) are structurally mapped to listen for these database insertions. When a new row is detected, the webhook triggers automated **Email** and **WhatsApp** notifications to both the customer and the service team!

## ✨ Features
- **Perfect Aesthetics:** Blends sleek blues (`#004d99`) and contrast oranges (`#ff9800`) seamlessly.
- **Responsiveness First:** Utilizing `min-w`, viewport thresholds, and mobile bottom navigation bars guarantees identical feature-parity on a 5-inch phone and a 32-inch monitor.

### Written with passion to elevate Namma Ooru Services!
