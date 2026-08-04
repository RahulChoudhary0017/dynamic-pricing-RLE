# 🏨 Dynamic Pricing using Reinforcement Learning (Q-Learning)

> An AI-powered Dynamic Pricing System that uses **Reinforcement Learning (Q-Learning)** to maximize hotel revenue by learning the optimal pricing strategy based on inventory, booking days, and competitor pricing.

---

## 📌 Project Overview

Dynamic pricing is widely used in industries such as hotels, airlines, ride-sharing, and e-commerce. Instead of keeping prices fixed, businesses adjust prices according to market demand and competition.

In this project, a **Q-Learning Agent** learns the best pricing policy through continuous interaction with a custom Gymnasium environment.

---

## 🎯 Problem Statement

Hotels often face two major challenges:

* Setting prices too low reduces overall revenue.
* Setting prices too high decreases customer demand.

The objective of this project is to build an intelligent pricing agent capable of maximizing revenue automatically.

---

## 💡 Solution

The project simulates a hotel booking environment where the Reinforcement Learning agent learns to:

* Analyze the current inventory.
* Observe remaining booking days.
* Compare competitor pricing.
* Predict customer demand.
* Select the most profitable room price.

The agent continuously updates its Q-Table to improve future pricing decisions.

---

# 🏗️ System Architecture

```text
Environment
     │
     ▼
Current State
(Inventory, Days Left, Competitor Price)
     │
     ▼
Q-Learning Agent
     │
     ▼
Choose Best Price
     │
     ▼
Customer Demand
     │
     ▼
Revenue & Reward
     │
     ▼
Q-Table Update
     │
     ▼
Next State
```

---

# 🔄 Workflow

```text
Start
   │
Reset Environment
   │
Generate Current State
   │
Agent Chooses Price
   │
Customer Demand Simulation
   │
Revenue Calculation
   │
Reward Calculation
   │
Update Q-Table
   │
Episode Finished?
   │
No ────────────────► Continue Training
   │
Yes
   │
Training Complete
```

---

# 🚀 Features

* ✅ Custom Gymnasium Environment
* ✅ Q-Learning Algorithm
* ✅ Dynamic Pricing Strategy
* ✅ Dynamic Customer Demand
* ✅ Competitor Price Simulation
* ✅ Reward Engineering
* ✅ Revenue Optimization
* ✅ Training Reward Visualization
* ✅ Moving Average Graph
* ✅ Strategy Performance Comparison

---

# 🛠️ Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Programming Language   |
| Gymnasium  | RL Environment         |
| NumPy      | Numerical Computation  |
| Matplotlib | Visualization          |
| Pickle     | Model Saving           |
| Q-Learning | Reinforcement Learning |

---

# 📂 Project Structure

```text
dynamic-pricing-RLE/
│
├── agents/
│   └── q_learning.py
│
├── env/
│   └── pricing_env.py
│
├── utils/
│   └── demand.py
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── diagrams/
│   └── screenshots/
│
├── outputs/
│   ├── reward_curve.png
│   ├── moving_average.png
│   ├── comparison.png
│   ├── training_summary.txt
│   └── q_table.pkl
│
├── train.py
├── evaluation.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone git clone https://github.com/RahulChoudhary0017/dynamic-pricing-RLE.git
```

Move to project directory:

```bash
cd dynamic-pricing-RLE
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Training

```bash
python train.py
```

---

# ▶️ Evaluation

```bash
python evaluation.py
```

---

# 📊 Final Results

| Strategy           |         Revenue |
| ------------------ | --------------: |
| 🥇 Fixed Strategy  | **310,191,000** |
| 🤖 Q-Learning      | **290,180,000** |
| 🎲 Random Strategy | **257,143,000** |

---

# 📈 Generated Outputs

The project automatically generates:

* Reward Curve
* Moving Average Curve
* Revenue Comparison Graph
* Training Summary
* Learned Q-Table

---

# 📸 Screenshots

Add the following screenshots from the `docs/screenshots` folder:

* Reward Curve
* Moving Average
* Revenue Comparison
* Training Output
* Evaluation Output

---

# 🔮 Future Improvements

* Deep Q-Network (DQN)
* PPO (Proximal Policy Optimization)
* Multi-Agent Reinforcement Learning
* Seasonal Demand Forecasting
* Real-Time Pricing API
* Interactive Dashboard using Streamlit

---

# 📚 Learning Outcomes

Through this project, I learned:

* Reinforcement Learning Fundamentals
* Q-Learning Algorithm
* Reward Engineering
* Environment Design using Gymnasium
* AI-based Pricing Optimization
* Git & GitHub Workflow
* Project Documentation

---

👨‍💻 Author

Rahul Choudhary

🎓 B.Tech – Computer Science (AI & DS)

💼 Aspiring AI / ML Engineer

🐙 GitHub: https://github.com/RahulChoudhary0017

📂 Project Repository: https://github.com/RahulChoudhary0017/dynamic-pricing-RLE

🔗 LinkedIn: https://www.linkedin.com/in/rahul-choudhary-b55062317

⭐ Support

If you found this project helpful, please consider giving it a ⭐ Star on GitHub.

Thank you for visiting this repository!