# 📚 Career Mentor Agent – Multi-Agent AI Career Guide

## 📌 Overview
The **Career Mentor Agent** is an AI-powered multi-agent system that guides users through career exploration, skill-building, and job market research.

It uses:
- **Career Agent** → Helps users discover career paths.
- **Skill Agent** → Builds a skill-learning roadmap.
- **Job Agent** → Shows real-world job roles and trends.
- **Google Gemini API** → Generates detailed and structured roadmaps.
- **Chainlit** → Provides an interactive chat UI.

---

## 🧠 How It Works

The system works in **three phases**:

1. **Career Discovery** – Career Agent chats with the user to understand their passions, strengths, education, and work preferences.
2. **Roadmap Generation** – When the user picks a career, the Career Agent calls the `get_career_roadmap` tool to generate beginner → intermediate → advanced skill paths.
3. **Specialized Handoff** – Based on the user’s needs:
   - If they want to **learn skills** → Handoff to **Skill Agent**
   - If they want to **explore jobs** → Handoff to **Job Agent**

Agents can also hand off to each other (Skill ↔ Job).

---

## ⚙️ Agents & Roles

### 1️⃣ Career Agent
- **Role**: Main guide for career discovery.
- **Tasks**:
  - Ask open-ended questions to learn about the user.
  - Suggest **3+ career paths** with a short description and future scope.
  - Call `get_career_roadmap` to provide a structured learning path.
  - Handoff to Skill Agent or Job Agent as needed.

---

### 2️⃣ Skill Agent
- **Role**: Learning coach.
- **Tasks**:
  - List **essential hard and soft skills** for the chosen career.
  - Create a **step-by-step learning roadmap**:
    - Courses, certifications, or workshops
    - Practice projects
    - Timeline (short, mid, long-term)
  - Handoff to Job Agent if the user wants job info.

---

### 3️⃣ Job Agent
- **Role**: Job market expert.
- **Tasks**:
  - Provide **3+ real job roles** for the chosen career:
    - Role description
    - Required skills/certifications
    - Approximate salary range
    - Industries/companies hiring
    - Demand trends
  - Handoff to Skill Agent if the user wants to learn skills.

---

## 🛠 Tool Used

### **`get_career_roadmap`**
- **Purpose**: Generate a beginner → intermediate → advanced skill roadmap for any career.
- **Powered by**: Google Gemini API.
- **Output**: Bullet-point format with clear, actionable steps.


