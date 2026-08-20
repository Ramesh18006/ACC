# Aruna Computers Care (ACC) - Digital Platform

Welcome to the frontend and automation repository for **Aruna Computers Care**, a modern IT service and hardware repair storefront based in Sivakasi. I built this platform to make it incredibly fast and easy for my customers to book service repairs and explore hardware instantly.

## 🚀 What This Does
- **Instant Service Requests:** Customers can book repairs for laptops, desktops, and printers with just a few clicks.
- **Dynamic E-Commerce:** The platform pulls live hardware inventory directly from Google Sheets—no heavy database required!
- **Fast Communication:** Customers can trigger phone dialers natively, or interact with a smart UI for instant help.

## ⚙️ Tech Stack
I focused on keeping the architecture light, fast, and server-less where possible:
- **Frontend Code:** Pure HTML5, CSS3, and Vanilla JavaScript.
- **Styling:** Custom Tailwind CSS (CDN) mixed with Flexbox for absolute responsiveness across every screen size.
- **Dynamic Data:** PapaParse and native `fetch` APIs pull real-time inventory from **Google Sheets**.
- **State Management:** LocalStorage is used for session holding, acting as a zero-OTP login alternative.

## 🔔 Backend & Notifications
To keep my team and my customers in the loop without building a massive backend, I used powerful no-code integrations:
1. **Supabase Database:** All service requests from the frontend are collected into a secure Supabase table using native REST APIs.
2. **Make.com Automation:** When Supabase receives a new row, a Make.com webhook triggers specific workflows:
   - **Telegram API:** Immediately fires a message to my management team via a Telegram Bot, letting us know a new service requests needs review!
   - **Email API:** Automatically sends a professional confirmation email to the customer, thanking them and confirming their request is being handled.

## 📱 Features
- **Responsive Navigation:** Bottom mobile navbars instantly transition into beautiful top-headers for desktop users.
- **Ask Manager Feature:** Direct `tel:` hooks on every single product so customers can immediately dial us for hardware quotes.
- **Integrated Feedback UI:** A custom built interactive 5-star HTML portal for capturing user app experiences natively.

---
*Built to elevate Namma Ooru Services!*
