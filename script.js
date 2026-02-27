// --- STATE ---
let userScore = 0;
let compScore = 0;
let drawScore = 0;
const CHOICES = ["Snake", "Water", "Gun"];
const EMOJIS = { "Snake": "🐍", "Water": "💧", "Gun": "🔫" };

// --- DOM ELEMENTS ---
const userScoreEl = document.getElementById("user-score");
const drawScoreEl = document.getElementById("draw-score");
const compScoreEl = document.getElementById("comp-score");
const resultMsgEl = document.getElementById("result-msg");
const userChoiceDisplayEl = document.getElementById("user-choice-display");
const compChoiceDisplayEl = document.getElementById("comp-choice-display");
const choiceButtons = document.querySelectorAll(".controls .btn");
const restartBtn = document.getElementById("restart");

// --- GAME LOGIC ---
async function playGame(userChoice) {
    toggleButtons(true);
    const selectedBtn = document.getElementById(userChoice.toLowerCase());
    selectedBtn.classList.add("selected");

    try {
        // Send choice to Python Backend
        const response = await fetch('/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ choice: userChoice })
        });
        
        const data = await response.json();

        // Suspense before showing result (UI animation)
        setTimeout(() => {
            updateChoiceDisplays(data.user_choice, data.comp_choice);
            
            if (data.winner === "user") {
                userScore++;
                updateResultMessage(data.result, "#2ecc71");
                updateScore(userScoreEl, userScore);
            } else if (data.winner === "computer") {
                compScore++;
                updateResultMessage(data.result, "#e74c3c");
                updateScore(compScoreEl, compScore);
            } else {
                drawScore++;
                updateResultMessage(data.result, "#f39c12");
                updateScore(drawScoreEl, drawScore);
            }

            // Reset UI state
            setTimeout(() => {
                toggleButtons(false);
                selectedBtn.classList.remove("selected");
                userScoreEl.classList.remove("updated");
                compScoreEl.classList.remove("updated");
                drawScoreEl.classList.remove("updated");
            }, 800);
        }, 400);

    } catch (error) {
        console.error("Error connecting to backend:", error);
        updateResultMessage("Server Error! Is Flask running?", "red");
        toggleButtons(false);
        selectedBtn.classList.remove("selected");
    }
}

function restartGame() {
    userScore = 0;
    compScore = 0;
    drawScore = 0;
    userScoreEl.innerText = "0";
    compScoreEl.innerText = "0";
    drawScoreEl.innerText = "0";
    updateResultMessage("Choose your weapon!", "white");
    userChoiceDisplayEl.innerText = "You: ❓";
    compChoiceDisplayEl.innerText = "Comp: ❓";
}

// --- UI UPDATE FUNCTIONS ---
function updateChoiceDisplays(userChoice, compChoice) {
    userChoiceDisplayEl.innerText = `You: ${EMOJIS[userChoice]}`;
    compChoiceDisplayEl.innerText = `Comp: ${EMOJIS[compChoice]}`;
}

function updateResultMessage(message, color) {
    resultMsgEl.innerText = message;
    resultMsgEl.style.color = color;
    // Trigger animation
    resultMsgEl.classList.remove("animate");
    void resultMsgEl.offsetWidth; // Reflow to restart animation
    resultMsgEl.classList.add("animate");
}

function updateScore(element, score) {
    element.innerText = score;
    element.classList.add("updated");
}

function toggleButtons(disabled) {
    choiceButtons.forEach(button => {
        button.disabled = disabled;
    });
}

// --- EVENT LISTENERS ---
choiceButtons.forEach(button => {
    button.addEventListener("click", () => {
        // The second part of the button's text is the choice (e.g., "🐍 Snake")
        const choice = button.innerText.split(" ")[1];
        playGame(choice);
    });
});

restartBtn.addEventListener("click", restartGame);

// --- INITIALIZE ---
restartGame();
