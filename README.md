
# 📊 A/B Testing Dataset: Email Campaign Performance

This dataset simulates an **A/B test conducted for an email marketing campaign** by an e-commerce company. The goal is to compare the performance of two email formats (Text-heavy vs. Image-rich) in driving user engagement and conversion.

---

## 🗃️ Dataset Overview

| Column Name           | Data Type | Description |
|------------------------|-----------|-------------|
| `user_id`              | Integer   | Unique identifier for each user (1 to 5000). |
| `group`                | Category  | A or B, representing the version of the email received:<br>**A** = Text-heavy email<br>**B** = Image-rich email |
| `email_version`        | String    | Descriptive name for the group:<br>`Text-heavy` for A and `Image-rich` for B |
| `age`                  | Integer   | Age of the user (random value between 18 and 60). |
| `gender`               | Category  | Gender of the user: `M` or `F`. |
| `location`             | Category  | User's state location. One of: `NY`, `CA`, `TX`, `FL`, `IL`. |
| `previous_purchases`   | Integer   | Number of past purchases by the user (simulated using a Poisson distribution). |
| `click`                | Binary    | `1` if the user clicked the email, `0` otherwise.<br>Click probability:<br>• Group A ≈ 15%<br>• Group B ≈ 20% |
| `conversion`           | Binary    | `1` if the user made a purchase after clicking, `0` otherwise. (Only clickers can convert; ≈10% of them do.) |

---

## 🔍 Example Record

| user_id | group | email_version | age | gender | location | previous_purchases | click | conversion |
|---------|-------|----------------|-----|--------|----------|---------------------|--------|-------------|
| 101     | B     | Image-rich     | 34  | F      | CA       | 3                   | 1      | 0           |

➡ This user received the **Image-rich** email, clicked on it, but **did not convert**.

---

## 🎯 Analysis Goals

- **Compare** click-through and conversion rates between email versions
- **Identify** user segments (age, gender, location) that perform better
- **Evaluate** impact of past behavior (`previous_purchases`) on engagement
- **Build a Power BI dashboard** to visualize key metrics and trends
- *(Optional)* Apply machine learning to predict user conversion likelihood

---

## 🧠 Funnel Breakdown

- **Total Users** = 5000
- **Click Rate**:
  - Group A ≈ 15%
  - Group B ≈ 20%
- **Conversion Rate** (post-click):
  - ≈10% across both groups

---

## 📁 File

