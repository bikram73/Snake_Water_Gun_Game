# 🐍 Snake Water Gun Game 🔫

A modern, interactive adaptation of the classic **Snake Water Gun** game (similar to Rock Paper Scissors). This project offers two ways to play: a **Web Application** built with Flask and a **Desktop Application** built with Tkinter.

![Game Preview](https://via.placeholder.com/800x400?text=Snake+Water+Gun+Game+UI) 
*(Replace this link with a screenshot of your actual game after running it)*

## 🚀 Features

- **🎮 Dual Platforms**: Play on the Web or as a Desktop App.
- **🎨 Modern Web UI**: Glassmorphism design with smooth CSS animations.
- **🤖 Smart Backend**: Python logic handles random computer choices and score tracking.
- **📊 Score Tracking**: Real-time tracking of User wins, Computer wins, and Draws.
- **📱 Responsive**: Works on Desktop and Mobile.

## 📂 Project Structure

```text
Snake_Water_Gun_Game/
│
├── 📄 index.html        # Main Game Interface
├── 🎨 style.css         # Modern UI Styling (Glassmorphism)
├── 📜 script.js         # Frontend Logic & API Calls
├── 🖥️ main.py           # Desktop: Tkinter Game App
├── 🐍 server.py         # Flask Backend (Game Logic)
├── ⚙️ requirements.txt  # Python Dependencies
├── 🚀 vercel.json       # Vercel Deployment Config
└── 📝 README.md         # Project Documentation
```

## 🛠️ Installation & Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-username/snake-water-gun.git
    cd snake-water-gun
    ```

2.  **Install Dependencies**
    Make sure you have Python installed.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    python server.py
    ```

4.  **Play!**
    Open your browser and go to: `http://127.0.0.1:5000`

## 🌐 Deployment

### Deploying to Vercel

This project is configured for easy deployment on Vercel.

1.  Push your code to **GitHub**.
2.  Log in to Vercel.
3.  Click **"Add New..."** -> **"Project"**.
4.  Import your GitHub repository.
5.  Vercel will detect the `vercel.json` and `requirements.txt`.
6.  Click **Deploy**.

## 🧠 Game Logic

| You Choose | Computer Chooses | Result |
| :--- | :--- | :--- |
| 🐍 Snake | 💧 Water | **Win** 🎉 |
| 💧 Water | 🔫 Gun | **Win** 🎉 |
| 🔫 Gun | 🐍 Snake | **Win** 🎉 |
| *Same* | *Same* | **Draw** 😐 |
| *Other* | *Other* | **Lose** 🤖 |

---

Made with ❤️ and Python.
```
